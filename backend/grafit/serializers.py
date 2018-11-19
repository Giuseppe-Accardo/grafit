from django.contrib.auth.models import Group
from rest_framework import serializers
from .concept_runner import ConceptRunner

from .models import User, Article, Workspace, GraphArticle


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email',
                  'groups', 'first_name', 'last_name')


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('url', 'username', 'password',
                  'first_name', 'last_name', 'email',)
        extra_kwargs = {'password': {'write_only': True}}


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class SubArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('url', 'id', 'title')


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('id', 'url', 'name', 'initials')


class ArticleSerializer(serializers.ModelSerializer):
    related = SubArticleSerializer(required=False, many=True)

    class Meta:
        model = Article
        fields = ('id', 'url', 'title', 'text',
                  'related', 'workspace', 'created_at', 'updated_at')

    def _save_related(self, article):
        ConceptRunner.generate_concepts_for_article(article.id)
        article_node = GraphArticle.nodes.get_or_none(uid=article.id)
        relatedArticles = article_node.related

        for relatedArticle in relatedArticles:
            article.related.add(Article.objects.get(pk=relatedArticle.uid))

        article.save()

    def create(self, validated_data):
        article = Article.objects.create(**validated_data)
        self._save_related(article)
        return article

    def update(self, instance, validated_data):
        super(ArticleSerializer, self).update(instance, validated_data)
        self._save_related(instance)
        return instance
