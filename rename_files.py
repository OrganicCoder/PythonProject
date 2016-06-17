import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/Rawk/Desktop/PythonProject/alphabet2")
    print(file_list)

    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    #change directory
    os.chdir("/Users/RawK/Desktop/PythonProject/alphabet2")

    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

    #change directory back to the saved path
    os.chdir(saved_path)

rename_files()
