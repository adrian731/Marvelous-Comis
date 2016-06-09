#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, default_app, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
import urllib2
import requests
import json
import time
from HTMLParser import HTMLParser
from urlparse import parse_qs
import os

@get('/')	
def home_page():
	return template('index.tpl')
	
@get('/busqueda1')
def busqueda1():
	return template('busqueda1.tpl')
	
@get('/busqueda2')
def busqueda2():
	return template('busqueda2.tpl')

@post('/resultado1')
def busqueda1():
	url_base='http://gateway.marvel.com/'
	name=request.forms.get('name')
	payload = {'apikey':'fcd7230a0d69643d5bd4110504babd72','hash':'fe261e6ba1072612497588694d4e2738','ts':'1'}
	payload['name']=name
	r=requests.get(url_base+'v1/public/characters',params=payload)
	if r.status_code == 200:
		js=json.loads(r.text)
		idchar=js["data"]["results"][0]["id"]
		total=js["data"]["results"][0]["comics"]["available"]
		print idchar, total
	else: 
		print "No existe ningún personaje con ese nombre"

	payload2 = {'apikey':'fcd7230a0d69643d5bd4110504babd72','hash':'fe261e6ba1072612497588694d4e2738','ts':'1'}
	payload2['characters']=idchar 
	payload2['limit']="100"
	r=requests.get(url_base+'v1/public/comics',params=payload)
	limit=100
	varoffset=0
	idcomics=[]
	urlcomics=[]
	imgcomics=[]
	final={}
	cantidad=(total//100)+2
	for i in xrange(1,cantidad):
		payload2['offset']=str(varoffset)
		r=requests.get(url_base+'v1/public/comics',params=payload2)
		if r.status_code == 200:
			print r.url
			js=json.loads(r.text)
			for c in js["data"]["results"]:
				idcomic=c["id"]
				url=c["name"]
				img=c["thumbnail"]["path"]+"/portrait_xlarge.jpg"
				idcomics.append(idcomic)
				urlcomics.append(url)
				imgcomics.append(img)
		varoffset=varoffset+100
	
	return template('resultado1.tpl',url=urlcomics,img=imgcomics,idcomic=idcomics)
	
"""@post('/resultado2')
def busqueda2():
	url_base='http://gateway.marvel.com/'
	name=request.forms.get('name')
	payload = {'apikey':'fcd7230a0d69643d5bd4110504babd72','hash':'fe261e6ba1072612497588694d4e2738','ts':'1'}
	payload['name']=name
	r=requests.get(url_base+'v1/public/characters',params=payload)
	if r.status_code == 200:
		js=json.loads(r.text)
		idchar=js["data"]["results"][0]["id"]
		total=js["data"]["results"][0]["comics"]["available"]
		print idchar, total
	else: 
		print "No existe ningún personaje con ese nombre"

	payload2 = {'apikey':'fcd7230a0d69643d5bd4110504babd72','hash':'fe261e6ba1072612497588694d4e2738','ts':'1'}
	payload2['characters']=idchar 
	payload2['limit']="100"
	r=requests.get(url_base+'v1/public/comics',params=payload)
	limit=100
	varoffset=0
	idcomics=[]
	urlcomics=[]
	imgcomics=[]
	final={}
	cantidad=(total//100)+2
	for i in xrange(1,cantidad):
		payload2['offset']=str(varoffset)
		r=requests.get(url_base+'v1/public/comics',params=payload2)
		if r.status_code == 200:
			print r.url
			js=json.loads(r.text)
			for c in js["data"]["results"]:
				idcomic=c["id"]
				title=c["name"]
				img=c["thumbnail"]["path"]+"/portrait_xlarge.jpg"
				idcomics.append(idcomic)
				urlcomics.append(url)
				imgcomics.append(img)
		varoffset=varoffset+100
	
    """Character 2"""
payload = {'apikey':'fcd7230a0d69643d5bd4110504babd72','hash':'fe261e6ba1072612497588694d4e2738','ts':'1'}
payload['name2']=busqueda2
r=requests.get(url_base+'v1/public/characters',params=payload)
if r.status_code == 200:
	js=json.loads(r.text)
	idchar=js["data"]["results"][0]["id"]
	total=js["data"]["results"][0]["comics"]["available"]
	print idchar, total
else: 
	print "No existe ningún personaje con ese nombre"

payload2 = {'apikey':'fcd7230a0d69643d5bd4110504babd72','hash':'fe261e6ba1072612497588694d4e2738','ts':'1'}
payload2['characters']=idchar 
payload2['limit']="100"
r=requests.get(url_base+'v1/public/comics',params=payload)


limit=100
varoffset=0
idcomics2=[]
urlcomics2=[]
imgcomics2=[]
cantidad=(total//100)+2
for i in xrange(1,cantidad):
	payload2['offset']=str(varoffset)
	r=requests.get(url_base+'v1/public/comics',params=payload2)
	if r.status_code == 200:
		print r.url
		js=json.loads(r.text)
		for c in js["data"]["results"]:
			idcomic=c["id"]
			title=c["name"]
			img=c["thumbnail"]["path"]+".jpg"
			idcomics2.append(idcomic)
			urlcomics2.append(url)
			imgcomics2.append(img)
	varoffset=varoffset+100
#for n, u, m in zip(idcomics,urlcomics,imgcomics):
#	print n,"\n"+ u, "\n"+ m
idcomicsf=[]
urlcomicsf=[]
imgcomicsf=[]
for i1,u,m in zip(idcomics,urlcomics,imgcomics):
	if i1 in idcomics2:
		idcomicsf.append(i1)
		urlcomicsf.append(u)
		imgcomics.append(m)
	return template('resultado2.tpl',img=imgcomicsf,idcomic=idcomics)
	for k,l,m in zip(idcomicsf,urlcomicsf,imgcomics):
	print k,"\n"+ l, "\n"+ m"""

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')
	
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'],'wsgi/view/'))

application=default_app()
