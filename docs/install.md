
##Installation

Django-fsq is a package which works with Django.  Install with pip

    pip install git+git://github.com/cam-mrc-epid/django-fsq

This will install it directly into your site-packages directory.  If you are using virtualenv, this will be inside the Lib folder at your virtualenv's home directory.  Alternatively if you can install it like this

    pip install -e git+git://github.comcam-mrc-epid/django-fsq#egg=django-fsq

This will create a source folder in your virtulenv home folder and clones the entire package to that folder.  This requires git to be installed on your system.  You can work with the code directly in this location and use git there as normal.

##Config

There are 2 options for using the package.

###Case 1 - Normal Django using default database

In your project settings, add to INSTALLED_APPS

```python
'questionnaire',
'import_export',
```

then
```python
python manage.py migrate
```

###Case 2 - Set up with pre-existing MySQL database
For any pre-existing database you will have to set up the backend in your settings file in the normal way.  For MySQL you can use pymysql

    pip install pymsql

To use pymysql add in your manage.py immediately under `import sys`

```python
    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass 
```

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

The db name in your django settings has to be 'db3' in order for the routers in the questionnaire to connect up.
    
##Uninstall

    pip uninstall django-fsq
