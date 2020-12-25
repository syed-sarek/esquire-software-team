from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ai import models
from django.db import connection 
import speech_recognition as sr
from django.http import JsonResponse

def index(request): 
    if request.is_ajax():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Please Speak: ")
            audio = r.listen(source)
        try:
            output = " " + r.recognize_google(audio, language="en")
            # output = " " + r.recognize_google(audio, language="bn")
        except sr.UnknownValueError:
            output = "Could not understand audio!"
        except sr.RequestError as e:
            output = "Could not connect with internet!"
        
        return JsonResponse(output,safe=False)

    return render(request, "index.html")

# Python program to translate 
# speech to text and text to speech 

# import pyttsx3 
 
# r = sr.Recognizer() 

# def SpeakText(command): 
	
# 	# Initialize the engine 
# 	engine = pyttsx3.init() 
# 	engine.say(command) 
# 	engine.runAndWait() 
	


# while(1):	 
	
# 	# Exception handling to handle 
# 	# exceptions at the runtime 
# 	try: 
		
# 		# use the microphone as source for input. 
# 		with sr.Microphone() as source2: 
			
# 			# wait for a second to let the recognizer 
# 			# adjust the energy threshold based on 
# 			# the surrounding noise level 
# 			r.adjust_for_ambient_noise(source2, duration=0.2) 
			
# 			#listens for the user's input 
# 			audio2 = r.listen(source2) 
			
# 			# Using ggogle to recognize audio 
# 			MyText = r.recognize_google(audio2) 
# 			MyText = MyText.lower() 

# 			print("Did you say "+MyText) 
# 			SpeakText(MyText) 
			
# 	except sr.RequestError as e: 
# 		print("Could not request results; {0}".format(e)) 
		
# 	except sr.UnknownValueError: 
# 		print("unknown error occured") 

