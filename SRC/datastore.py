#To carry out directory related functions
import os
#To write contents into json files
import json
#Used to get size of dictionary
import sys
#To make use of time functions for time to live operations
import time
#Getting the path of the directory from the user where the key-value pairs have to be stored

#To create a key and store the value in it
dict1 = {}
def createdata(key1, ttl1, path, jsonstring):
    #Checking whether the key already exists in the given directory
    try:
        dir_list = os.listdir(path)
    except:
        #If the specified directory is not present, then a new directory is created
        os.mkdir(path)
        dir_list = os.listdir(path)
        print("\t\t\tNew Folder Has Been Created With The Specified Path")
    if(len(key1)>32):
                    print("\t\t\tKey Size Limit Exceeded.")
                    print("\t\t\tPlease Enter A Key With Size<=32")
                    print("\t\t\tCurrent Size Of Key: " + str(len(key1)))
                    return False
    else: 
        if key1+".json" in dir_list:
            print("\t\t\tAlready Existing Key")
            return False
        else:
            filename = path+'/'+ key1 + ".json"
            #Creating a key to store the values
            f1 = open(filename, 'w')
            jsondict = eval(jsonstring)
            #Checking the size of the value whether it is less than or greater than 16KB
            if (sys.getsizeof(jsondict)>16000):
                originalsize = sys.getsizeof(jsondict)/1000
                print("\t\t\tValue Size Exceeded.")
                print("\t\t\tOnly 16KB Or Less Is Allowed.")
                print("\t\t\tCurrent Size Of Value: " + str(originalsize) + "KB")
                os.remove(key1+".json")
                return False
            else:
                jsonwrite = json.dumps(jsondict, indent = 4)
                #Writing the JSON value to the corresponding key
                if(ttl1>0):
                    dict1[key1] = ttl1+time.time()
                    json.dump(jsonwrite, f1)
                else:
                    json.dump(jsonwrite, f1)
                f1.close()
                print("\t\t\tKey Created Successfully")
                return True

#Reading the JSON contents and printing it        
def readdata(key1, path):
    try:
        dir_list = os.listdir(path)
    except:
        print("\t\t\tInvalid Path")
        return False
    if key1+".json" in dir_list: 
        bool1 = validatettl(key1, path)
        if (bool1 == False):
            filename = path+'/'+ key1 + ".json"
            f1 = open(filename, 'r')
            data = json.load(f1)
            print(data)
            f1.close()
            return True
        else:
            print("\t\t\tTime To Live Expired")
            return False
    else:
        print("\t\t\tNo Such File !!!")
        return False
#Deleting the key from the directory
def deletedata(key1, path):
    dir_list = os.listdir(path)
    if key1+".json" in dir_list:
        bool3 = validatettl(key1, path)
        if (bool3 == False):
            filename = path+'/'+ key1 + ".json"
            os.remove(filename)
            return True
        else:
            #Time To Live Expired
            return False 
    else:
        #No Such File
        return False
#Function to validate time to live of each key
def validatettl(key1, path):
    if key1 in dict1:
        
            #If current time is more than the time to live of a particular key,
            #then the key is deleted
            if(dict1[key1]<=time.time()):
                deletedata(key1, path)
                del dict1[key1]
                return True
            else:
                return False
    else:
        return False
        
#Function to validate the size of the directory. It should be capped at 1GB
def validatesize(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for i in filenames:
            f = os.path.join(dirpath, i)
            total_size += os.path.getsize(f)
    totalsizegb = total_size/1000000000
    if (totalsizegb<=1):
        return True, totalsizegb
    else:
        return False, totalsizegb

    
