import os
import mimetypes

def ParseSearch():
    target_file = raw_input('Enter the name of the file(Separate with comma): ')
    target_type = raw_input('Enter the type of the file(Separate with spaces): ').split()
    target_dir = raw_input('Enter directory (Press Enter for current directory)(Separate with comma): ')
    
    flag = 0
    if target_file:
        target_file = target_file.split(',')
        for i in range(len(target_file)):
            target_file[i] = target_file[i].lower()
            if target_file[i].startswith(' '):
                target_file[i] = target_file[i][1:]
        target_file = list(set(target_file))
    else:
        target_file = ['']
    
    if target_dir:
        invalid_dir = []
        target_dir = target_dir.split(',')
        for i in range(len(target_dir)):
            if target_dir[i].startswith(' '):
                target_dir[i] = target_dir[i][1:]
            if not os.path.isdir(target_dir[i]):
                print 'Invalid Directory',target_dir[i]
                invalid_dir.append(target_dir[i])
            else:
                flag = flag+ 1
        
        if invalid_dir:
            for i in range(len(invalid_dir)):
                target_dir.remove(invalid_dir[i])           
            
    else:
        target_dir = [os.getcwd()]
    if flag == 0:
        target_dir = [os.getcwd()]
        
    search(target_file, target_type, target_dir)
    
def search(target_file, target_type=None, target_dir=[os.getcwd()]):
    """
    >>> search(["python","date","time","twitter"],["png","avi","txt","py"],["/home","/python"])
    
    To search in current directory without any file types:
    >>> search(["python","date","time","twitter"])
    
    Prints Path and filename
    """
        
    if not target_type:
        target_type = ['image/audio/text/video/application']
    else:
        for i in range(len(target_type)):
            target_type[i] = target_type[i].lower()
            if target_type[i].startswith('.'):
                target_type[i] = target_type[i].split('.')[-1]
            print target_type[i]    
            if target_type[i] == 'avi':
                target_type[i] = 'x-msvideo'
            elif target_type[i] == 'mkv':
                target_type[i] = 'x-matroska'
            elif target_type[i] == 'mov':
                target_type[i] = 'quicktime'
            elif target_type[i] == 'flv':
                target_type[i] = 'x-flv'
            print target_type[i]
            
    print 'searching for',target_file,'in',target_dir
                
    for k in range(len(target_dir)):
        for path, dirs, files in os.walk(target_dir[k]):
                for filename in files:
                    ctype, encoding = mimetypes.guess_type(filename)
                    if ctype:
                        maintype, subtype = ctype.split('/', 1)
                        for i in range(len(target_type)):
                            if maintype in target_type[i] or target_type[i] in maintype or target_type[i] in subtype:
                                for j in range(len(target_file)):
                                    if target_file[j] in filename.lower():
                                        print path,filename
