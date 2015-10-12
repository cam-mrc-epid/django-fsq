from django.contrib import admin
from questionnaire.models import Users, Results, Progress, Questionnaires, Roles, Groups
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ResultsResource(resources.ModelResource):

    class Meta:
        model = Results


class UsersResource(resources.ModelResource):

    class Meta:
        model = Users


class ProgressResource(resources.ModelResource):

    class Meta:
        model = Progress


class QuestionnairesResource(resources.ModelResource):

    class Meta:
        model = Questionnaires


class RolesResource(resources.ModelResource):

    class Meta:
        model = Roles


class GroupsResource(resources.ModelResource):

    class Meta:
        model = Groups

class UsersAdmin(ImportExportModelAdmin):
    resource_class = UsersResource
    search_fields = ('user_id',)

admin.site.register(Users, UsersAdmin)


class ResultsAdmin(ImportExportModelAdmin):
    resource_class = ResultsResource
    search_fields = ('user__user_id', 'questionnaire_id')
    list_display = ('user', 'questionnaire_id', 'var_id', 'var_name', 'var_value')
    list_filter = ('questionnaire_id',)

admin.site.register(Results, ResultsAdmin)


class ProgressAdmin(ImportExportModelAdmin):
    resource_class = ProgressResource
    list_filter = ('questionnaire_id', 'started', 'finished')
    search_fields = ('user__user_id', 'questionnaire_id')
    list_display = ('user', 'questionnaire_id', 'started', 'finished')

admin.site.register(Progress, ProgressAdmin)


class QuestionnairesAdmin(ImportExportModelAdmin):
    resource_class = QuestionnairesResource
    list_filter = ('study_name', 'questionnaire_id')
    list_display = ('questionnaire_id', 'questionnaire_name', 'study_name')

admin.site.register(Questionnaires, QuestionnairesAdmin)


class RolesAdmin(ImportExportModelAdmin):
    resource_class = RolesResource
    search_fields = ('user__user_id',)
    list_display = ('user_id', 'role')
    list_filter = ('role',)

admin.site.register(Roles, RolesAdmin)


class GroupsAdmin(ImportExportModelAdmin):
    resource_class = GroupsResource
    list_display = ('user_id', 'study_name', 'user_group')
    list_filter = ('study_name', 'user_group')

admin.site.register(Groups, GroupsAdmin)
