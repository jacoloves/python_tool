#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import webbrowser
from color import test_color
import pandas as pd
import iosparser



DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def developerkey_set():

    global DEVELOPER_KEY

    f = open('apikey.txt', 'r', encoding='UTF-8')

    while True:
        DEVELOPER_KEY = f.readline()
        break


def video_duration_search(videoid):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    video_list_res = youtube.videos().list(
        part="contentDetails",
        id=videoid
    ).execute()

    videos_duraition = ""

    for video_result in video_list_res.get("items", []):
        videos_duraition = video_result['contentDetails']['duration']

    videotime = iosparser.iosParser.iso_parser(videos_duraition)
    return videotime

def youtube_search(options):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results,
        type="video",
        videoDuration="long",
    ).execute()

    videos_ids = []
    videos_titles = []
    videos_url = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos_titles.append("%s" % search_result["snippet"]["title"])
            videos_url.append("https://www.youtube.com/watch?v=%s" % search_result["id"]["videoId"])
            videos_ids.append("%s" % search_result["id"]["videoId"])

    videotime_arr = []
    for videoid in videos_ids:
        videotime = video_duration_search(videoid)
        videotime_arr.append(videotime)

    df = pd.DataFrame(index=[], columns=[])

    df["title"] = videos_titles
    df["url"] = videos_url
    df["video_time"] = videotime_arr

    print(test_color.Color.GREEN + "♫ Let's Play CITYPOP ♫" + test_color.Color.END)
    for title, url, video_time in zip(df['title'], df['url'], df['video_time']):
        print(test_color.Color.PURPLE + "Now Playing is ♫♫" + test_color.Color.END)
        print(test_color.Color.PURPLE + ("[%s] %s" % (title, video_time)) + test_color.Color.END)
        webbrowser.open(url, new=1)
        print(test_color.Color.RED + ("Press enter to listen to the next song!") + test_color.Color.END)
        get_key = input()

    print(test_color.Color.BLUE + ("Finished! See you later Zzz...") + test_color.Color.END)

if __name__ == "__main__":

    developerkey_set()

    # 検索パラメータ
    argparser.add_argument("--q", help="Search term", default="CITYPOP")
    # max_resultsパラメータ
    argparser.add_argument("--max-results", help="Max results", default=30)
    args = argparser.parse_args()

    try:
        youtube_search(args)
    except HttpError as e:
        print("An HTTP error %d occurred:¥n%s" % (e.resp.status, e.content))