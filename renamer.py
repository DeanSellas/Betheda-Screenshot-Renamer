import os, os.path
import sys
import shutil
import datetime
import time

def rename(prefix, inpath, outpath):
    'Renames Screenshots for games to date time format.'
    prefix = prefix.upper()
    print('Current Directory: {}'.format(inpath))
    print('Move To: {}'.format(outpath))
    items = os.listdir(inpath)
    #print(items)
    for item in items:
        curItem = os.path.join(inpath,item)
        curTime = datetime.datetime.now()
        curTime = curTime.strftime('%Y%m%d%H%M%S')
        if os.path.isfile(curItem) and 'ScreenShot' in item:
            fname = '{}{}.png'.format(prefix, curTime)
            fname = os.path.join(inpath,fname)
            print(item)
            os.rename(curItem, fname)
            shutil.move(fname, outpath)
            time.sleep(1)

if __name__ == '__main__':
    try:
        prefix = sys.argv[1]
        inpath = sys.argv[2]
        outpath = sys.argv[3]
        print(sys.argv)
        rename(prefix, inpath, outpath)
    except:
        pass

