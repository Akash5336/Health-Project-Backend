import bs4
import requests

text = "geeksforgeeks"

url = "https://google.com/search?q=" + text

request_result = requests.get(url)

soup = bs4.BeautifulSoup(request_result.text, "html.parser")

# print(soup)


heading_object = soup.find_all('div')

for info in heading_object:
    print(info.getText())
    print('-----------')












































