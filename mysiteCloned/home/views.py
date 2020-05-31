from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core import serializers

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
import json 

from .models import AppChoose


def home(request):
    # choices = AppChoose.objects.all()
    # ret = serializers.serialize('json', choices)
    # return HttpResponse(ret, content_type='application/json')

    # data = list(AppChoose.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
    # return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})

    choices = get_list_or_404(AppChoose) 
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx", choices)
    return render(request, 'home/home.html', {'choices':choices})



# def some_view(request):
#     qs = SomeModel.objects.all()
#     qs_json = serializers.serialize('json', qs)
#     return HttpResponse(qs_json, content_type='application/json')