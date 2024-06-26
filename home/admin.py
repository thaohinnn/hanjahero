from django.contrib import admin

from home.models.question import Question
from home.models.question_meta_data import QuestionMetaData
from home.models.test_history import TestHistory
from home.models.user import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from home.models.user_test_result import UserTestResult
from home.models.user_post import Post


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question


class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource


# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionMetaData)
admin.site.register(TestHistory)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(UserTestResult)
