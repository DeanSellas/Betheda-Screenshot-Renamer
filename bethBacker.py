import os, os.path, sys, shutil, datetime, time

# ENTER PATH TO GAMES
falloutFourPath = ''
skyrimSpecialEditionPath = 'G:\Games\Steam\steamapps\common\Skyrim Special Edition'

# OUTPUT LOCATION
pictureOutPath = 'D:\Google Drive\Pictures\Games'
modOutPath = 'D:\Google Drive\Documents\Mods\Backups'

# Mods to backup
fo4ModLst = ['']
sseModLst = ['BetterBooks.esp']

# Dictionaries to make code easier to read later
gamePathDict = {'fo4': falloutFourPath, 'sse': skyrimSpecialEditionPath}
picturePathDict = {'fo4': os.path.join(pictureOutPath, 'Fallout 4'), 'sse': os.path.join(pictureOutPath, 'Skyrim')}
modPathDict = {'fo4': os.path.join(modOutPath, 'Fallout 4'), 'sse': os.path.join(modOutPath, 'Skyrim SE')}
backupDict = {'fo4': fo4ModLst, 'sse': sseModLst}

def rename(prefix = '', inpath = '', outpath = ''):
    'Renames Screenshots for games to date time format.'
    
    # if outpath is empty just rename it
    if outpath == '':
        outpath = inpath
    # if path doesnt exist create it
    elif not os.path.exists(outpath):
        os.makedirs(outpath)

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

def backup(modList = [], inpath = '', outpath = ''):
    'Backs Up files in the Skyrims Data Directory Created to safely backup the mods that I am creating on'
    
    # Makes sure inpath is set to data directory
    if not 'Skyrim Special Edition/Data' in inpath:
        inpath = os.path.join(inpath, 'Data')

    # if path doesnt exist create it
    if not os.path.exists(outpath):
        os.makedirs(outpath)

    # backsup files
    items = os.listdir(inpath)
    for item in items:
        if item in modList:
            fpath = os.path.join(inpath, item)
            outpath = os.path.join(outpath, item)
            print('Copying {} to {}'.format(item, outpath))
            shutil.copyfile(fpath, outpath)


# Code needed for the .bat file to call functions properly
if __name__ == '__main__':
    # print(sys.argv)
    # slices first item out (first item should always be file name!)
    sys.argv[:1]
    for item in sys.argv:
        game = item[7:]
        if item[:6] == 'rename':
            rename(game, gamePathDict[game], picturePathDict[game])
        elif item[:6] == 'backup':
            backup(backupDict[game], gamePathDict[game], modPathDict[game])
