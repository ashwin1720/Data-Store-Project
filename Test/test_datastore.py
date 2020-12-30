import unittest


import sys


sys.path.insert(1, '/Users/HP/OneDrive/Desktop/My Folder/Games/Freshworks/SRC')

import datastore as d

class TestDataStore(unittest.TestCase):
    
        #TestCase To Create A New File In An Existing Directory
        def test_01_create(self):
            try:
                
                tc1_create = d.createdata("abc",100,"C:/Users/HP/OneDrive/Desktop/My Folder/Games", '{"A":1}')
                self.assertTrue(tc1_create)
                print("\t\t\ttest_01_create: Passed")
            except:
                print("\t\t\ttest_01_create: Failed")
            
        #TestCase To Create An Existing File (Should Raise Error)
        def test_02_create(self):
            try:
                
                tc2_create = d.createdata("abc",100,"C:/Users/HP/OneDrive/Desktop/My Folder/Games", '{"C":3}')
                self.assertFalse(tc2_create)
                print("\t\t\ttest_02_create: Passed")
            except:
                print("\t\t\ttest_02_create: Failed")

        #TestCase To Have A Key Name Whose Length Greater Than 32 (Should Raise Error)
        def test_03_create(self):
            try:
                tc3_create = d.createdata("qwertyuiopasdfghjklzxcvbnmqwertyu",100,"C:/Users/HP/OneDrive/Desktop/My Folder/Games", '{"D":4}')
                self.assertFalse(tc3_create)
                print("\t\t\ttest_03_create: Passed")
            except:
                print("\t\t\ttest_03_create: Failed")
            
        #TestCase To Read An Existing File In An Existing Directory
        def test_04_read(self):
            try:
                
                tc4_read = d.readdata("abc","C:/Users/HP/OneDrive/Desktop/My Folder/Games")
                self.assertTrue(tc4_read)
                print("\t\t\ttest_04_read: Passed")
            except:
                print("\t\t\ttest_04_read: Failed")
            
        #TestCase To Read A File From A Non Existing Directory (Should Raise Error)
        def test_05_read(self):
            try:
                
                tc5_read = d.readdata("abc","C:/Users/HP/OneDrive/Desktop/My Folder/Games/Read")
                self.assertFalse(tc5_read)
                print("\t\t\ttest_05_read: Passed")
            except:
                print("\t\t\ttest_05_read: Failed")

        #TestCase To Read A Non Existing File (Should Raise Error)
        def test_06_read(self):
            try:
                
                tc6_read = d.readdata("def","C:/Users/HP/OneDrive/Desktop/My Folder/Games")
                self.assertFalse(tc6_read)
                print("\t\t\ttest_06_read: Passed")
            except:
                print("\t\t\ttest_06_read: Failed")
            
        #TestCase To Delete An Existing File
        def test_07_delete(self):
            try:
                
                tc7_delete = d.deletedata("abc","C:/Users/HP/OneDrive/Desktop/My Folder/Games")
                self.assertTrue(tc7_delete)
                print("\t\t\ttest_07_delete: Passed")
            except:
                print("\t\t\ttest_07_delete: Failed")
                
        #TestCase To Delete A Non Existing File (Should Raise Error)
        def test_08_delete(self):
            try:
                
                tc8_delete = d.readdata("def","C:/Users/HP/OneDrive/Desktop/My Folder/Games")
                self.assertFalse(tc8_delete)
                print("\t\t\ttest_08_delete: Passed")
            except:
                print("\t\t\ttest_08_delete: Failed")
    

if __name__ == '__main__':
    unittest.main()
        
