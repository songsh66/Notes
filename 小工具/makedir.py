import os
import shutil
path = "/home/shuang/workspace/python/chop/image/b/"
for i in range(0, 98):
    tar = path + str(i)
    if not (os.path.exists(tar)):
        shutil.rmtree(tar)
        #os.mkdir(tar)