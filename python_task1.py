import pyttsx3
import os

#pyttsx3.speak("Welcome to my tools")
print("Hello Prachika This is menu-driven Program!")

while True:
	print("***************************************************************************************Which is the Program you want to open?**************************************************************************************", end=' \n ')
	p=input()
	
        #print(p)
	#os.system(p)


	if(("run" in p) or ("execute" in p))and ("Chrome" in p):
		os.system("chrome")

	elif (("run" in p) or ("execute" in p)) and (("Notepad" in p) or ("Editor" in p)):
		os.system("notepad")

	elif (("run" in p) or ("execute" in p)) and (("Player" in p) or ("Media" in p)):
		os.system("wmplayer")
	
	elif (("run" in p) or ("execute" in p)) and ("TeamViewer" in p):
		os.system("teamviewer")

	elif (("run" in p) or ("execute" in p)) and ("Firefox" in p):
		os.system("firefox")

	elif (("run" in p) or ("execute" in p))and (("Eclipse IDE" in p) or ("Run Java" in p)):
		os.system("eclipse")

	elif("exit" in p) or ("quit" in p):
		break

	else:
		print("dont support")