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
You need to install 

        pip install pymysql
        
Edit your manage.py to look like this

        #!/usr/bin/env python
        import os
        import sys
        try:
            import pymysql
            pymysql.install_as_MySQLdb()
        except ImportError:
            pass 
        
        if __name__ == "__main__":
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fenland_api.settings")
            from django.core.management import execute_from_command_line
            execute_from_command_line(sys.argv)


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
    
Also in the project settings add the setting

    DATABASE_ROUTERS = ['questionnaire.routers.PlayRouter',]
    

