import os

home = "/home"
os.chdir(home)
user = os.listdir()

folpath = []
filepath = []

def filecol(fdlist, fol1, file) :
	for path in fdlist :
		os.chdir(path) 
		content2 = os.listdir()
		for item in content2 :
			if os.path.isfile(item) :
				file.append(os.path.abspath(item))

			else :
				folderpath = os.path.abspath(item)
				fol1.append(folderpath)
                
def filecol2(folpath, filepath):
    try:
        for folder in folpath:          
            child = os.listdir(folder)
            for content in child:
                abpath = f'{os.path.abspath(folder)}/{content}'
                if os.path.isfile(abpath):
                    filepath.append(abpath)
                elif os.path.isdir(abpath):
                    folpath.append(abpath)
                else:
                    pass
    except Exception as e:
        print(e)

filecol(user, folpath,filepath)
filecol2(folpath,filepath)
for i in filepath:
    print(i)
print(len(filepath))
