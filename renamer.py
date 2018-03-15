import os, os.path, sys, shutil, datetime, time

def rename(prefix = '', inpath = '', outpath = ''):
    'Renames Screenshots for games to date time format.'
    
    # if outpath is empty just rename it
    if outpath == '':
        outpath = inpath
    prefix = prefix.upper()

    # prints directories
    print('Current Directory: {}'.format(inpath))
    print('Move To: {}'.format(outpath))

    items = os.listdir(inpath)
    #print(items)
    for item in items:
        curItem = os.path.join(inpath,item)
        if os.path.isfile(curItem) and 'ScreenShot' in item:
            
            # naming convention
            curTime = datetime.datetime.now()
            curTime = curTime.strftime('%Y%m%d%H%M%S')
            # renames file
            fname = '{}{}.png'.format(prefix, curTime)
            fpath = os.path.join(inpath,fname)
            print('Renaming {} to {}'.format(item, fname))
            os.rename(curItem, fpath)
            shutil.move(fpath, outpath)
            # small delay
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
