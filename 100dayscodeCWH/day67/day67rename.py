import os
folderpath="G:/pythonjourney/100dayscodeCWH/day67"
extention=".png"
files=os.listdir(folderpath)
i=1
for file in files:
    if file.endswith(extention):
        print(file)
        os.rename(f"{folderpath}/{file}",f"{folderpath}/{i}{extention}")
        i=i+1