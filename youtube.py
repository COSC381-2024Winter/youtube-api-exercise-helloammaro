import sys
import config
from googleapiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = config.API_KEY

def youtube_search(query_term, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=query_term,
        part="id,snippet",
        maxResults=max_results
    ).execute()
    return search_response

if __name__ == "__main__":
    query_term = sys.argv[1]
    max_results = sys.argv[2]
    response = youtube_search(query_term, max_results)
    print(response)
