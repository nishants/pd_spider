from django.core import serializers

class PageMetaDataResource:
	JSON_TEMLPATE = '{"title" : "%s", "description": "%s", "keyword": "%s", "id": "%s" }'

	def __init__(self, page):
		self.keyword = page.keyword
		self.description = page.description
		self.title = page.title 
		self.id = page.pk 

	def asJson(self): 		
		return PageMetaDataResource.JSON_TEMLPATE % (self.title, self.description, self.keyword, self.id)
