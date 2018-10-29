# -*- coding:utf-8 -*-
import json
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *
# Register your models here.

#models
class english_dict_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = english_dict_Resource
    list_display = ('dict_name', 'details', 'n_all')
    search_fields = ('dict_name', 'details')
    def n_all(self, obj):
        try:
            return len(json.loads(obj.words))
        except Exception as e:
            return "null"
    n_all.short_description = "词库总单词数"
    readonly_fields = ('n_all',)


class score_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = score_Resource
    list_display = ('username', 'dict_name', 'n_learned', 'n_all')
    search_fields = ('username', 'dict_name')

    def n_learned(self, obj):
        try:
            return len(json.loads(obj.learned_words))
        except:
            return "null"
    n_learned.short_description = "词库已背单词数"

    def n_all(self, obj):
        try:
            words = english_dict.objects.get(dict_name=obj.dict_name).words
            return len(json.loads(words))
        except:
            return "null"
    n_all.short_description = "词库总单词数"
    readonly_fields = ('n_learned', 'n_all')

admin.site.register(english_dict, english_dict_Admin)
admin.site.register(score, score_Admin)
