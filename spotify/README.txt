HELLO WELCOME TO THE SPOTI.py ALARMCLOCK!!!!

This version should work on mac

Preparation: 
Steps:
1. place a Spotify shortcut at the top right of your desktop
1.1 spotify for desktop should already be downloaded make sure the left column on spotify takes up the most space possible, so if not
already done, expand the left column!
2. open a terminal shell
3. install homebrew so copy and paste this: /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
4. run: brew doctor
5. install python so run: brew install python3
6. install pyautogui so run: pip3 install pyautogui
7. edit using your favourite text editor, notepad or whatever the run.sh file in the folder to change the path to find the folder to the proper one
8. now its time to do the hard stuff. so if u want you can use the launch daemon process. I personally don't have loads of success with it, so you can
also use the crontab to do it.
9. In terminal, run: crontab -e
10: time to do the fun stuff: so it should open in vi, that means
11: press I for insert, paste this on the first line: 00 6 * * * 00 6 * * * Users/withthe/appropriatepath/spotify/run.sh and
replace 00 with the desired minutes for the alarm, the 6 with hour, and the Users/withthe/appropriatepath/ with the path to this folder

You are almost done!!!

12: press escape to exit out of insert mode, and type: :wq and press enter to save and quit.
13: The alarm clock should now work! have a great listening time.

built to be adapted by the dumbest person, all that you need to change is the bash (.sh) file!
