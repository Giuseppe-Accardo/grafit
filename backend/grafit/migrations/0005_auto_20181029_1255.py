# Generated by Django 2.1.2 on 2018-10-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafit', '0004_article_related'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='related',
            field=models.ManyToManyField(blank=True, related_name='_article_related_+', to='grafit.Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
