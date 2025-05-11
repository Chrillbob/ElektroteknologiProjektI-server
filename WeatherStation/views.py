from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Measurements

import json
import datetime

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['temp', 'humidity', 'wind_speed', 'wind_dir', 'pressure', 'smoke', 'ambient']

# Create your views here.
def index(request):
    if request.method == "POST" and request.content_type == "application/json":
        try:
            body = json.loads(request.body)
            
            for entry in body:
                fields = entry.get("fields", {})
                fields.pop("meas_time", None)
                # Create new Measurements object - meas_time is handled by auto_now_add
                print(fields)
                
                Measurements.objects.create(**fields)
            
            return JsonResponse({"status": "ok"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
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

