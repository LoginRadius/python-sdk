#!/usr/bin/python
#################################################
# Class for Social Authentication               #
#################################################
# This is the main class to communicate with    #
# LogiRadius Unified Social API. It contains    #
# functions for Social Authentication with User #
# Profile Data (Basic and Extended).            #
#################################################
# Copyright 2013 LoginRadius Inc.               #
# - www.LoginRadius.com                         #
#################################################
# This file is part of the LoginRadius SDK      #
# package.                                      #
#################################################

SECURE_API_URL="https://hub.loginradius.com/"
HEADERS={}
HEADERS['User-Agent'] = "LoginRadius - Python - SDK"

class LoginRadius():
	def __init__(self, API_Secret, Token):
		self.api_secret = API_Secret
		self.token = Token
		#We prefer to use requests with the updated urlib3.
		try:
			import requests
			self.library="requests"
			self.requests = requests
			self.urllib2 = False
		
		#However, we can use urllib if there is no requests.
		except:
			import urllib
			import urllib2
			import json
			self.library="urlib2"
			self.urllib2 = urllib2
			self.urllib = urllib
			self.json = json
			self.requests = False
			
	#
	# Read Permissions
	#
	
	def loginradius_get_data(self):
		if self.requests:
			payload = {'apisecrete':self.api_secret, 'token':self.token}
			r = self.requests.get(SECURE_API_URL + "UserProfile.ashx", params=payload, headers=HEADERS)
			return r.json()
		else:
			r = self.urllib2.Request(SECURE_API_URL + "UserProfile.ashx/" + self.api_secret + "/" + self.token)
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)
			
			
	def loginradius_get_contacts(self):
		if self.requests:
			r = self.requests.get(SECURE_API_URL + "contacts/" + self.api_secret + "/" + self.token, headers=HEADERS)
			return r.json()
		else:
			r = self.urllib2.Request(SECURE_API_URL + "contacts/" + self.api_secret + "/" + self.token)
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)
	
	def loginradius_get_groups(self):
		if self.requests:
			r = self.requests.get(SECURE_API_URL + "GetGroups/" + self.api_secret + "/" + self.token, headers=HEADERS)
			return r.json()
		else:
			r = self.urllib2.Request(SECURE_API_URL + "GetGroups/" + self.api_secret + "/" + self.token)
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)

	def loginradius_get_posts(self):
		if self.requests:
			r = self.requests.get(SECURE_API_URL + "GetPosts/" + self.api_secret + "/" + self.token, headers=HEADERS)
			return r.json()		
		
		else:
			r = self.urllib2.Request(SECURE_API_URL + "GetPosts/" + self.api_secret + "/" + self.token)
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)			


	def loginradius_get_events(self):
		if self.requests:
			r = self.requests.get(SECURE_API_URL + "GetEvents/" + self.api_secret + "/" + self.token, headers=HEADERS)
			return r.json()
		
		else:
			r = self.urllib2.Request(SECURE_API_URL + "GetEvents/" + self.api_secret + "/" + self.token)
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)					


	def loginradius_get_mentions(self):
		if self.requests:
			r = self.requests.get(SECURE_API_URL + "status/mentions/" + self.api_secret + "/" + self.token, headers=HEADERS)
			return r.json()	

		else:
			r = self.urllib2.Request(SECURE_API_URL + "status/mentions/" + self.api_secret + "/" + self.token)
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)			

	def loginradius_get_timeline(self):
		if self.requests:
			r = self.requests.get(SECURE_API_URL + "status/timeline/" + self.api_secret + "/" + self.token, headers=HEADERS)
			return r.json()	
			
		else:
			r = self.urllib2.Request(SECURE_API_URL + "status/timeline/" + self.api_secret + "/" + self.token)
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)		

	def loginradius_get_company(self):
		if self.requests:
			r = self.requests.get(SECURE_API_URL + "GetCompany/" + self.api_secret + "/" + self.token, headers=HEADERS)
			return r.json()	
			
		else:
			r = self.urllib2.Request(SECURE_API_URL + "GetCompany/" + self.api_secret + "/" + self.token)
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)		
	#
	#Write Permissions
	#			
	
	def loginradius_status_update(self, status, to=None, title=None, url=None, imageurl=None, caption=None, description=None):
		payload = {'status':status}
		if to is not None:
			payload['to'] = to
		if title is not None:
			payload['title'] = title
		if url is not None:
			payload['url'] = url
		if imageurl is not None:
			payload['imageurl'] = imageurl
		if captions is not None:
			payload['caption'] = caption
		if description is not None:
			payload['description'] = description		
		if self.requests:
			r = self.requests.get(SECURE_API_URL + "status/update/" + self.api_secret + "/" + self.token, params=payload, headers=HEADERS)
			return r.json()

		else:
			payload = urlencode(payload)
			r = self.urllib2.Request(SECURE_API_URL + "status/update/" + self.api_secret + "/" + self.token, payload, {'Content-Type': 'application/json'})
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)		
			
	def loginradius_direct_message(self, to, subject, message):
		payload = {'to': to, 'subject': subject, 'message':message}
		if self.requests:
			r = self.requests.get(SECURE_API_URL + "directmessage/" + self.api_secret + "/" + self.token, headers=HEADERS)
			return r.json()
		
		else:
			payload = json.dumps(payload)
			r = self.urllib2.Request(SECURE_API_URL + "directmessage/" + self.api_secret + "/" + self.token, payload, {'Content-Type': 'application/json'})
			r.add_header('User-Agent', HEADERS['User-Agent'])
			try:
				data = self.urllib2.urlopen(r)
			except self.urllib2.HTTPError, error:
				return error.read()
			return self.json.load(data)		
			
			



			
		