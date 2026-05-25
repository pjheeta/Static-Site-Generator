import os
import shutil

def publicCleanup(src,dst):

    if os.path.exists(dst):  
        print (f'Directoy "{dst}" is present')      
        shutil.rmtree(dst)
        print (f'Directoy "{dst}" has been deleted')  
    os.mkdir(dst)
    print (f'Directoy "{dst}" has been created') 
    files = os.listdir(src)
    for file in files:
        if os.path.isfile(os.path.join(src,file)) is True:
            shutil.copy(os.path.join(src,file), os.path.join(dst,file)) 
            print (f'copying "{os.path.join(src,file)}" to "{os.path.join(dst,file)}"')  
        else:
            publicCleanup(os.path.join(src, file), os.path.join(dst, file))