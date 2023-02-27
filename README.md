# firebase-auth-drf
Firebase Authentication using Django and Django Rest Framework


## Installation
To install all the dependencies just hit this command
```console
pip install -r requirements.txt
```

## Setup .env file
create a ```.env``` file where ```manage.py``` file is located.

``` .env
FIREBASE_ACCOUNT_TYPE = service_account
FIREBASE_PROJECT_ID = -- Paste FIREBASE_PROJECT_ID here --
FIREBASE_PRIVATE_KEY_ID = -- Paste FIREBASE_PRIVATE_KEY_ID here --
FIREBASE_PRIVATE_KEY = -- Paste FIREBASE_PRIVATE_KEY here --,
FIREBASE_CLIENT_EMAIL = -- Paste FIREBASE_CLIENT_EMAIL here --
FIREBASE_CLIENT_ID = -- Paste FIREBASE_CLIENT_ID here --
FIREBASE_AUTH_URI = https://accounts.google.com/o/oauth2/auth
FIREBASE_TOKEN_URI = https://oauth2.googleapis.com/token
FIREBASE_AUTH_PROVIDER_X509_CERT_URL = https://www.googleapis.com/oauth2/v1/certs
FIREBASE_CLIENT_X509_CERT_URL = -- Paste FIREBASE_CLIENT_X509_CERT_URL here --

```
