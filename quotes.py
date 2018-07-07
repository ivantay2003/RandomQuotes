

from RetrieveQuotes  import RandomQuoteGenerator
from getjson import JSONData


quotes =  RandomQuoteGenerator ()
r = quotes.readURL()


json = JSONData()
jsonData = json.parse_data(r)

print ("Quote : " + jsonData['quote'])
print ("By : "  + jsonData ['author'])

