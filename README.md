# firebase-auth-drf
Firebase Authentication using Django and Django Rest Framework


## Installation
To install all the dependencies just hit this command
```console
pip install -r requirements.txt
```

## Create a Firebase Project
Visit this url https://console.firebase.google.com/ and create a firebase project.
and add the authentication sign-in method.

## Get the firebase project credentials
Open this url https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk select your project and click on generate new private key.
<br />
It will download the ```.json``` file open that file you will get all the credentials, just paste in your .env file.

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

Find out full blog on ```firebase authentication``` <a href="https://pythonworld.io/blogs/how-to-implement-firebase-authentication-in-django-and-dango-rest-framework">here</a>
