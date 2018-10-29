# -*- coding:utf-8 -*-
from .models import english_dict, score
from import_export import resources


class english_dict_Resource(resources.ModelResource):

    class Meta:
        model = english_dict


class score_Resource(resources.ModelResource):

    class Meta:
        model = score
