
import os

fileType = [".exe",".deb","zip","iso","rar","msi","7z"]
filelist = []
pathlist = []
floder = "E:\\Tools\\"
desName = "E:\\SoftTools.txt"
for root,dirs, files in os.walk(floder):
    for file in files:
        path = root + os.sep + file
        for typeN in fileType:
            if file.endswith(typeN):
                filelist.append(file)
                pathlist.append(path)
        
with open(desName,"w",encoding='utf-8') as f:
    for file in filelist:
        f.write(file)
        f.write("\n")
   
    for x in range(10):
        f.write("\n")
    for file in pathlist:
        f.write(file)
        f.write("\n")