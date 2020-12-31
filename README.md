# Data-Store


1. The user has to enter a path of any folder where the keys have to be stored. If the folder does not exist, a new folder is created in that path.

2. The maximum size of the directory/folder where these keys are created is 1GB.

3. There are 5 options from which the user has to select from. 

      a. Create:

            i. Create option creates a key which stores JSON objects as value inside it. 
               Keys are unique, and no keys can have the same name.
      
            ii. The entered key name should be of length<=32. If not, error arises.
      
            iii. The JSON value that has to be stored inside the key should be <=16KB.

            iv. Time To Live of each key has to be entered by the user (in seconds). 
                After that time, the key will be deleted from the data store.
      b. Read:
      
            i. Read option displays the JSON value of a key specified by the user.

            ii. Error will be displayed if the Time To Live for that key has expired or
                if the file is not existing.
      c. Delete:

            i. Delete option deletes the key from the path that was specified.
            
            ii. Error will be displayed if the Time To Live for that key has expired or 
                if the file is not existing.
            
      d. View All Files:
      
            i. Lists the available files in the specified directory.
            
      e. Exit:
      
            i. Exit option returns from the execution.


# Unit Testing:

      Run the test_datastore.py for the execution of unit test cases.
      
# Execution:

      Run the main_datastore.py and follow the above steps for execution.
      
      
# Environment:
      
      The project works with both Windows and LINUX. 
      
      Unit tests are written only for Windows.
