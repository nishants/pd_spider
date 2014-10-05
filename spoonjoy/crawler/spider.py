from crawler.models import PageMetaData
import urllib2
import re
import HTMLParser
from collections import defaultdict

def info_of(url) : 
	page = urllib2.urlopen(url)
	page_info = Crawler().parse(page.read())
	page_info["url"]  = url
	return to_all_keys_lower(page_info) 

def to_all_keys_lower(info):
	all_keys_lower = {}
	for key in info : all_keys_lower[key.lower()] = info[key]
	return all_keys_lower

def action_for(tag): 
	tag_actions = {
		"title" : getTitleInfo,
		"meta"  : getMetaTag,
		"others": no_action, 
	}
	return tag_actions[name_of(tag)]

def name_of(tag):
	names = {
		"title" : "title",
		"meta"  : "meta",
		"others":  "others"
	}
	return names[tag] if tag in names else names["others"]


def no_action(data, attrs) : 
	return "", None

def getTitleInfo(data, attrs) : 
	return "title", data

def getMetaTag(data, attrs):
	if('name' not in attrs or 'content' not in attrs ): return "",""
	return attrs['name'], attrs['content'] 

class Crawler(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.info = {}
		self.last_data = None
		self.flushed = True

	def handle_starttag(self, tag, attrs):
		self.flush()
		self.flushed = False
		self.last_attrs = dict(attrs)
		self.last_tag = tag

	def handle_endtag(self, tag):		
		self.flush()

	def handle_data(self, data):
		self.last_data = data

	def parse(self, htmlStr):
		self.feed(htmlStr)
		return self.info

	def flush(self):
		if self.flushed : return 
		info_key, info_value = action_for(self.last_tag)(self.last_data, self.last_attrs)
		self.info[info_key] = info_value
		self.flushed = True
