from django.core import serializers

class PageMetaDataResource:
	JSON_TEMLPATE = '{"title" : "%s", "description": "%s", "keyword": "%s", "id": "%s", "url": "%s" }'

	def __init__(self, page):
		self.keyword = page.keyword
		self.description = page.description
		self.title = page.title 
		self.id = page.pk 
		self.url = page.url 

	def asJson(self): 		
		return PageMetaDataResource.JSON_TEMLPATE % (self.title, self.description, self.keyword, self.id, self.url)


class PageMetaDataCollectionResource:
	def __init__(self, pages):
		resources = []
		for page in pages : resources.append(PageMetaDataResource(page))
		self.resources = resources

	def asJson(self): 		
		jsonStr = "["
		for resource in self.resources : jsonStr+=resource.asJson() + " ,"
		return jsonStr[0:-1] + "]"
