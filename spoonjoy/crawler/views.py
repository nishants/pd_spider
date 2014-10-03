from django.http import HttpResponse
from django.template import RequestContext, loader
from crawler.models import PageMetaData
from django.http import HttpResponse
from django.core import serializers
from crawler.pageReader import PageReader
from django.core import serializers

import json

from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def pages(request):
	# if(request.method)
    # print(request['REQUEST_METHOD'])
    # return ""
    if request.method == 'POST' :
    	return create(request)
    if request.method == 'GET' :
    	return findOne(request)

def create(request):
	link = json.loads(request.body)['link']

	pageMetaData = PageReader(link).getMetaData()
	# import pdb; pdb.set_trace()

	asJson = serializers.serialize("json", [pageMetaData])
	return HttpResponse(asJson)

def findOne(request):
	return HttpResponse("findOne")
# if request.method == 'GET':
#     	return find(request)
# 	elif request.method == 'POST':
#     	return HttpResponse("create")

# def create(request):
# 	return HttpResponse("create")

# def find(request):
# 	return HttpResponse("find")