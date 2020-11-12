from os import getenv

PORT = getenv("PORT", 8080)
CACHE_HOST = getenv("CACHE_HOST", "localhost")
URI_CONNECTION=f'postgresql://{getenv("DB_USER")}:{getenv("DB_PASSWORD")}@{getenv("DB_HOST")}/{getenv("DB_NAME")}'


