import requests
from bs4 import BeautifulSoup

def scrape_google(query):
    url = f'https://www.google.com/search?q={query}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())
    results = []
    for result in soup.find_all('div', class_='g'):
        title = result.find('h3').text
        link = result.find('a')['href']
        snippet = result.find('span', class_='st').text
        results.append({'title': title, 'link': link, 'snippet': snippet})
    return results

if __name__ == '__main__':
    query = input('Enter your search query: ')
    results = scrape_google(query)
    print(results)
    for result in results:
        print(result)
        #needs further extraction
