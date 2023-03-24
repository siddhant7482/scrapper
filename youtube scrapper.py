'''
@author: Yathansh Nagar
'''

import os
import openpyxl
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


api_key = "AIzaSyDUV3SI1qvvoSiX2_uN5ISpj58zbIpcxPw" #FunFluential
#api_key = "AIzaSyBL_Zd218ZvalHi-1BM_6_5uNnBmEiAjMA" #yathanshnaagar    
#api_key = "AIzaSyCSba1fh3nJ5QYd8qqmk6sIPri95_Aj7Ho" #yathanshdhingra
#api_key = "AIzaSyAMysrZh7Run6Cc8JE0P1AxG74G6ToT7FQ" #FunTry
#api_key = "AIzaSyD4opHMSOF8q44ie9wXxeOaLmmRMw7G1Rk" #ypn2021136
youtube = build("youtube", "v3", developerKey=api_key)


query = "craftswithkids"


excel_file = "youtube_scraping_data.xlsx"
sheet_name = "Sheet1"
fields = ["channel_id", "channel_name", "description", "subscriber_count", "video_count", "view_count", "country", "published_at", "email"]


if not os.path.isfile(excel_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = sheet_name
    ws.append(fields)
    wb.save(excel_file)


try:
    search_response = youtube.search().list(
        q=query,
        type="channel",
        part="id,snippet",
        maxResults=50
    ).execute()
except HttpError as e:
    print("An error occurred while searching for channels: %s" % e)
    search_response = None


while search_response is not None:
    for search_result in search_response.get("items", []):

        channel_id = search_result["id"]["channelId"]
        channel_snippet = search_result["snippet"]

        channel_response = youtube.channels().list(
            id=channel_id,
            part="snippet,statistics"
        ).execute()

        channel_data = channel_response["items"][0]
        channel_name = channel_snippet["title"]
        description = channel_snippet["description"]
        subscriber_count = channel_data["statistics"]["subscriberCount"]
        video_count = channel_data["statistics"]["videoCount"]
        view_count = channel_data["statistics"]["viewCount"]
        country = channel_data["snippet"].get("country", "")
        published_at = channel_data["snippet"]["publishedAt"]
        email = channel_data["snippet"].get("email", "")

        wb = openpyxl.load_workbook(excel_file)
        ws = wb[sheet_name]
        ws.append([channel_id, channel_name, description, subscriber_count, video_count, view_count, country, published_at, email])
        wb.save(excel_file)

        print(f"Channel {channel_name} successfully written to {excel_file}")

    # check if there are more pages of results
    if "nextPageToken" in search_response:
        next_page_token = search_response["nextPageToken"]
        try:
            search_response = youtube.search().list(
                q=query,
                type="channel",
                part="id,snippet",
                maxResults=50,
                pageToken=next_page_token
            ).execute()
        except HttpError as e:
            print("An error occurred while searching for channels: %s" % e)
            search_response = None
    else:
        search_response = None


 1m 34s
