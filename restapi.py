import requests
import json
import string

def get_synonyms(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_syn"] = word
    params_diction["max"] = "3" # get at most 1 results
    resp = requests.get(baseurl, params=params_diction)
    return resp

# return the top three words
resp = get_synonyms('funny')
print(resp.url)
print(resp.status_code)
print(resp.json())