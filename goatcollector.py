#needs to be heavily refactored.


import twitter
import json

class Goatcollector:

    myresult = "1"

    def __init__(self,query):
        self.query = ""
        'goat collector class'
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
        
        # for debugging since sometime it does not seem to auth
        # print twitter_api
        
        # The Yahoo! Where On Earth ID for the entire world is 1.
        # See https://dev.twitter.com/docs/api/1.1/get/trends/place and
        # http://developer.yahoo.com/geo/geoplanet/
        WORLD_WOE_ID = 1
        US_WOE_ID = 2514815        
        # Prefix ID with the underscore for query string parameterization.
        # Without the underscore, the twitter package appends the ID value
        # to the URL itself as a special case keyword argument.
        
        world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
        us_trends = twitter_api.trends.place(_id=US_WOE_ID)
        
        #print world_trends
        #print
        #print us_trends
        #print json.dumps(world_trends, indent=1)
        #print
        #print json.dumps(us_trends, indent=1)
       
        world_trends_set = set([trend['name'] 
                                for trend in world_trends[0]['trends']])
        
        us_trends_set = set([trend['name'] 
                             for trend in us_trends[0]['trends']]) 
        
        common_trends = world_trends_set.intersection(us_trends_set)
        
        #print common_trends
        # XXX: Set this variable to a trending topic, 
        # or anything else for that matter. 

        q = '#Cats' 
        count = 100
        # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
        search_results = twitter_api.search.tweets(q=q, count=count)
        statuses = search_results['statuses']
        # Iterate through 5 more batches of results by following the cursor
        
        for _ in range(5):
            #print "Length of statuses", len(statuses)
            try:
                next_results = search_results['search_metadata']['next_results']
            except KeyError, e: # No more results when next_results doesn't exist
                break
                
            # Create a dictionary from next_results, which has the following form:
            # ?max_id=313519052523986943&q=NCAA&include_entities=1
            kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
            
            search_results = twitter_api.search.tweets(**kwargs)
            statuses += search_results['statuses']
        
        # Show one sample search result by slicing the list...
        Goatcollector.myresult = json.dumps(statuses[0], indent=1)
     
    def getCollection(self):
                
        return Goatcollector.myresult