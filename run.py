#! /usr/bin/env python3


# The Script opens all files on a dir as TextFiles
# and process line by line the file creating a dictionary
# with predefined keys
#
# Variables
#   pathOrigin = Directory where the TextFiles are stored
#   destinationUrl = (post) URL to send the JSON Obkects
#   types = Dictionary keys


# Imports
import os
import requests

# Origin Directory and Desination URL
pathOrigin = "/data/feedback"
destinationUr1= "http://34.171.37.47/feedback/"

# List of files on pathOrigin
foundFilesList = os.listdir(pathOrigin)

# Show Feedback
print(">>> Files found: ", foundFilesList)

# File iteration
for file in foundFilesList:
    types = ["title","name","date","feedback"]
    jsonItem = {}
    print(">>> Processing file: ", file)

    #Text Lines iteration
    with open(pathOrigin+"/"+file,"r") as txtfile:
        x = 0
        for line in txtfile:
            # Delete line jumps
            jsonItem[types[x]] = line.rstrip('\n')
            x += 1
    # Show Feedback
    print(">>> Processed file ", file, "as: ", jsonItem)
    response = requests.post(destinationUrl,json=jsonItem)

    # Show Feedback - HTTP Response code
    print(">>>>>>>>> RESPONSE (201 = ok): ", response.status_code)
