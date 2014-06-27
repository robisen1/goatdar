#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search-geo
#  - performs a search for tweets close to New Cross, and outputs
#    them to a CSV file.
#-----------------------------------------------------------------------

import twitter 
import urllib
import sys
import csv
import json


json_credentials = open('twittersecret.json')
mycreds = json.load(json_credentials)

json_credentials.close()
# pull OAuth creds from json file
CONSUMER_KEY = mycreds["CONSUMER_KEY"]
CONSUMER_SECRET = mycreds["CONSUMER_SECRET"]
OAUTH_TOKEN = mycreds["OAUTH_TOKEN"]
OAUTH_TOKEN_SECRET = mycreds["OAUTH_TOKEN_SECRET"]

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# create twitter API object
#twitter = Twitter()

# open a file to write (mode "w"), and create a CSV writer object
csvfile = file("output.csv", "w")
csvwriter = csv.writer(csvfile)

# add headings to our CSV file
row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)

# the twitter API only allows us to query up to 100 tweets at a time.
# to search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.

def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True


# perform a search based on latitude and longitude
# twitter API docs: https://dev.twitter.com/docs/api/1/get/search

query = twitter_api.search.tweets(q="#Syria", geocode = "47.6097,122.3331,25km", count = 1)

#print query 
mytemp = json.dumps(query, indent=1)
# print mytemp
# make a dictionary from the JSON
resp_dict = json.loads(mytemp)

print resp_dict

#print type(resp_dict) is dict


my_list = resp_dict['statuses']

for doc in my_list:
    for key, value in doc.iteritems():
        if is_empty(value) == False:
            #print type(value)
            if isinstance(value, unicode):
                print key, value.encode('utf-8')
            else:
                print key, value



#print resp_dict['statuses']['entities']

#if 'media' in resp_dict['statuses']['text'] == True:    
    #if is_empty(resp_dict['entities']['media']) == False:
        #print resp_dict['media']['url']
        #print "cats"

#if 'geo' in resp_dict['text'] == True:    
    #if is_empty(resp_dict['geo']) == False:
        #print resp_dict['geo']
        #print "meow cats"

#for result in query["results"]:
        ## only process a result if it has a geolocation
        #if result["geo"]:
                #user = result["from_user"]
                #text = result["text"]
                #text = text.encode('ascii', 'replace')
                #latitude = result["geo"]["coordinates"][0]
                #longitude = result["geo"]["coordinates"][1]

                ## now write this row to our CSV file
                #row = [ user, text, latitude, longitude ]
                #csvwriter.writerow(row)

# let the user know where we're up to
#print "done page: %d" % (pagenum)

# we're all finished, clean up and go home.
csvfile.close()