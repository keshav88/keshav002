mydis={
    "fast": "in a quick manner",
    "harry": "a coder",
    "l1": [1,3,6],
    1:2,
    "mydis1":{"harry": "player",
              "a":5,}
}

# #Dictionary methods
# print(mydis.keys())
# print(mydis.values())
# print(mydis.items())

print(mydis)
updatedis={
    "lovish":"friend",
    "divya":"friend",
    "shubham":"friend"
}

mydis.update(updatedis)
print(mydis)

# print(mydis.get("harry")) #harry ke jo valuse hai woh show karega
# print(mydis["harry"]) #harry ke saath jo valuse hai woh show karega

# #the difference between .get and [] syntax in dictionaries  
# print(mydis.get("harry2")) #retruns none as harry2 mydis me nahi hai
# # print(mydis["harry2"]) #yeh error show karega because yeh mydis me hai he nahi 
