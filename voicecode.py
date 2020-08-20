import os
import subprocess
import pyttsx3

pyttsx3.speak("How can i help you ?")
while True:
	p=input()
	if ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or ("want" in p)  or ("need" in p) )  and ( ("notepad" in p) or ("note" in p)  or ("notes" in p) or ("write" in p) or ("editor" in p) or ("document" in p) ) ) ):
	  	pyttsx3.speak("enter the name for file")
	  	fil=input()
	  	os.system("notepad "+fil)

	elif( ("python" in p) or ("redhat" in p) or ("linux" in p) or  ("future ready" in p)  or  ("iiec" in p) ) :
		os.system("chrome youtube.com/channel/UCtY-JhEZ3iPLtozWGgd2efQ")

	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)  )  and ( ("vlc" in p) ) ) ):
		os.system("vlc")	
	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)  )  and ( ("windows" in p) and ("player" in p) ) ) ):
		os.system("wmplayer")
	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)  )  and ( ("movies" in p) ) ) ):
		os.system("start mswindowsvideo:")	

	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)  or ("need" in p) or ("watch" in p) )  and ( ("video" in p) or ("videos" in p) or ("media" in p) ) ) ):
		pyttsx3.speak("do you want vlc media player, windows media player or Movies and Tv ?")
		choice=input()
		if "vlc" in choice:
	  	  os.system("vlc")
		elif "windows" in choice:
		  os.system("wmplayer")
		elif "movies" in choice:
		  os.system("start mswindowsvideo:")

	elif( ( ("open" in p) or  ("need" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("listen" in p) ) and ( ("music" in p) or  ("song" in p) or  ("songs" in p)  or  ("playlist" in p) )):
		pyttsx3.speak("do you want vlc , windows media player , or groove music ?")
		ch=input()
		if "windows" in ch:
	  	  os.system("vlc")
		elif "groove" in ch:
		  os.system("start mswindowsmusic:")


	elif( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("listen" in p) ) and ( ("settings" in p) or ("setting" in p))):
	  	os.system("start ms-settings:")

	elif "weather" in p :
	  	os.system("start bingweather:")

	elif ( ("clock" in p) or ("alarm" in p) or ("timer" in p)  or ("stopwatch" in p) ) :
	  	os.system("start ms-clock:")

	elif ( ("screenshot" in p) or ("snip" in p) or ("crop" in p) ) :
	  	os.system("SnippingTool")

	elif "calender" in p :
	  	os.system("start outlookcal:")

	elif  ( ("photo" in p) or ("pic" in p) or ("video" in p)  or ("camera" in p) ) :
	  	os.system("start microsoft.windows.camera:")

	elif "time" in p :
	  os.system("time /T")
	
	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p) or  ("check" in p) or ("need" in p) or ("write" in p) or  ("compose" in p) )  and ( ("mail" in p) or ("inbox" in p) or ("email" in p)  or ("gmail" in p) ) ) ):
	  	os.system("start outlookmail:")

	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or ("want" in p)  or ("need" in p))  and ( ("calculation" in p) or ("calculate" in p)  or ("calculator" in p) ) ) ):
	  	os.system("calc")
	
	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)   or ("need" in p))  and ( ("file" in p) or ("explorer" in p)  or ("computer" in p) or ("hard" in p) or ("disk" in p) or ("drive" in p) ) ) ):
	  	os.system("explorer")

	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)   or ("need" in p))  and ( ("word" in p) ) ) ):
	  	os.system("WINWORD")
	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)   or ("need" in p))  and ( ("ppt" in p) or ("power" in p) ) ) ):
	  	os.system("POWERPNT")
	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)   or ("need" in p))  and ( ("excel" in p) ) ) ):
	  	os.system("EXCEL")
	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)   or ("need" in p))  and ( ("outlook" in p) ) ) ):
	  	os.system("OUTLOOK")

	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p) or  ("want" in p)   or ("need" in p))  and (  ("draw" in p) or ("paint" in p) ) ) ):
	  	os.system("mspaint")

	elif ( ( ( ("open" in p) or ("start" in p) or ("execute" in p) or  ("launch" in p)  or  ("want" in p) or ("need" in p) )  and ( ("chrome" in p) or ("browser" in p) or ("website" in p) ) ) ):
	  	pyttsx3.speak("please enter the website you want to open")
	  	web=input()
	  	if('.com' in web) :
	    		os.system("chrome "+web)
	  	else:
	    		os.system("chrome "+web+".com")  
	
	elif "exit" in p or "close" in p or "terminate" in p or "bye" in p :
		pyttsx3.speak("Thanks for using my services. Please visit again")
		break
	else:
	 	pyttsx3.speak(" Please try different keyword ")










