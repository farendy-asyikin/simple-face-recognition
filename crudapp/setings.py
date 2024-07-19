DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'farendfal',
        'PASSWORD': 's3crEt',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

INSTALLED_APPS = [
    'simple-face-recognition',
    'rest_framework',
]

