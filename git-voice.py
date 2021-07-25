import subprocess as sp
import speech_recognition as sr
from win32com.client import Dispatch
import os
import webbrowser
import time


speak = Dispatch("SAPI.SpVoice").Speak
rec = sr.Recognizer()
speak("Hello welcome to the Voice based Git tool by Mubin")
speak("Before doing any action please let me know the repository where the tasks would be performed in the prompt below")
rsp=input("Enter the repository url:  ")



def main():
    init()
    
    while True: 
        with sr.Microphone() as source0:               
            speak("Tell me what can i do for you")
            rec.adjust_for_ambient_noise(source0, duration=2)
            user0=rec.listen(source0)              
        user0i=rec.recognize_google(user0)             
        
        print("You told ",user0i)
        
        if ("create" in user0i or "initialise" in user0i or "initialize" in user0i):
            init()
        
        elif ("clone" in user0i or "download" in user0i or "copy" in user0i):
            cln()
       
        elif ("restore" in user0i or "retrieve" in user0i):
            restore()
        
        elif("upload" in user0i or "upload code" in user0i or "push" in user0i):
            lfs()
        
        elif ("scratch" in user0i or "start" in user0i):
            repo()
        
        elif ("commit" in user0i or "message" in user0i):
            commit()
        
        elif ("push" in user0i):
            push()
        
        elif ("revert" in user0i or "undo" in user0i or "revert" and "change" in user0i):
            revert()
        
        elif ("save" in user0i or "temporarily" in user0i or "stash" in user0i):
            stash()
        
        elif("apply" and " temporary save" in user0i or "apply temporary change"  in user0i or "apply temporary change" in user0i or "stash apply" in user0i):
            stashapp()
        
        elif("nothing" in user0i or "finish" in user0i or "exit" in user0i):
            break
        
        else:
            speak("Not recognized please try again")

def lfs():
    speak("Ok so you want to upload files no problem i have got a solution for it")
    time.sleep(2)
    speak("Where are your files located")
    currdir=os.getcwd()
    print("This is you current directory",currdir)
    lctfls=input("Enter the location of files: ")
    os.chdir(lctfls)
    speak("Now let us add the file you want to upload")
    lfi=input("Enter the name of file , if you want to add multiple files use this format file1.txt file2.py:  ")
    addlf1="git add"+" "+lfi
    print(addlf1)
    sp.run(addlf1)
    commit()
    push()
    
def init():
    speak("Do you want to initialize the repository")
    with sr.Microphone() as source01:
        user01=rec.listen(source01)
    user01i=rec.recognize_google(user01)
    speak("Ok wait")
    print(user01i)
    if ("yes " in user01i or "i want to" in user01i or "initialise" in user01i):
        speak("Please enter the directory where you want to intialise a repository")
        cdir=os.getcwd()
        print("This is you current directory",cdir)
        rmtd=input("Enter the directory path: ")
        initr="git init"+" "+rmtd
        sp.run(initr)
    elif("no" in user01i or "it is" in user01i or "it's already initialized" in user01i or " it's already initialised" in user01i):
        speak("Ok it seems that you already have an repository initialized")

def commit():
    speak("Now as we have added the files let's commit them please say what should be the commit message")
    with sr.Microphone() as source02:
        rec.adjust_for_ambient_noise(source02, duration=1)
        user02=rec.listen(source02)
    user02i=rec.recognize_google(user02)
    print(user02i)
    cmtmsg='git commit -m'+' '+'"'+user02i+'"'
    print(cmtmsg)
    sp.run(cmtmsg)

def push():
    speak("Now as we have committed the files we need to push our files")

    speak("In which branch you want to push the files")
    speak("If you want main branch keep the letter M of it capital")
    
    branch=input("Branch name : ")
    speak("Do you want to create new branch")
    with sr.Microphone() as source09:
        rec.adjust_for_ambient_noise(source09, duration=1)
        user09=rec.listen(source09)
    user09i=rec.recognize_google(user09)
    print(user09i)
    if("yes" in user09i or "create" and "new" in user09i):
        branchc="git checkout -b"+" "+branch
        sp.run(branchc)
    else:
        fetch="git fetch"+" "+rsp
        sp.run(fetch)
        psh="git push --force"+" "+rsp+" "+branch
        sp.run(brnch)
        sp.run(psh)
        time.sleep(2)
        speak("hey user you are good to go all files are uploaded")    

def cln():
    speak("please write the username followed by the repository name which you want to clone")
    print("example- th3gentleman-MubinGirach/test")
    user2=input("Enter the username/repositoryname: ")
    cw=os.getcwd()
    print("This is your current directory",cw)
    speak("Please enter the directory where you want to clone in the below prompt")
    path=input("Enter the directory: ")
    os.chdir(path)
    clone="git clone https://github.com/"+user2
    sp.run(clone)
    speak("Successfully cloned")

def revert():
    speak("No problem if you have committed a mistake we will try to fix it")
    with sr.Microphone() as source04:
        speak("Tell me in which branch you want undo the changes")
        time.sleep(0.20)
        rec.adjust_for_ambient_noise(source04)
        user04=rec.listen(source04)
        speak("Ok wait")
    user04i=rec.recognize_google(user04)
    print(user04i)
    if rsp.endswith('.git'):
        newrsp = rsp[:-4]
    print(newrsp)
    web=newrsp+"/commits/"+user04i
    webbrowser.open(web)
    speak("Please enter the commit id to which you want to revert the changes")
    rvt=input("Enter the commit id: ")
    chg="git revert"+" "+rvt
    sp.run(chg)
    speak("Now do you want to push these updates")
    with sr.Microphone() as source05:
        time.sleep(0.25)
        user05=rec.listen(source05)
        speak("Ok wait")
    user05i=rec.recognize_google(user05)
    print(user05i)
    if ("yes" in user05i or "want to push" in user05i):
        pchg="git push --force"+" "+rsp+" "+user04i
        sp.run(pchg)
    else:
        speak("No problem")

def restore():
    speak("Please make sure that the file you want to restore was been tracked by git before it got deleted")
    speak("Please provide me the name of file which you want to restore")
    rstr=input("Enter the filename: ")
    restr="git restore"+" "+rstr
    sp.run(restr)

def repo():
    speak("Ok great seems so you have created a brand new repository let me help you")
    time.sleep(3)
    lfs()
    
def stash():
    speak("I understand that you want to keep your workspace clean we got a solution for it")
    speak("what should be the temporary save named as ")
    with sr.Microphone() as source06:
        rec.adjust_for_ambient_noise(source06)
        user06=rec.listen(source06)
    user06i=rec.recognize_google(user06)
    print(user06i)
    speak("performing temporary save")
    stsh="git stash save"+" "+user06i
    sp.run(stsh)

def stashapp():
    speak("Thats great that you are using stash feature")
    speak("Here is your list of stash")
    sp.run("git stash list")
    speak("Tell me the serial number of the stash and i will apply it for you")
    with sr.Microphone() as source07:
        rec.adjust_for_ambient_noise(source07)
        user07=rec.listen(source07)
    user07i=rec.recognize_google(user07)
    print(user07i)
    li=[]
    li.append(user07i)
    for i in li:
        apply="git stash apply stash@{"+i+"}"
        print(apply)
        sp.run(apply)
    speak("Do you want to further push it to the respository")
    with sr.Microphone() as source08:
        user08=rec.listen(source08)
    user08i=rec.recognize_google(user08)
    if ("yes" in user08i or "push" in user08i):
        lfs()
    else:
        speak("no problem")
    

    

main()
