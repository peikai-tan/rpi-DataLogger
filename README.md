# Raspberry Pi Sense Hat Data Logger

## Auto-start
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/ (Option 4)
1. Place dataGen.py at a any convenient location. (e.g ~/Documents/dataGen.py)
2. Create dataGen.service in /usr/lib/systemd/system with the following contents  
```
[Unit]  
Description=Activity Tracker  
WantedBy=multi-user.target  
  
[Service]  
Type=simple  
WorkingDirectory=<absolute/path/to/>dataGen.py
ExecStart=/usr/bin/python3 <absolute/path/to>/dataGen.py  
```
3. Enable the service  
`sudo systemctl enable dataGen.service`
4. Reboot

## Setup Instructions
Enter the function you need in line 43: ```data = <ENTER YOUR FUNCTION HERE>```  
This will allow you to get your specific values from the sensehat.

Refer to the sense-hat api for the different methods you can call.  
https://pythonhosted.org/sense-hat/api/

Remember to change the other commented lines too.
These are all labeled in the python file.

## Operating Instructions
- Turn on the Pi
- Choose your activity using the joystick. s = start, e = exit
- Start the recording by clicking on the joystick. (LED grid will turn red)
- Proceed to do the activity
- End the recording by clicking on the joystick. (LED grid will turn blank)
- Program will restart to allow you to start a new track [Repeat as many times as you'd like]
- Select "e" to exit
- The data files will can be found in the same folder as your dataGen.py file. 

## Deletion
1. Disable the service
`sudo systemctl disable dataGen.service`
2. Delete dataGen.service file from /usr/lib/systemd/system/
3. Reboot
