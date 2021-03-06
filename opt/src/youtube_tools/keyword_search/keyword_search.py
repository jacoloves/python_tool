#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "APIKey"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        # q=options.q,
        channelId=options.channel_id,
        part="id,snippet",
        maxResults=options.max_results,
        publishedAfter='2019-08-11T00:00:00Z',
        order='date',
    ).execute()

    print(search_response)

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s" % search_result["snippet"]["title"])

    for data in videos:
        print(data)


if __name__ == "__main__":
    # 検索パラメータ
    argparser.add_argument("--q", help="Search term", default="月ノ美兎")
    # channelIDパラメータ
    argparser.add_argument("--channel-id", help="Channel ID", default="UCCzUftO8KOVkV4wQG1vkUvg")
    # max_resultsパラメータ
    argparser.add_argument("--max-results", help="Max results", default=25)
    args = argparser.parse_args()

    try:
        youtube_search(args)
    except HttpError as e:
        print("An HTTP error %d occurred:¥n%s" % (e.resp.status, e.content))