import subprocess as sp
import speech_recognition as sr
from win32com.client import Dispatch
import os
import webbrowser
from word2number import w2n




speak = Dispatch("SAPI.SpVoice").Speak
rec = sr.Recognizer()
speak("Hello welcome to the Voice based Git tool by Mubin")
speak("Before doing any action please let me know the repository where the tasks would be performed in the prompt below")
rsp=input("Enter the repository url:  ")


def main():
    while True: 
        
        with sr.Microphone() as source0:               
            speak("Tell me what can i do for you")
            user0=rec.listen(source0)                  
            speak("Ok wait")
        user0i=rec.recognize_google(user0)             
        
        print("You told this just now",user0i)
        
        if ("create" in user0i or "initialise" in user0i or "initialize" in user0i):
            init()
        
        elif ("clone" in user0i or "download" in user0i or "copy" in user0i):
            cln()
       
        elif ("restore" in user0i):
            restore()
        
        elif("upload" in user0i or "upload code" in user0i):
            lfs()
        
        elif ("scratch" in user0i or "start" in user0i):
            repo()
        
        elif ("commit" in user0i or "message" in user0i):
            commit()
        
        elif ("push" in user0i):
            push()
        
        elif ("revert" in user0i or "undo" in user0i):
            revert()
        
        elif ("save locally" in user0i or "temporary save" in user0i):
            stash()
        
        elif("apply local change" in user0i or "apply temporary change" in user0i):
            stashapp()
        
        elif("install" in user0i or "configure" in user0i):
            install():
        
        elif("nothing" in user0i or "finish" in user0i or "exit" in user0i):
            break
        
        else:
            speak("Not recognized please try again")

def lfs():
    speak("Ok so you want to upload files no problem i have got a solution for it")
    init()
    fetch="git fetch"+" "+rsp
    sp.run(fetch)
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
        speak("Ok wait")
    user01i=rec.recognize_google(user01)
    print(user01i)
    if ("yes" in user01i or "want to" in user01i):
        speak("Please enter the directory where you want to intialise a repository")
        cdir=os.getcwd()
        print("This is you current directory",cdir)
        rmtd=input("Enter the directory path: ")
        initr="git init"+" "+rmtd
        sp.run(initr)
    else:
        speak("Ok it seems that you already have an repository initialized")

def commit():
    speak("Now as we have added the files let's commit them please say what should be the commit message")
    with sr.Microphone() as source02:
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
    print("Main")
    branch=input("Branch name : ")
    branchc="git checkout -b"+" "+branch
    sp.run(branchc)
    brnch="git branch -M"+" "+branch
    psh="git push"+" "+rsp+" "+branch
    sp.run(brnch)
    sp.run(psh)
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
    speak("Please tell me which file you want to restore")
    rstr=input("Enter the filename: ")
    restr="git restore"+" "+rstr
    sp.run(restr)

def repo():
    speak("Ok great seems so you have created a brand new repository let me help you")
    init()
    speak("Respository initialised lets add files now ")
    lfs()
    commit()
    push()

def stash():
    speak("I understand that you want to keep your workspace clean we got a solution for it")
    speak("what should be the temporary save named as ")
    with sr.Microphone() as source06:
        user06=rec.listen(source06)
        speak("performing temporary save")
    user06i=rec.recognize_google(user06)
    print(user06i)
    stsh="git stash save"+" "+user06i
    sp.run(stsh)

def stashapp():
    speak("Thats great that you are using stash feature")
    speak("Here is your list of stash")
    sp.run("git stash list")
    speak("Tell me the serial number of the stash and i will apply it for you")
    with sr.Microphone() as source07:
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
    
def install()
    sp.run("choco install git")
    speak("Please enter your username")
    usrm=input("Enter your username: ")
    speak("Please enter your email address")
    eml=input("Enter your email: ")
    usrcfg="git config --global user.name"+" "+usrm
    emlcfg="git config --global user.email"+" "+eml
    sp.run(usrcfg)
    sp.run(emlcfg)

    

    
main()
