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
            # small delay to allow for unique names
            time.sleep(1)

def backup(lst = [], inpath = '', outpath = ''):
    'Backs Up files in the Skyrims Data Directory Created to safely backup the mods that I am creating on'
    
    # Makes sure inpath is set to data directory
    if not 'Skyrim Special Edition/Data' in inpath:
        inpath = os.path.join(inpath, 'Data')
    
    # backsup files
    items = os.listdir(inpath)
    for item in items:
        if item in lst:
            fpath = os.path.join(inpath, item)
            print('Copying {} to {}'.format(item, outpath))
            shutil.copyfile(fpath, outpath)


# Code needed for the .bat file to call functions properly
if __name__ == '__main__':
    try:
        function = sys.argv[1]
        var = sys.argv[2]
        inpath = sys.argv[3]
        outpath = sys.argv[4]
        if function == 'rename':
            rename(var, inpath, outpath)
        elif function == 'backup':
            backup(var, inpath, outpath)
    except:
        pass
