#!/usr/bin/python

import os
import hashlib
import csv
import json


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
for dirName, subdirList, fileList in os.walk(rootDir):
	for fname in fileList:
		path = os.path.join(dirName, fname)
		file_md5 = md5file(path)
		file_sha = sha256hash(path)
		data = ({'chemin': dirName, 'fichier': fname, 'md5': file_md5, 'sha256': file_sha})
		with open('Checksum.json', 'a') as f:
			jsonData = json.dumps(data)
			json.dump(jsonData, f)

		print('chemin: %s' % dirName, 'Fichier: %s' % fname, 'md5: %s' % file_md5, 'sha256: %s' % file_sha)
		
		with open('checksum.csv', 'a') as csvfile:
			fieldnames = ['chemin','fichier', 'md5', 'sha256']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({'chemin': dirName, 'fichier':fname, 'md5': file_md5, 'sha256': file_sha})
			
			
