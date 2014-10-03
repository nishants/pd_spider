from django.http import HttpResponse
from django.template import RequestContext, loader
from crawler.models import PageMetaData
from django.http import HttpResponse
from django.core import serializers
from crawler.pageReader import PageReader

import json

from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def pages(request):
    if request.method == 'POST' :
    	return create(request)

def create(request):
	link = json.loads(request.body)['link']
	pageMetaData = PageReader(link).getMetaData()
	pageMetaData.save()
	asJson = serializers.serialize("json", [pageMetaData])
	return HttpResponse(asJson)

def getPage(request, page_id):
	page = PageMetaData.objects.get(pk=page_id)
	return HttpResponse(asJson(page))

def asJson(obj): 
	return serializers.serialize("json", [obj])	

