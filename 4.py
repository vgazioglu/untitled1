from lxml import html, etree
import requests


#page = requests.get("http://www.howtowebscrape.com/examples/simplescrape1.html")

page = requests.get("https://www.tff.org/Default.aspx?pageId=28&kulupId=4710")


print(page.content)

#extractedHtml = html.fromstring(page.content)
#bookTitle = extractedHtml.xpath("/html/body/div[1]/div[4]/div/div/div/table/tbody/tr[1]/td[4]")
#print(bookTitle[0].text)
#bookTitle = extractedHtml.xpath("/html/body/div[1]/div[4]/div/div/div/table/tbody/tr[2]/td[4]")
#print(bookTitle[0].text)