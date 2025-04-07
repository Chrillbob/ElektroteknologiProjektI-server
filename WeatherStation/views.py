from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Measurements

import datetime


# Create your views here.
def index(request):
    if request.method == "POST" and request.content_type == "application/json":
        data = request.POST
        print(request.body)
        for deserialized_object in serializers.deserialize("json", request.body):
            deserialized_object.save()
        response = HttpResponse()
        response.status_code = 200
        return HttpResponse("")
    else:
        return HttpResponse("Hello, world. You're at the WeatherStation index.")

def measurement(request, meas_id):
#   return HttpResponse("You requested measurement %s." %meas_id)

    json = serializers.serialize("json", Measurements.objects.filter(pk=meas_id))
    return JsonResponse(json, safe=False)

def latest(request):
    json = serializers.serialize("json", [Measurements.objects.latest("meas_time")])
    return JsonResponse(json, safe=False)

def lastday(request):
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)

    data = Measurements.objects.filter(meas_time__gte=yesterday)
    json = serializers.serialize("json", data)
    return JsonResponse(json, safe=False)

