import os

home = "/home"
os.chdir(home)
folpath = os.listdir();
filepath = []

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
                    continue
    except Exception as e:
        print(e)

filecol2(folpath,filepath)
print(len(filepath))
for i in filepath:
    print (i)
