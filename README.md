# django-fsq
This is questionnaire django models that fit with the Forms System Mysql DB.  

##Installation

    pip install git+git://github.com/davidgillies/django-fsq
    
##Settings
###Case 1:  Normal django app.  

In your project settings, add to INSTALLED_APPS

    'questionnaire',
    'importexport',

then

    python manage.py migrate
    
###Case 2:  Set up with pre-existing MySQL DB.

In your project settings, add to INSTALLED_APPS

    'questionnaire',
    'importexport',
    
Also in your project settings add your DB details, e.g. :

    'db3': {
        'ENGINE': 'django_mysql_fix.backends.mysql',
        'NAME': 'mrc_epid_fenland',
        'USER': 'david',
        'PASSWORD': '*****',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    
