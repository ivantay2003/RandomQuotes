import urllib.request

class RandomQuoteGenerator () :

    url = "https://random-quote-generator.herokuapp.com/api/quotes/random";


    def getQuotes(self):
        print ("hello")

    def readURL (self):
        r= urllib.request.urlopen(self.url).read().decode('utf-8')

        return r

