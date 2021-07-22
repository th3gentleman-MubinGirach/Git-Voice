from _typeshed import IdentityFunction
import subprocess as sp
import speech_recognition as sr
import pyttsx3
from win32com.client import Dispatch
import os
import pyaudio

speak = Dispatch("SAPI.SpVoice").Speak
speak("Hello user welcome to the git tool by Mubin ggiraach")
rec = sr.Recognizer()
with sr.Microphone() as source:
    speak("Tell me what can i do for you")
    user1=rec.listen(source)
    speak("Ok wait")

user1i=rec.recognize_google(user1)
print(user1i)

if ("create" in user1i or "initialise" in user1i) :
    sp.run(["git", "init"], capture_output=True)
    
elif ("clone" in user1i or "download" in user1i):
    speak("please write the username followed by the repository name which you want to clone")
    print("example- th3gentleman-MubinGirach/test")
    user2=input("Enter the username/repositoryname: ")
    clone="git clone https://github.com/"+user2
    sp.run(clone)
    speak("Successfully cloned")

elif ("install" in user1i):
    speak("Installing git for you please wait")
    try:
        sp.run("choco install git -y")
    except:
        sp.run("dnf install git")
    else:
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



git init 
where u want to initialize 
git init - for current directory
git init remote-directory 

    
   
        
     

    
   


    
     
    
  
    

    

     
    
#if ("init"in useri):
    #os.system("git init")



