import os

def clutter67fun(folderpath,extention):
    files=os.listdir(folderpath)
    i=1
    for file in files:
        if file.endswith(extention):
            print(file)
            os.rename(f"{folderpath}/{file}",f"{folderpath}/{i}{extention}")
            i=i+1
            
folderpath="C:/Users/BHAVYA MITTAL 1729/Desktop/mathscopy"
extention=".png"
clutter67fun(folderpath,extention)