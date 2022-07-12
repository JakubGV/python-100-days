from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

article_tags = soup.find_all(name='a', class_='titlelink')
article_texts = []
article_links = []
for tag in article_tags:
    text = tag.getText()
    link = tag.get('href')
    article_texts.append(text)
    article_links.append(link)
    
article_upvotes = [int(tag.getText().split(' ')[0]) for tag in soup.find_all(name='span', class_='score')]

largest_score = max(article_upvotes)
largest_index = article_upvotes.index(largest_score)

print(article_texts[largest_index])
print(article_links[largest_index])