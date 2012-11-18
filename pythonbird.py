#!/usr/bin/env python

'''
author: Daniele Faugiana
last update: October the 20th 2012 
version: 0.1
'''

import tweepy
from time import sleep
from auth import startAuth
from os import path

#Authorize this application
api = startAuth()

#Get yourself's object
myself = api.me()

#This function gets the last 1000 tweets given a user
def getTweets():
	print ('Write the name of the user you want to get tweets from')
	user = raw_input()
	print ('Getting tweets...')
	tweets = []
	for result in tweepy.cursor.Cursor(api.user_timeline,include_rts=True,screen_name=user).items():
		tweets = tweets + [result]
	return tweets


#This functions gets the people an user follows given his id
def getFollowing(userID):
	
	following = []
	for result in tweepy.cursor.Cursor(api.friends,id=userID).items():
		following = following + [result]
		
	return following



#This functions gets the people who follows an user given his id
def getFollowers(userID):
	
	following = []
	for result in tweepy.cursor.Cursor(api.followers,id=userID).items():
		following = following + [result]
	return following




#It checks differences between followings and followers	
def matchFollowers(user,otherUser=myself):
	
	#First user's followings
	print ('Getting',user.screen_name,'followings...')
	follo1 = getFollowing(user.id)
	
	#Then otherUser's followers
	print ('Getting',otherUser.screen_name,'followers...')
	follo2 = getFollowers(otherUser.id)
	
	common = []
	unCommon = []
	
	print ('Ckecking lists...')
	
	#Common followers/following
	for f1 in follo1:
		ID1 = f1.id
		for f2 in follo2:
			ID2 = f2.id
			if ID1==ID2:
				common = common + [f1]
				break #Only one follower can match
	
	#Uncommon followers/following
	for f in follo1:
		if f not in common:
			unCommon = unCommon + [f]
	
	return [common,unCommon]




#It simple UNfollows an user
def defollow(user):
	api.destroy_friendship(user.id)
	return
	


#Shows people who don't follow you and asks for unfollowing 
def checkMatch():
	print ('Wait for followers/following scan \n')
	matches = matchFollowers(myself)
	
	goodList = []
	badList = []
	
	for match in matches[0]:
		goodList += [match.screen_name]
	
	for match in matches[1]:
		badList += [match.screen_name]
	
	
	print ''
	print ('These are',myself.screen_name,"'s followings who followback \n")
	for i in goodList:
		print (i)
	
	print ''
	print ('These are',myself.screen_name,"'s followings who don't followback \n")
	for i in badList:
		print (i)
	
	for i in matches[1]:
		print ''
		print ('Do you want to unfollow', i.screen_name,'?')
		print ('Type "u" to unfollow, "x" to exit, any other to ignore')
		answer = raw_input()
		if answer == 'd':
			defollow(i)
			print (i.screen_name,' has been unfollowed \n')
		elif answer=='x':
			break
		else:
			print ('Next... \n')
			
	print ('All operations done')			


#Sends a DM to all your followers
def massDM():
	#It gets all your followers, first.
	print ('Searching followers...')
	x = getFollowers(myself.id)
	print ('You have '+str(len(x))+' followers')
	print ('Write your DM here (max 140 chars)')
	dmText = raw_input()
	if len(dmText) > 140:
		print ('You talk too much')
		print ('Write your DM again')
		dmText = raw_input()
		
	countSent = 0 #Sent DMs
	countUnsent = 0 #Unsent DMs
	
	#Sends 1 DM every second
	for follower in x:
		try:
			receiverID = follower.id
			api.send_direct_message(user_id=receiverID,text=dmText)
			countSent += 1
		except:
			countUnsent += 1 #If anyone unfollow you during the process
		sleep(1)
		
	print ('\n'+str(countSent)+' DMs have been sent')
	print ('PythonBird could not send '+str(countUnsent)+' DMs\n')
	return
	

#Saves a tweets list on a text file
def fileSaveTweets(tweetsList):
	lenght = len(tweetsList)
	user = tweetsList[0].user
	name = user.screen_name
	thisPath = path.abspath(__file__)
	thisPath = path.dirname(thisPath)
	tweetsFile = open('tweets.txt','w') #Create a file
	tweets = []
	print ('Writing file...\n')
	errors = 0
	for tweet in tweetsList:
		try:
			tweets = tweets + [str(tweet.text)+'\n\n']
		except:
			errors += 1
			pass
	tweetsFile.write('THESE ARE '+name+' LAST ' +str(lenght-errors)+' TWEETS\n')
	tweetsFile.write('===============================\n')
	tweetsFile.writelines(tweets)
	tweetsFile.close()
	print ('PB has been unable to save '+str(errors)+' tweets\n')
	print (str(lenght-errors)+' tweets have been saved\n')
	print ('File has been saved in '+str(thisPath)+'/tweet.txt\n')
	return 	

#Sends a tweet
def update_status():
        tweet = raw_input("Insert your tweet: ")
        while len(tweet) > 140:
            print ("The tweet must be less or equal to 140 characters")
            tweet = raw_input("Insert your tweet: ")
        api.update_status(tweet)
        return

#Creates a new list
def create_list():
        name = raw_input("Insert the name of the list you want to create: ")
        description = raw_input("Insert the description of the list: ")
        api.create_list(name, description)
        print ("List created")
        return

#Adds a member to a list
def add_list_member():
        slug = raw_input("Which list? ")
        user = raw_input("Which user do you want to add to the list? ")
        api.add_list_member(slug, user)
        return

#Destroys a list
def destroy_list():
        slug = raw_input("Which list do you want to delete?")
        api.destroy_list(slug)
        print ("List deleted")
        return
        
def begin():
        
        begin = 'R'
        print ''
        print ('==================================================')
        print ('WELCOME TO PYTHONBIRD, A PYTHON-SHELL TWITTER TOOL')
        print ('==================================================')
        print ''
        print 'Hello', myself.screen_name
        print ('______________________________________________')
        print ''
        print 'What do you want to do?'
        print ''
        print '1. unfollow'
        print '2. mass-DM'
        print '3. send tweet'
        print '4. save tweets'
        print '5. create a list'
        print '6. add users to a list'
        print '7. delete a list'
        while(begin is 'R' or begin is 'r'):
                answer = input()
                while (not ((answer == 1) or (answer == 2) or (answer == 3) or (answer == 4) or (answer == 5) or (answer == 6) or (answer == 7))):
                        print ('Bad choice, try again: 1 = unfollow, 2 = mass-DM, 3 = update your status, 4 = save tweets, 5 = create a list, 6 = add users to a list, 7 = delete a list')
                        answer = input()
        
                if answer == 1:
                        checkMatch()
                        
                elif answer == 2:
                        massDM()
                        
                elif answer == 3:
                        update_status()
                        
                elif answer == 4:
                        timeline = getTweets()
                        fileSaveTweets(timeline)

                elif answer == 5:
                        create_list()

                elif answer == 6:
                        add_list_member()

                elif answer == 7:
                        destroy_list()

                print ('Type R to restart, X to exit')
                begin = raw_input()
                print ("What do you want to do, now?")
                print ''
        return
                

if __name__=="__main__":
        begin()
        
