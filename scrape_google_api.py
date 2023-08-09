from googleapiclient.discovery import build

def search_google(api_key, cse_id, query):
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=query, cx=cse_id).execute()
    return result['items']

if __name__ == '__main__':
    api_key = 'API_KEY'
    cse_id = 'SEARCH_ENGINE_ID'
    query = 'Chocolate Chip Cookie Recipe'
    results = search_google(api_key, cse_id, query)
    for result in results:
        print(result['title'])
        print(result['link'])
        print(result['snippet'])
        print()
    print(results[0])
