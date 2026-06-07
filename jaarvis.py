# importing phything libralies
import speech_recognition as r
import webbrowser
import pyttsx3
import datetime
import calendar


re = r.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)  
    engine.runAndWait()
    
if __name__ == "__main__":
    speak("hello sir")     
 
    while True: 
        try:
            with r.Microphone() as source:  
                print("listening...")
                audio = re.listen(source, phrase_time_limit=5)
                text = re.recognize_google(audio)
                print("You said:", text)
                
                command = text.lower()
                
                if "hey jarvis" in command:
                    speak("yes sir")
                elif "open youtube" in command:
                    webbrowser.open("https://youtube.com")
                elif "open google" in command:
                    webbrowser.open("https://google.com")
                elif "open facebook" in command:
                    webbrowser.open("https://facebook.com")
                elif "open twitter" in command:
                    webbrowser.open("https://twitter.com")
                elif "open instagram" in command:
                    webbrowser.open("https://instagram.com")
                elif "what is the date today" in command:  # 🌟 FIXED: Kept ONLY the clean words version
                    today = datetime.date.today()
                    clean_date = today.strftime("%B %d, %Y")
                    print(clean_date)
                    speak("Today's date is " + clean_date)
                elif "what is the day today" in command:
                    today = datetime.date.today()
                    day = calendar.day_name[today.weekday()]
                    print(day)
                    speak("Today is " + day)
                elif "stop" in command:
                    speak("jarvis signing off")
                    break 
                    
        except Exception as e:  # 🌟 FIXED: Aligned perfectly under 'try'
            print("Listening loop warning:", e)
                         