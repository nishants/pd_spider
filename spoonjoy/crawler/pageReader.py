from crawler.models import PageMetaData
import urllib2
import re

class PageReader:
	def __init__(self, url):
		self.pageUrl = url

	def getMetaData(self):
		metaTags = getMetaInfo(self.pageUrl)

		return PageMetaData(
			title=_keyOrNone(metaTags, 'pageTitle'), 
			description=_keyOrNone(metaTags,'description'), 
			keywords=_keyOrNone(metaTags,'keywords'),
			url=self.pageUrl
			)

def _keyOrNone(dict, key):
	return dict[key] if dict.has_key(key) else ''

def getMetaInfo(url) : 
	page = urllib2.urlopen(url)
	metaTags = {}	
	for line in page : _merge(metaTags, __metaInfoFrom(line))
	return metaTags

def _merge(dictOne, dictTwo):
	if dictTwo and (len(dictTwo.keys()) != 0) : 		
		for key in dictTwo: dictOne[key] = dictTwo[key]


def __pageTitle(htmlStr) : 
	titleTag = "<\\s*title.*>"
	titleValue = ">.*<\\s*/\\s*title\\s*>"
	matches = re.findall(titleTag, htmlStr)
	if(len(matches) != 0 ) : 
		return re.split("<\\s*/\\s*title\\s*>", re.findall(titleValue, matches[0])[0])		 
	return None

def __metaInfoFrom(htmlStr) : 
	result = {}
	htmlStr = htmlStr.lower().replace("\'", "\"")
	metaTag = "<\\s*meta.*>"
	propertyName = "name\\s*=\\s*\"[^\"]+\""
	propertyValue = "content\\s*=\\s*\"[^\"]+\""
	matches = re.findall(metaTag, htmlStr)
	pageTitle = __pageTitle(htmlStr)
	if pageTitle : result['pageTitle'] =  pageTitle

	if(len(matches) == 0 ) : return result
	for match in matches : 
		nameAttrib = re.findall(propertyName, match)
		contenAttrib = re.findall(propertyValue, match)
		if len(nameAttrib) > 0 : 
			key = nameAttrib[0].split("=")[1].replace('"', "")
			value = contenAttrib[0].split("=")[1].replace('"', "") if len(contenAttrib) > 0 else ''
			result[key] = value

	return result





