from crawler.models import PageMetaData
import urllib2
import re
import HTMLParser
from collections import defaultdict

def info_of(url) : 
	page = urllib2.urlopen(url)
	page_info = Crawler().parse(page.read())
	page_info["url"]  = url
	return page_info

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
	return "keywords", "some-meta-value"


class Crawler(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.info = {}
		self.last_data = None
		print("creating new")

	def handle_starttag(self, tag, attrs):
		self.last_attrs = attrs

	def handle_endtag(self, tag):
		print "Encountered the end of a %s tag" % tag
		self._process_tag(action_for(tag), self.last_data, self.last_attrs)

	def handle_data(self, data):
		print("Encountered data %s" % data)
		self.last_data = data

	def parse(self, htmlStr):
		self.feed(htmlStr)
		return self.info

	def _process_tag(self, action, data, attrs):
		info_key, info_value = action(data, attrs)
		self.info[info_key] = info_value