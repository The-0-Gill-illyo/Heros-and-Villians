# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)d0)o@dvca23%)50@8pd-%4nu*w=(jz(yhd5od+89+oo66ippg'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}