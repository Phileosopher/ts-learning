import os

dirname = "."
fileType = "py"

for path, dirs, files in os.walk(dirname):
    # print path and directories
    files = [f for f in files
             if f.endswith(fileType)]

    for eachFile in files:
        result = os.path.join(path, eachFile)
        print('result:',result)
    # print('-' * 40)


