from django.http import HttpResponse
from django.template import RequestContext, loader
from crawler.models import PageMetaData
from django.http import HttpResponse
from django.core import serializers
from spider import info_of
from resources import PageMetaDataResource, PageMetaDataCollectionResource
from collections import defaultdict

import json

from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@csrf_exempt
def pages (request) : 
	if(request.method == 'POST'):	
		return create(request)
	return allPages()

def allPages():	
	return HttpResponse(PageMetaDataCollectionResource(PageMetaData.objects.all()).asJson())

def create(request):
	pageMetaData = to_page_data(info_of(url_from(request)))
	pageMetaData.save()
	return HttpResponse(asJson(pageMetaData))

def to_page_data(values) : 	
	values = defaultdict(lambda: None, values)
	return PageMetaData(
		title=values['title'],
		description=values['description'],
		keywords=values['keywords'],
		url=values['url']
	)

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

def asJson(data): 
	return _responseOf(PageMetaDataResource(data).asJson())

def _responseOf(jsonString) : 
	return '{ "data" : ' + jsonString + " }"

def url_from(request): 
	url =  json.loads(request.body)['link']
	if not url.startswith("http://") : url = "http://" + url
	return url
