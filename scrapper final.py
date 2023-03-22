# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:04:13 2023

@author: siddh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:36:34 2023

@author: siddh
"""
import instaloader
import openpyxl

# Create an instance of Instaloader class
L = instaloader.Instaloader()
#L.login('python9174','Siddhant@7482')

# Define the hashtag to search for
hashtag = input("Enter the hashtag to search for: ")

# Get the Hashtag object for the specified hashtag
hashtag_obj = instaloader.Hashtag.from_name(L.context, hashtag)

# Load the workbook if it exists, otherwise create a new one
try:
    wb = openpyxl.load_workbook("instagram_data.xlsx")
    ws = wb.active
except FileNotFoundError:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Username", "Userid", "Total posts", "Followers", "Following", "Bio", "Profile link"])

# Set the maximum number of posts to scrape
max_posts = 30

# Loop through all the recent posts for the hashtag
for post in hashtag_obj.get_posts():
    username = post.owner_username
    profile = instaloader.Profile.from_username(L.context, username)
    
    # Check if the user has more than 2000 followers before scraping their data
    if profile.followers >= 2000:
        # Write the scraped data to the Excel file
        ws.append([profile.username, profile.userid, profile.mediacount, profile.followers, profile.followees, profile.biography, profile.external_url])

        # Exit the loop if we have scraped the maximum number of posts
        if ws.max_row >= max_posts:
            break

# Save the changes to the Excel file
wb.save("Games.xlsx")
