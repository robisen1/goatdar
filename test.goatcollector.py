#! python 2.7
# test the goat collector   

import goatcollector
import json


def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True
    
    
query = "cats"

goatquery = goatcollector.Goatcollector(query)

#.getTrendingTopic('#cats')

print goatquery.getCollection()

print type(goatquery.getCollection()) is str

resp_dict = json.loads(goatquery.getCollection())

print type(resp_dict) is dict

if is_empty(resp_dict['text']) == False:
    print resp_dict['text'].encode('utf-8')
    

print "that worked"

if 'media' in resp_dict['text'] == True:    
    if is_empty(resp_dict['entities']['media']) == False:
        print resp_dict['media']['url']
        print "cats"
        
if 'geo' in resp_dict['text'] == True:    
    if is_empty(resp_dict['geo']) == False:
        print resp_dict['geo']
        print "meow cats"
    
print "Robi Sen loves him some kitties"
#if is_empty(resp_dict['media']['url']) == False:    
# print resp_dict['media']['url']