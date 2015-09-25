# django-fsq
This is questionnaire django models that fit with the Forms System Mysql DB.  

##Installation

    pip install git+git://github.com/davidgillies/django-fsq
    
##Settings
###Case 1:  Normal django app.  

In your project settings, add to INSTALLED_APPS

    'questionnaire',
    'import_export',

then

    python manage.py migrate
    
###Case 2:  Set up with pre-existing MySQL DB.
You need to install 

        pip install pymysql
        
Add in your manage.py immediately under `import sys`


        try:
            import pymysql
            pymysql.install_as_MySQLdb()
        except ImportError:
            pass 
        



In your project settings, add to INSTALLED_APPS

    'questionnaire',
    'import_export',
    
Also in your project settings add your DB details, e.g. :

    'db3': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mrc_epid_fenland',
        'USER': 'david',
        'PASSWORD': '*****',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    
Also in the project settings add the setting

    DATABASE_ROUTERS = ['questionnaire.routers.PlayRouter',]
    

