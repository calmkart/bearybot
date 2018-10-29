# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
import traceback
import logging


import requests
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from . import models as learn_models


# @method_decorator(csrf_exempt, name="dispatch")
class get_dict_list(View):

    def get(self, request):
        try:
            result = [{"dict_name": ed.dict_name, "dict_details": ed.details, "numbers": len(
                json.loads(ed.words))} for ed in learn_models.english_dict.objects.all()]
            return JsonResponse({"result": result})
        except Exception:
            logging.getLogger('app_log').error(traceback.format_exc())


class get_score(View):

    def get(self, request):
        try:
            username = request.GET.get("username", "")
            dict_name = request.GET.get("dict_name", "")
            if username:
                result = list(learn_models.score.objects.filter(username=username).values())
                return JsonResponse({"result": result})
            elif dict_name:
                result = list(learn_models.score.objects.filter(dict_name=dict_name).values())
                return JsonResponse({"result": result})
            else:
                return JsonResponse({"result": "no params error"})
        except Exception:
            logging.getLogger('app_log').error(traceback.format_exc())
            return JsonResponse({"result": "error"})
