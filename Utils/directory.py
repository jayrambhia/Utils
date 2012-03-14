import os

def makeDir(path):
    """
    You want to make a directory: Python/Workspace/Utils/diskUtils/
    and Python/Workspace exists but Python/Workspace/Utils does not.
    
    So instead of making Python/Workspace/Utils and then making
    Python/Workspace/Utils/diskUtils/ , 
    
    >>> makeDir("Python/Workspace/Utils/diskUitls")
    
    It would first create Python/Workspace/Utils and then
    Python/Workspace/Utils/diskUtils
    
    It can be extended for any number of branches.
    """
    if os.path.isdir(path):
        return
    dir1, dir2 = os.path.split(path)
    makeDir(dir1)
    os.mkdir(path)
    return
