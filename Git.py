import subprocess as sp
import speech_recognition as sr
import pyttsx3
from win32com.client import Dispatch
import os
import pyaudio


main()



def main():
    speak = Dispatch("SAPI.SpVoice").Speak
    speak("Hello user welcome to the git tool by Mubin ggiraach")
   
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Tell me what can i do for you")
        user1=rec.listen(source)
        speak("Ok wait")

    user1i=rec.recognize_google(user1)
    print(user1i)

    if ("create" or "initialise" in user1i) :
        init()
    
    elif ("clone" or "download" in user1i):
        cln()

    elif ("add" or "upload" in user1i):
        addfls()
    
    elif ("restore" in user1i):
        restore()

    elif("upload large file" in user1i):
        lfs()




    
def init(): 
    speak("where u want to initialize")
    with sr.Microphone() as source3:
        user3=rec.listen(source3)
        speak("Ok wait")
    user3i=rec.recognize_google(user3)
    print(user3i)
    
    if ("here" in user3i or "current"in user3i):
        sp.run("git init")
    
    elif ("other" or "another" in user3i):
        speak("Please enter the directory where you want to intialise a repository")
        rmtd=input("Enter the directory path: ")
        initr="git init"+" "+rmtd
        sp.run(initr)
    
    else:
        speak("Please follow proper instructions")

    


def restore():
    speak("Please make sure that the file you want to restore was been tracked by git before it got deleted")
    speak("Please tell me which file you want to restore")
    rstr=input("Enter the filename: ")
    restr="git restore"+" "+rstr
    sp.run(restr)



def lfs():
speak("Ok so you are having a large file no problem i have got a solution for it")
sp.run("git install lfs")
speak("Now let us track the file you want upload")
speak("If you want to add all files with a certain extension we can do that or we can simply add one file")
trk=input("Enter the directory you want to track: ")
track="git track"+" "trk
sp.run(track)
speak("Now let us add that large file")
lf=input("name of large file: ")
addlf="git add"+" "+lf
sp.run(addlf)
commit()
push()



def repo():
    speak("Ok great seems so you have created a brand new repository let me help you")
    speak("Please tell me where is your code so I can initialise a reposiroty there ")
    code = input("Enter the directory: ")
    create= "git init"+" "+code
    sp.run(create)
    speak("Respository initialised lets add files now ")
    speak("Which files you want to add")
    print("For Multiple files give the name of files as file1.txt file2.py file3.png ")
    print("For adding all the files in the directory just give a character . in the input")
    files=input("Enter the file name: ")
    addfiles="git add"+" "+files
    sp.run(addfiles)
    commit()
    sp.run("git branch -M main")
    speak("Please enter your repository u r l where you want to upload these files")
    url=input("Enter the repository url: ")
    rmto="git remote add origin"+" "+url
    sp.run(rmto)
    sp.run("git push -u origin main")
    speak("hey user you are good to go all files are uploaded")

def commit():
    speak("Now as we have added the files let's commit them please say what should be the commit message")
    with sr.Microphone() as source3:
        usercmt=rec.listen(source3)
        userc=rec.recognize_google(usercmt)
        print(userc)
    cmtmsg="git commit -m"+" '"+usercmt+"'"


def cln():
    speak("please write the username followed by the repository name which you want to clone")
    print("example- th3gentleman-MubinGirach/test")
    user2=input("Enter the username/repositoryname: ")
    clone="git clone https://github.com/"+user2
    sp.run(clone)
    speak("Successfully cloned")

def addfls():
    with sr.Microphone() as source1:
        speak("Which file you want to add")
        user2=rec.listen(source1)
        speak("Ok wait")
    user2i=rec.recognize_google(user2)
    print(user2i)
    if ("all" in user2i):
        sp.run("git init")
        sp.run("git add .")
    else:
<<<<<<< HEAD
        speak("Please write the name of files in the below prompt")
        print("Example file1.txt file2.py ")
        file=input("Enter the file names with extensions: ")
        add="git add"+file
        sp.run(add)

def push():
    speak("Now we need to push our files")
    sp.run("git branch -M main")
    speak("Please enter your repository u r l where you want to upload these files")
    url=input("Enter the repository url: ")
    rmto="git remote add origin"+" "+url
    sp.run(rmto)
    sp.run("git push -u origin main")
    speak("hey user you are good to go all files are uploaded")















    


=======
        speak("I tried installing git for windows , ubuntu and redhat but nothing worked try using the program in a terminal with admin privileges")
        
elif ("add" in user1i or "upload" in user1i):
   with sr.Microphone() as source1:
    speak("Which file you want to add")
    user2=rec.listen(source1)
    speak("Ok wait")
   user2i=rec.recognize_google(user2)
   print(user2i)
   if ("all" in user2i):
    sp.run("git init")
    sp.run("git add .")
   else:
     speak("Please write the name of files in the below prompt")
     print("Example file1.txt file2.py ")
     file=input("Enter the file names with extensions: ")
     add="git add"+file
     sp.run(add)
>>>>>>> db4019b0d7fe9e68955575aad0f6203c66f5887d


    
   
        
     

    
   


    
     
    
  
    

    

     
    
#if ("init"in useri):
    #os.system("git init")



