from lxml import html
import requests
from collections import Counter

# Question - How many Stories Does Charlie Pollard Appear in with the 8th Doctor? And What about the other companion actors?

# Page targets to scrape 
page = requests.get("https://www.bigfinish.com/collections/v/the-eighth-doctor-collection?sort_ordering=date_asc&search_product_type=&search_availability=all")
page2 = requests.get("https://www.bigfinish.com/collections/v/the-eighth-doctor-collection/page:2?url=collections%2Fv%2Fthe-eighth-doctor-collection&sort_ordering=date_asc&search_product_type=&search_availability=all&search_release_date=asc&_=1565593266884")
page3 = requests.get("https://www.bigfinish.com/collections/v/the-eighth-doctor-collection/page:3?url=collections%2Fv%2Fthe-eighth-doctor-collection&sort_ordering=date_asc&search_product_type=&search_availability=all&search_release_date=asc&&_=1565593266884")
page4 = requests.get("https://www.bigfinish.com/collections/v/the-eighth-doctor-collection/page:4?url=collections%2Fv%2Fthe-eighth-doctor-collection&sort_ordering=date_asc&search_product_type=&search_availability=all&search_release_date=asc&&_=1565593266884")
page5 = requests.get("https://www.bigfinish.com/collections/v/the-eighth-doctor-collection/page:5?url=collections%2Fv%2Fthe-eighth-doctor-collection&sort_ordering=date_asc&search_product_type=&search_availability=all&search_release_date=asc&&_=1565593266884")
page6 = requests.get("https://www.bigfinish.com/collections/v/the-eighth-doctor-collection/page:6?url=collections%2Fv%2Fthe-eighth-doctor-collection&sort_ordering=date_asc&search_product_type=&search_availability=all&search_release_date=asc&&_=1565593266885")

# Set up the Tree
tree = html.fromstring(page.content)
tree2 = html.fromstring(page2.content)
tree3 = html.fromstring(page3.content)
tree4 = html.fromstring(page4.content)
tree5 = html.fromstring(page5.content)
tree6 = html.fromstring(page6.content)

# specify the xpath to target on the page
charley1 = tree.xpath('//*[@id="container"]/li[*]/article/figure/figcaption/p/a[2]/text()')
charley2 = tree2.xpath('//*[@id="container"]/li[*]/article/figure/figcaption/p/a[2]/text()')
charley3 = tree3.xpath('//*[@id="container"]/li[*]/article/figure/figcaption/p/a[2]/text()')
charley4 = tree4.xpath('//*[@id="container"]/li[*]/article/figure/figcaption/p/a[2]/text()')
charley5 = tree5.xpath('//*[@id="container"]/li[*]/article/figure/figcaption/p/a[2]/text()')
charley6 = tree6.xpath('//*[@id="container"]/li[*]/article/figure/figcaption/p/a[2]/text()')


#concat the compainions together

charley = charley1+charley2+charley3+charley4+charley5+charley6

# print the list
print(charley)

# count up the number of times India Fisher appears as Charley on the page.
print(Counter(charley))

# List to string
# stringCharley = ''.join(map(str,charley))

# print and strip out newline and tab characters
# print(stringCharley.split("\n\t"))
