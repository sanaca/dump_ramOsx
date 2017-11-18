#! /usr/bin/python
# -*- coding: iso-8859-15 -*-


import sys, os
import time
import os.path
import subprocess
import re
import hashlib
import commands
import json
import time,datetime

def print_red(text):
	print ('\033[22;31m' + text + '\033[0;m')
		
def print_green(text):
	print ('\033[22;32m' + text + '\033[0;m')

def print_log(text):
	print ('\033[5;5m' + text + '\033[1;m')


	
os.system('clear')


def fct_dump_RAM():
	RAM = raw_input("Choisissez un nom pour le dump de la RAM :")
	with open(RAM,"wb") as outfile:
		output = subprocess.Popen(["./osxpmem '%s'" % RAM ], shell=True)

def fct_artefact():
	RAM = raw_input("Choisissez un nom pour le dump de la RAM :")
	fichier = raw_input("Choisissez un nom pour le fichier tar.gz de sortie :")
	with open(RAM,"wb") as outfile:
		output = subprocess.Popen(["./osxpmem '%s'" % RAM ], shell=True)
	with open(fichier,"wb") as ofile:
		output = subprocess.Popen(["/usr/bin/python2.7 osxcollector.py -c -d -l -i '%s'" % fichier ], shell=True)
	sys.exit()
def fct_checksum():
	def md5file(path, blocksize = 65536):
		afile = open(path, 'rb')
		hasher = hashlib.md5()
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)
		afile.close()
		return hasher.hexdigest()
		
	def sha256hash(path, blocksize = 64*1024):
		afile = open(path, 'rb')
		hasher = hashlib.sha256()
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)
		afile.close()
		return hasher.hexdigest()
		
	rootDir = '/'
	fichier = raw_input("Entrez le nom du json en sortie : ")
	for dirName, subdirList, fileList in os.walk(rootDir):
		for fname in fileList:
			path = os.path.join(dirName, fname)
			file_md5 = md5file(path)
			file_sha = sha256hash(path)
			data = ({'chemin': dirName, 'fichier': fname, 'md5': file_md5, 'sha256': file_sha})
			#with open('Checksum.json', 'a') as f:
			with open(fichier, 'a') as f:
				jsonData = json.dumps(data)
				json.dump(jsonData, f)
			print('chemin: %s' % dirName, 'Fichier: %s' % fname, 'md5: %s' % file_md5, 'sha256: %s' % file_sha)
				
				
var_uid = os.geteuid()
if var_uid != 0 : 
	print_red("\nLes privileges root sont requis.\n")
	sys.exit()



var_attack = "null"

while var_attack != "q":                                                             
	print_green("\n                      ====Outil de collect d'artefacts MAC OSX====")
	print_green("========================================================================\n")




	var_version=os.popen('uname -r | cut -d "." -f 1').read().strip("\n")
	if var_version == "10" : 
		print_red("Votre version d'OSX est: Snow Leopard Mac OS X / 10.6")
	elif var_version == "11" : 
		print_red("Votre version d'OSX est: Lion / 10.7")
	elif var_version == "12" : 
		print_red("Votre version d'OSX est: Mountain Lion / 10.8  ")
	elif var_version == "13" : 
		print_red("Votre version d'OSX est: Mavericks / 10.9")
	elif var_version == "14" : 
		print_red("Votre version d'OSX est: Yosemite / 10.10")
	elif var_version == "15" : 
		print_red("Votre version d'OSX est: El Capitan / 10.11")
	elif var_version == "16" : 
		print_red("Votre version d'OSX est: Sierra / 10.12")
	else: 
		print_red("\n\nVersion d'OSX non supporté.\n\n")
		exit()

	print_log("Notez cette date/heure dans votre rapport: " + str(datetime.datetime.now()))
	var_action = "null"
	while var_action == "null":
		print_green("1: Dump DE LA RAM")
		print_green("2: Dump DE LA RAM ET ARTEFACT")
		print_green("3: CheckSum de tous les fichiers presents sur le Disque")
		print_green("q: pour quitter")
		var_action=raw_input("\nVotre choix: > ")

	if var_action == "1": 
		fct_dump_RAM()
		var_action = "null"
	elif var_action == "2":
		fct_artefact() 
		var_action = "null"
	elif var_action == "3":
		fct_checksum() 
		var_action = "null"
	elif var_action == "q": 
		exit()
	else: 
		print_red("\nVeuillez choisir 1, 2, 3 ou q\n")
var_action = "null"












