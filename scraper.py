import snscrape.modules.twitter as sntwitter
import pandas as pd
import json
from datetime import datetime, timedelta

# Created a list to append all tweet attributes(data)
attributes_container = []

nowDate = datetime.now().date()
dateRange = 10
dataSize = 100

textSearch = " "

for d in range(1,dateRange):
    start = nowDate - timedelta(days=d)
    end = nowDate - timedelta(days=d-1)
    query = textSearch+' since:'+str(start)+' until:'+str(end)+" place:96683cc9126741d1"
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i>dataSize:
            print('append query \"'+query+'\" to the json file')
            break
        attributes_container.append({
                "Id" :tweet.id, 
                "Date":tweet.date, 
                "Place":tweet.place, 
                "Tweets":tweet.content.encode("utf-8"),
                "Hashtags": tweet.hashtags
            })


# Add a list from the tweets list above to data file

jsonString = json.dumps(attributes_container, indent=1, default = str)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()