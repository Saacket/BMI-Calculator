def speak(str):
 from win32com.client import Dispatch
 speak = Dispatch("SAPI.SpVoice")
 speak.Speak(str)

if __name__ == '__main__':



 Height=float(input(speak("Enter your height in centimeters: ")))

Weight=float(input(speak("Enter your Weight in Kg: ")))
Height = Height/100
BMI=Weight/(Height*Height)
speak("your Body Mass Index is: ,BMI")
if(BMI>0):
	if(BMI<=16):
		speak("you are severely underweight")
	elif(BMI<=18.5):
		speak("you are underweight")
	elif(BMI<=25):
		speak("you are Healthy")
	elif(BMI<=30):
		speak("you are overweight")
	else: speak("you are severely overweight")
else:("enter valid details")