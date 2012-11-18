#!/usr/bin/env python

'''
author: Daniele Faugiana
last update: October the 20th 2012 
version: 0.1
'''

import os 
import tweepy
import webbrowser
from consumer import CONSUMER_KEY, CONSUMER_SECRET
from access import ACCESS_KEY, ACCESS_SECRET

def startAuth():
    #Firstly check if CK and CS are available
    if ((not CONSUMER_KEY) or (not CONSUMER_SECRET)):
        print ('CCK ERROR, KEYS ARE NOT AVAILABLE ANYMORE')
        print ('Please, register a new app on Twitter Developers')
    
    #If available, it starts a new OAuth handler
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    
    #Now it checks if accesses are available
    if (ACCESS_KEY and ACCESS_SECRET):
        #If available start an api instance
        auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
        api = tweepy.API(auth)
        return api
    
    else:
        #Else it start the authentication procedure
        auth_url = auth.get_authorization_url()
        webbrowser.open(auth_url)
        print ('Write here the pin after browser authentication')
        verifier = raw_input(' Insert PIN: ').strip()
        auth.get_access_token(verifier)
        
        accessKey = auth.access_token.key
        accessSecret = auth.access_token.secret
        
        #It gets Access keys and show them
        ak = 'ACCESS_KEY = "' + str(accessKey) + '"\n'
        aS = 'ACCESS_SECRET = "' + str(accessSecret) + '"\n'
        
        print ('These are your personal keys')
        print (ak)
        print (aS)
        
        #It overwrites keys in the access file
        thispath = os.path.abspath(__file__)
        thispath = os.path.dirname(thispath)
        filePath = thispath + '/access.py'
        accessfile = open(filePath,'w')
        accessfile.write(ak)
        accessfile.write(aS)
        accessfile.close()
    
        print ('Your keys have been saved in', filePath, '\n \n')
        
        #Finally it calls itself to get the api object
        auth.set_access_token(accessKey,accessSecret)
        api = tweepy.API(auth)
        return api
