# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
import traceback

import requests
import logging
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from googletrans import Translator


@method_decorator(csrf_exempt, name="dispatch")
class trans_api(View):

    def post(self, request):
        try:
            data = json.loads(request.body)
            text = data["text"]
            dest = data["dest"]
            translator = Translator()
            result = translator.translate(text, dest=dest).text
            return HttpResponse(result)
        except Exception:
            logging.getLogger('app_log').error(traceback.format_exc())
