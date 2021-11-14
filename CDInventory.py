#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DDefelici, 2021-Nov-14, replaced inner data structure (list) with dictionary, added functionality to load data and delete entry
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {} # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Load existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            line = row.strip().split (',')
            dicRow = {'id': line[0], 'title': line[1], 'artist': line[2],}
            lstTbl.append(dicRow)
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist' :strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            cdStr = ''
            for key, val in row.items():
                cdStr += str(val) + ', '
            print(cdStr + '\n')
    elif strChoice == 'd':
        # Delete entry
        chosenID = input('What is the ID of the CD you would like to delete?')
        cdtodel = None
        for row in lstTbl:
            if row['id'] == str(chosenID):
                cdtodel = row
                break
        if cdtodel != None:
            lstTbl.remove(cdtodel)
        pass
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for key, val in row.items():
                strRow += str(val) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

