# https://developers.google.com/explorer-help/guides/code_samples#python

import os
from API import YT_DEVELOPER_KEY
import json
import googleapiclient.discovery


def main():
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = YT_DEVELOPER_KEY       # INSERT YOUR API_KEY HERE

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    request = youtube.search().list(
        part="snippet",
        maxResults=2,
        q="la peppina fa il caffe"
    )
    response = request.execute()
    links = []
    for items in response["items"]:
        links.append("https://www.youtube.com/watch?v=" + items["id"]["videoId"])
    print(json.dumps(links, indent=3))


if __name__ == "__main__":
    main()

