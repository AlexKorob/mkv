ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": "mkv",
        "USER": "alex",
        "PASSWORD": "123",
        "HOST": "localhost",
        "PORT": "5432"
    }
}
