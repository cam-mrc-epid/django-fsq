# Django FSQ

Django-fsq is a packaged app version of the models for the Forms System MySQL Database.  You need to have Django installed and add it to your project.

##Features
It provides models to make it easy to connect up to the form system and use Django's Object Relational Mapper (ORM) to work with the database.  It can be set up to use a local Sqlite database or another existing database.  

It provides a router that allows connections to non-default databases.

It connects the models to Django's admin system so they can be managed there.  There is export functionality for each table.

Django-fsq provides Users, Groups, Progress, Questionnaires, Results and Roles models, that match up to the Forms System MySQL Database.  The classes:


```python
class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    password_hash = models.TextField(blank=True)
    salt = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.user_id

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Groups(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    study_name = models.CharField(max_length=50)
    user_group = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return "%s, %s" % (self.user_group, self.user_id)

    class Meta:
        db_table = 'groups'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Progress(models.Model):
    user = models.ForeignKey(Users)
    questionnaire_id = models.CharField(max_length=50, blank=True)
    started = models.IntegerField(blank=True, null=True)
    finished = models.IntegerField(blank=True, null=True)
    progress_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return self.user.user_id

    class Meta:
        db_table = 'progress'
        verbose_name = 'User Progress'
        verbose_name_plural = 'User Progress'


class Questionnaires(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    study_name = models.CharField(max_length=50)
    user_group = models.CharField(max_length=50)
    questionnaire_id = models.CharField(max_length=50)
    questionnaire_name = models.CharField(max_length=50)
    save_as = models.CharField(max_length=45)

    def __unicode__(self):
        return "%s, %s" % (self.questionnaire_id, self.study_name)

    class Meta:
        db_table = 'questionnaires'
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'


class Results(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    user = models.ForeignKey(Users)
    questionnaire_id = models.CharField(max_length=45)
    var_id = models.CharField(max_length=45, blank=True)
    var_name = models.CharField(max_length=100)
    var_value = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.user.user_id

    class Meta:
        db_table = 'results'
        verbose_name = 'User Result'
        verbose_name_plural = 'User Results'


class Roles(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    role = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s, %s" % (self.user_id)

    class Meta:
        db_table = 'roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
```


