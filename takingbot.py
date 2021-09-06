

import speech_recognition as sr

import pyttsx3#convert the audio to text
import pywhatkit#bundle of kitt of take the Q from user
import datetime
import wikipedia
import pyjokes#from jiokes (python joke)

listener=sr.Recognizer()#here we are listening
engine=pyttsx3.init()#converting the voice into text
voices=engine.getProperty('voices')#setting the perporty of Alexa(talking bot)
engine.setProperty('voice',voices[1].id)#0 for male and 1 for female voice


#defination for talk of bot
def talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
    
  #command taking from user as Voice
def take_command():
    try:
        with sr.Microphone() as source:#listening from the local system
            print('listening.....')
            voice=listener.listen(source)#saving the voice signal in voice variable
            command=listener.recognize_google(voice)#converting sound singnal in text
            command=command.lower()
            if 'alexa' in command:#waht yours bot name (AKANKSHA,alexa,disha like this)#checking whether the command in the bot
                command=command.replace('AKANKSHA','')
                print(command)
    except:
        print(" I am unable to listen..kindly speak again")
    return command
    
    
    
    
    
def run_bot():
    wh=['who','why','how','when','where','whome','what']
    whr=['treading','corona']
    mind="how Are You"
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M %S')
        talk("current time is "+time)
    elif "who" in command:
    
    
        person=command.replace('who','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif "which" in command:
        person=command.replace('which','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'update' in command:
        talk("ok!!! you are my creator so you can do")
    elif 'thanks' or 'Tahnk you' in command:
        talk("You Are Most Welcome !! stay safe in this covid situation")
    elif 'how Are You' in command:
        talk("Am Good,Thanks For Asking me,What about you?")
    
    
    
    else:
        talk("am  only a talking bot ...am not got")
    
while True:
     run_bot()
        