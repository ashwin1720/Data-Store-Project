import datastore as p

import os

#Dictionary to store the time to live values of each key

def main():
    path = input("Enter Path: ")
    while True:
        #Checking the size of the directory by calling validatsize()
        boolf, totsize = p.validatesize(path)
        if (boolf == True):
            try:
                dir_list = os.listdir(path)
            except:
                #If the specified directory is not present, then a new directory is created
                os.mkdir(path)
                dir_list = os.listdir(path)
                print("\t\t\tNew Folder Has Been Created With The Specified Path")
            print("\n1. Create New Key\n2. Read The Contents From An Existing Key\n3. Delete An Existing Key\n4. Print The Files Of The Data Store\n5. Exit")
            #User needs to enter an option to carry out the operations
            option=input("\n\n\nEnter Option: ")
            
            if option=="1":
                key1 = input("\t\t\tEnter Key: ")
                ttl1 = int(input("\t\t\tEnter Time To Live: "))
                jsonstring = input("\t\t\tEnter The JSON Contents As A String: ")
                p.createdata(key1, ttl1, path, jsonstring)
                                            
            elif option=="2":
                key1 = input("\t\t\tEnter Key To Find: ")
                p.readdata(key1, path)
            elif option=="3":
                key1 = input("\t\t\tEnter Key To Delete: ")
                bool5 = p.deletedata(key1, path)
                if(bool5 == True):
                    print("\t\t\tFile Deleted")
                else:
                    print("\t\t\tNo Such File !!!")
                    
            elif option=="4":
                print("\n\tContents:")
                for contents in dir_list:
                    p.validatettl(contents, path)
                for new_contents in dir_list:
                    print("\t\t\t" + new_contents)
                                    
            elif option=="5":
                print("\t\t\tThank You")
                quit()
                
            else:
                print("\n\t\t\tEnter Valid Option")
            
        else:
            #Error message displayed to the user if the directory size greater than 1GB
            print("\t\t\tData Store Size Limit Exceeded.")
            print("\t\t\tMax Limit = 1GB")
            print("\t\t\tCurrent Size Of Data Store: "+ str(totsize) + "GB")
            break

if __name__ == '__main__':
    main()
