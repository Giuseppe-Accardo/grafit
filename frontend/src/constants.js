let BASE_URL = window.location.origin.toString() + "/"

if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1" || window.location.hostname === "0.0.0.0") {
    BASE_URL = 'http://' + window.location.hostname + ':8000/'
}

export const AUTH_API = BASE_URL + 'api-token-auth/'
export const API = BASE_URL + 'api/v1/'

export const JWT_LOCALSTOR_KEY = 'jwt';

export const ARTICLE_ENDPOINT = "articles/"
