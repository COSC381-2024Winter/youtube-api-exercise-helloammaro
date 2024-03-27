import sys
import config
from googleapiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = config.API_KEY

def youtube_search(query_term, max_results):
    print(f"Searching for '{query_term}' with maximum results of {max_results}")
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=query_term,
        part="id,snippet",
        maxResults=max_results,
        type="video"
    ).execute()
    
    search_list = []
    for item in search_response['items']:
        search_list.append(item)
        
    if len(search_list) == 0:
        print("No results")
    elif len(search_list) < int(max_results):
        print("No more results")
        
    return search_list

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python youtube.py [query_term] [max_results]")
        sys.exit(1)
    
    query_term = sys.argv[1]
    max_results = sys.argv[2]
    
    video_list = youtube_search(query_term, max_results)
    
    if len(video_list) != 0:
        print(video_list)
