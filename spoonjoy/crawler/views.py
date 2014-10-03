from django.http import HttpResponse
from django.template import RequestContext, loader
from crawler.models import PageMetaData
from django.http import HttpResponse
from django.core import serializers
from crawler.pageReader import PageReader
from resources import PageMetaDataResource, PageMetaDataCollectionResource

import json

from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@csrf_exempt
def pages (request) : 
	# import pdb; pdb.set_trace()
	if(request.method == 'POST'):	
		return create(request)
	return allPages()

def allPages():	
	return HttpResponse(PageMetaDataCollectionResource(PageMetaData.objects.all()).asJson())

def create(request):
	pageMetaData = PageReader(urlFrom(request)).getMetaData()
	pageMetaData.save()
	return HttpResponse(asJson(pageMetaData))

@csrf_exempt
def page(request, page_id): 
	if(request.method == 'GET'):
		return getPage(request, page_id)
	return update(request, page_id)

def getPage(request, page_id):
	return HttpResponse(asJson(PageMetaData.objects.get(pk=page_id)))

def update(request, page_id):
	params = json.loads(request.body)
	page = PageMetaData.objects.get(pk=page_id)
	page.description = params['description']
	page.keywords = params['keywords']
	page.title = params['title']
	page.save()
	return HttpResponse(asJson(page))

def asJson(pageMetadata): 
	return _responseOf(PageMetaDataResource(pageMetadata).asJson())

def _responseOf(jsonString) : 
	return '{ "data" : ' + jsonString + " }"

def urlFrom(request): 
	return json.loads(request.body)['link']
