# Program to backup the files in a given directory to a shared network drive.

import os
import datetime
from pathlib import Path
import pathlib
import shutil


now = datetime.datetime.now()
ago = now - datetime.timedelta(days = 1)

# backupFolder is a method that will backup sourceDir to backupDir
# @param sourceDir Path object to the source to backup
# @param backupDir Path object to the backup destination
def backupFolder(sourceDir, backupDir):
    #filePath = Path('C:/', 'temp')
    #backupLocation = Path('D:/', 'backup', 'temp')
    filePath = sourceDir
    backupLocation = backupDir

    for root, dirs, files in os.walk(filePath):
        for fname in files:
            path = os.path.join(root, fname)
            timestamp = os.stat(path)
            mtime = datetime.datetime.fromtimestamp(timestamp.st_mtime)
            if mtime > ago:
                print('%s modified %s'%(path, mtime))
                destFile = path.replace(str(filePath), str(backupLocation), 1)
                destFileParent = os.path.dirname(destFile)
                if not os.path.isdir(destFileParent):
                    print('Directory %s did not exist. Creating directory.'%(destFileParent))
                    pathlib.Path(os.path.dirname(destFile)).mkdir(parents=True, exist_ok=True)
                shutil.copy(path, destFile)

sourcePath = Path('C:/', 'temp')
backupPath = Path('D:/', 'backup', 'temp')

backupFolder(sourcePath, backupPath)

print('Done with scanning files.')
