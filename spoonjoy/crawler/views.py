from django.http import HttpResponse
from django.template import RequestContext, loader
from crawler.models import PageMetaData
from django.http import HttpResponse
from django.core import serializers
from crawler.pageReader import PageReader
from resources import PageMetaDataResource

import json

from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@csrf_exempt
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
	# import pdb; pdb.set_trace()
	params = json.loads(request.body)
	page = PageMetaData.objects.get(pk=page_id)
	page.description = params['description']
	page.keyword = params['keyword']
	page.title = params['title']
	page.save()
	return HttpResponse(asJson(page))

def asJson(pageMetadata): 
	return PageMetaDataResource(pageMetadata).asJson()

def urlFrom(request): 
	return json.loads(request.body)['link']
