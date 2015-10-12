class PlayRouter(object):
    """
    A router to control all database operations on models in
    the questionnaire application
    """

    def db_for_read(self, model, **hints):
        """
        Point all operations on questionnaire models to 'db3'
        """
        if model._meta.app_label == 'questionnaire':
            return 'db3'
        return None

    def db_for_write(self, model, **hints):
        """
        Point all operations on questionnaire models to 'other'
        """
        if model._meta.app_label == 'questionnaire':
            return 'db3'
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the 'questionnaire' app only appears on the 'other' db
        """
        if db == 'db3':
            return model._meta.app_label == 'questionnaire'
        elif model._meta.app_label == 'questionnaire':
            return False
        return None
