import os

def fileRename():
    #gets directory from user
    direc = input('Enter folder:')
    while True:
        try:
            file_list = os.listdir(direc)
            break
        except:
            direc = input('Enter valid folder path:')

    #Rename each file to remove numbers
    os.chdir(direc)
    change = str.maketrans('', '', '0123456789')
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("Old Name - " + file_name.translate(change))
        os.rename(file_name, file_name.translate(change))

fileRename()
