# -*- coding: utf-8 -*-
# @Author: @amarlearning
# @Date:   2017-01-15
# @Email:  amar.om1994@gmail.com  
# MIT License. You can find a copy of the License
# @http://amarlearning.mit-license.org

import os, re
import sys, string
import json
import urllib2
from pprint import pprint

class GithubSectory():
	""" docstring for GithubSectory : Python script to download Github Project Subdirectory! """
	

	def __init__(self):
		self.arg = sys.argv
		self.link = ""
		self.ghapi = "https://api.github.com/repos/"
		self.gh = "https://github.com/"

	def getSysArguments(self):

		""" Lets see what kind of input user has given to us """
		
		try:
			self.link = sys.argv[1]
		except Exception as e:
			print "Error : Not argument. Truncating process!"
			sys.exit(0)
		
		if not re.search(r'github.com', self.link):	
			
			for index, arg in enumerate(self.arg):
				if arg == "-r":
					self.repo = self.arg[index+1]
				if arg == "-d":
					self.dir = self.arg[index+1]
				if arg == "-b":
					self.branch = self.arg[index+1]

			try:
				self.link = self.ghapi + sys.argv[1]
			except Exception as e:
				print "Error : User/Organisation not mentioned. Truncating process!"
				sys.exit(0)

			try:
				self.link = self.link + "/" + self.repo
			except Exception as e:
				print "Error : Repository not mentioned. Truncating process!"
				sys.exit(0)

			try:
				self.link = self.link + "/contents/" + self.dir
				try:
					self.link = self.link + "?ref=" + self.branch
					self.downloadMe(self.link)
				except AttributeError:
					self.downloadMe(self.link)
			except AttributeError:
				self.link = self.gh + sys.argv[1] + "/" + self.repo + ".git"
				self.downloadMe(self.link)
		
		else:
			self.link = self.link.replace(self.gh, self.ghapi)
			self.link = self.link.replace('tree', 'contents')
			self.linkList = self.link.split("/")
			self.repo = self.linkList[5]
			self.link = self.link.replace(self.linkList[7]+"/", '')
			self.link = self.link + "/?ref=" + self.linkList[7]
			self.downloadMe(self.link)



	def downloadMe(self, parameter):

		""" Method to download file, link is passed via parameter """

		self.downloadLink = parameter
		self.parsed = json.loads(urllib2.urlopen(self.downloadLink).read())
		if not os.path.exists(self.repo):
			os.makedirs(self.repo)
		self.tempPath = os.path.join(os.getcwd(), self.repo)
		self.workingRecursively(self.tempPath, self.parsed)


	def workingRecursively(self, filepath, filedata):
		
		""" Get the List of all filenames and link of required subdirectory """

		for file in filedata:
			if file['type'] == "file":
				file = open(os.path.join(filepath, file['name']),'a+')
				file.close()	


if __name__ == '__main__':
	GithubSectory().getSysArguments()

# Pattern #1 : main.py https://github.com/GoogleChrome/samples/tree/gh-pages/push-messaging-and-notifications
# Pattern #2 : main.py GoogleChrome -r samples -d push-messaging-and-notifications -b gh-pages