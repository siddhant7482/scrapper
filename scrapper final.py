# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:04:13 2023

@author: siddh
"""

import instaloader
import re
import numpy as np
import pandas as pd
from itertools import dropwhile, takewhile
import csv
def userinfo(topic):
    bot = instaloader.Instaloader()
    bot.login('python9174','Siddhant@7482')
    search_results = instaloader.TopSearchResults(bot.context, topic)
    for profile in search_results.get_profiles():
            if (profile.followers>=2000):
             email=re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
             username=profile.username
             User_ID=profile.userid
             Number_of_Posts=profile.mediacount
             FollowersCount=profile.followers
             FollowingCount=profile.followees
             Bio= profile.biography
             link=profile.external_url
             data=[]
             user_data={'Username':[username],'Name':[User_ID],'number of posts':[Number_of_Posts],'followers count':[FollowersCount],'following count':[FollowingCount],'bio':[Bio],'link':[link]}
             data.append(user_data)         
             df=pd.DataFrame(data)
        
            ''' data={profile.username, profile.userid,profile.mediacount,profile.followers,profile.followees,profile.biography,profile.external_url}
             print(data)
            
             print(profile)
             print("Username: ", profile.username)
             print("User ID: ", profile.userid)
             print("Number of Posts: ", profile.mediacount)
             print("Followers Count: ", profile.followers)
             print("Following Count: ", profile.followees)
             print("Bio: ", profile.biography)
             print("External URL: ", profile.external_url)
             emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
             print("Emails extracted from the bio:")
             print(emails)
             '''
            print(df)     
userinfo("Toys")
        