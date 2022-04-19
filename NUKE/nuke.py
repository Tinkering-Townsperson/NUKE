import pyinputplus as pyip
import sys, animation, playsound, time, os, threading

#print(os.get_terminal_size())
#print(sys.argv)
city = sys.argv[1]
country = sys.argv[2]
place_to_nuke = (city + ", " + country).upper()
nuke = ("=>", "-=>", "--=>", "---=>", "----=>")
def sumting():
    playsound.playsound("/Users/AfterNoonPM/NUKE/assets/nuke.wav")
@animation.wait(nuke, color="red")
def s():
    time.sleep(5.647)
sound=threading.Thread(target=sumting)

print("SO YOU WANT TO NUKE " + place_to_nuke + ", HUH?")
print("FIRST U MUST ENTER DA PASSWORD!")
pswd = pyip.inputPassword()
if pswd == "bruh":
    print("DROPPING NUKE ON " + place_to_nuke + "!!!")
    sound.start()
    s()
else:
    print("INCORRECT PASSWORD!!! NOW YOU WILL BE NUKED!!!")
