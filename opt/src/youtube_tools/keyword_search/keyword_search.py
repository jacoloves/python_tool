#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "APIKey"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerkey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))

    print("Videos:¥n", "¥n".join(videos), "¥n")


if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="Google")
    argparser.add_argument("--max-result", help="Max results", default=25)
    args = argparser.parse_args()

    print(args)

    try:
        youtube_search(args)
    except HttpError as e:
        print("An HTTP error %d occurred:¥n%s" % (e.resp.status, e.content))