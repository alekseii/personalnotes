import requests
import json
import string

def get_synonym(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_syn"] = word
    params_diction["max"] = "1" # get at most 1 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    if word_ds != []:
        # If we get a match, return match
        word = word_ds[0]['word']
    #else just return original input
    return word

def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url

preppedURL = requestURL('https://www.google.com/search', params = {'tab':'isch', 'q':'"violins and guitars"'})

resp = requests.get(preppedURL)
print(resp.url)
print(resp.status_code)
print(get_synonym('funny'))