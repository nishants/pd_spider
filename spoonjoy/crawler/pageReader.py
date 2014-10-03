from crawler.models import PageMetaData

class PageReader:
	def __init__(self, url):
		self.pageUrl = url

	def getMetaData(self):
		return PageMetaData(
			title="flipkart.com", 
			description="A shopping website", 
			keywords="shopping, online, india",
			url=self.pageUrl
			)