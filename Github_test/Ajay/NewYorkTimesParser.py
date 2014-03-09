#Code Author	: Ajay Nair
#Code Reviewer	:
#Last Modified	: 03/08/2014 by Ajay Nair

from bs4 import BeautifulSoup
import urllib2
import sys

class NewYorkTimesParser:
	def __init__(self):
		pass
	def getArticleTitle(self,parser):
		try:
			title = parser.find("h1",{"class":"story-heading"}).text
			title = title.encode("ascii","ignore")
		except:
			title = ""
		return title
	
	def getArticleContent(self,parser):
		content = ""
		try:
			allBody = parser.findAll("p",{"class":"story-body-text story-content"})	
			for para in allBody:
				content += para.text
			content = content.encode("ascii","ignore")
		except:
			content = ""

		return content 

	def getArticleImages(self,parser):
		try:
			imgList = map(lambda x:x.get('src'),parser.findAll("img",{"class":"media-viewer-candidate"}))
		except:
			imgList = []
		return imgList

	def parse(self, source, inputText):
        	self.parser = BeautifulSoup(inputText)
		print self.getArticleTitle(self.parser)
		print self.getArticleContent(self.parser)
		print self.getArticleImages(self.parser)
		

if __name__ == '__main__':
	newYorkTimesParser = NewYorkTimesParser()
	#url = 'http://www.nytimes.com/2014/03/08/your-money/when-working-in-your-pajamas-is-more-productive.html'
	url = sys.argv[1]
	#handle = open("temp/new1.html")
	#Comment - make an url opener that can handle cookies required for New York Times, not necessary for others
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	handle = opener.open(url)
	data = handle.read()
	newYorkTimesParser.parse('New York Times',data)
	handle.close()
