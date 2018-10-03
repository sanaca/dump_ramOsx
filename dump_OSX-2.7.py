#! /usr/bin/python
# -*- coding: iso-8859-15 -*-


from __future__ import with_statement
from __future__ import absolute_import
import sys, os
import time
import os.path
import subprocess
import re
import hashlib
import commands
import json
import time,datetime
import shutil
from io import open

def print_red(text):
	print u'\033[22;31m' + text + u'\033[0;m'
		
def print_green(text):
	print u'\033[22;32m' + text + u'\033[0;m'

def print_log(text):
	print u'\033[5;5m' + text + u'\033[1;m'


	
os.system(u'clear')


def fct_dump_RAM():
	RAM = raw_input(u"Choisissez un nom pour le dump de la RAM :")
	volumes = os.popen(u"ls /Volumes").read()
	print volumes
	locate = raw_input(u"Dans quel volume voulez-vous le copier?")
	with open(RAM,u"wb") as outfile:
		shutil.copyfile(u'osxpmem', u'/tmp/osxpmem')
		shutil.copytree(u'pmem.kext', u'/tmp/pmem.kext')
		output = subprocess.Popen([u"cd /tmp && chmod +x pmem.kext osxpmem && ./osxpmem --format raw /Volumes/'%s'/'%s'" % (locate, RAM) ], shell=True)
		var_action = u"null"
		sys.exit()

def fct_artefact():
	RAM = raw_input(u"Choisissez un nom pour le dump de la RAM :")
	volumes = os.popen(u"ls /Volumes").read()
	print volumes
	locate = raw_input(u"Dans quel volume voulez-vous le copier?")
	fichier = raw_input(u"Choisissez un nom pour le fichier tar.gz de sortie :")
	with open(RAM,u"wb") as outfile:
		shutil.copyfile(u'osxpmem', u'/tmp/osxpmem')
		shutil.copytree(u'pmem.kext', u'/tmp/pmem.kext')
		output = subprocess.Popen([u"cd /tmp && chmod +x pmem.kext osxpmem && ./osxpmem --format raw /Volumes/'%s'/'%s'" % (locate, RAM) ], shell=True)
	with open(fichier,u"wb") as ofile:
		output = subprocess.Popen([u"/usr/bin/python2.7 outils/osxcollector.py -c -d -l -i '%s'" % fichier ], shell=True)
	sys.exit()
def fct_checksum():
	def md5file(path, blocksize = 65536):
		afile = open(path, u'rb')
		hasher = hashlib.md5()
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)
		afile.close()
		return hasher.hexdigest()
		
	def sha256hash(path, blocksize = 64*1024):
		afile = open(path, u'rb')
		hasher = hashlib.sha256()
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)
		afile.close()
		return hasher.hexdigest()
		
	rootDir = u'/'
	fichier = raw_input(u"Entrez le nom du json en sortie : ")
	for dirName, subdirList, fileList in os.walk(rootDir):
		for fname in fileList:
			path = os.path.join(dirName, fname)
			file_md5 = md5file(path)
			file_sha = sha256hash(path)
			data = ({u'chemin': dirName, u'fichier': fname, u'md5': file_md5, u'sha256': file_sha})
			with open(fichier, u'a') as f:
				jsonData = json.dumps(data)
				json.dump(jsonData, f)
			print u'chemin: %s' % dirName, u'Fichier: %s' % fname, u'md5: %s' % file_md5, u'sha256: %s' % file_sha
				
				
var_uid = os.geteuid()
if var_uid != 0 : 
	print_red(u"\nLes privileges root sont requis.\n")
	sys.exit()



var_attack = u"null"

while var_attack != u"q":                                                             
	print_green(u"\n                      ====Outil de collect d'artefacts MAC OSX====")
	print_green(u"========================================================================\n")




	var_version=os.popen(u'uname -r | cut -d "." -f 1').read().strip(u"\n")
	if var_version == u"10" : 
		print_red(u"Votre version d'OSX est: Snow Leopard Mac OS X / 10.6")
	elif var_version == u"11" : 
		print_red(u"Votre version d'OSX est: Lion / 10.7")
	elif var_version == u"12" : 
		print_red(u"Votre version d'OSX est: Mountain Lion / 10.8  ")
	elif var_version == u"13" : 
		print_red(u"Votre version d'OSX est: Mavericks / 10.9")
	elif var_version == u"14" : 
		print_red(u"Votre version d'OSX est: Yosemite / 10.10")
	elif var_version == u"15" : 
		print_red(u"Votre version d'OSX est: El Capitan / 10.11")
	elif var_version == u"16" : 
		print_red(u"Votre version d'OSX est: Sierra / 10.12")
	elif var_version == u"17" : 
		print_red(u"Votre version d'OSX est: High Sierra / 10.13")
	elif var_version == u"18" : 
		print_red(u"Votre version d'OSX est: Mojave / 10.14")
	else: 
		print_red(u"\n\nVersion d'OSX non supporté.\n\n")
		exit()

	print_log(u"Notez cette date/heure dans votre rapport: " + unicode(datetime.datetime.now()))
	var_action = u"null"
	while var_action == u"null":
		print_green(u"1: Dump DE LA RAM")
		print_green(u"2: Dump DE LA RAM ET ARTEFACT")
		print_green(u"3: CheckSum de tous les fichiers presents sur le Disque")
		print_green(u"q: pour quitter")
		var_action=raw_input(u"\nVotre choix: > ")

	if var_action == u"1": 
		fct_dump_RAM()
		var_action = u"null"
	elif var_action == u"2":
		fct_artefact() 
		var_action = u"null"
	elif var_action == u"3":
		fct_checksum() 
		var_action = u"null"
	elif var_action == u"q": 
		exit()
	else: 
		print_red(u"\nVeuillez choisir 1, 2, 3 ou q\n")
var_action = u"null"
