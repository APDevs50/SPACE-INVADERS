# Space Invaders
So, we all have seen space invaders in 90's arcades for sure. It was such an influential game! So I have successfully created this repository that is a space invaders game wrote using Python, compiled to `*.exe` using `pyinstaller`. It is made only using `tkinter` for **GUI**. It uses the `subprocess` module to launch a new instance in case you lose.<br><br>
**Here's What You Need To Know:**
+ **How To Install:**
  + To install the game (if you want to play or review it), please click on the green button saying "Code" and click "Download ZIP" in the dropdown that will appear. After that, extract the file. If you would like to go to play the previous version 1.0, go to the `archive` folder and select `Version 1`. Then double-click on the `Space-Invaders.exe` file to run the game. Same goes for other archived versions if no clear guideline is there.
  + **Specific Guideline for Version 2.0:** To install the second version, please follow the following:
      1. Install the file using the procedure mentioned
      2. Navigate to `Space-Invaders-v2.0.exe` and in that folder, right-click and install both the `*.ttf` files as they are essential fonts the game needs. Then play by double-clicking.
+ **How To Play The Game:**
  + Use the `left` and `right` arrow keys to move the player.<br><br>
    ![Left And Right Arrow Keys](https://www.alialkaheli.com/breakout/images/left_right_keys.png)<br><br>
    The player moves `10px` to the left or `10px` to the right on arrow key press. It uses `root.bind("<Left>",player.move_right())...` to move the player. Player cannot move outside the window.
    <br><br>![image](https://github.com/user-attachments/assets/d03052f4-1495-4e1e-a11f-839023ed4f90)<br><br>
  + Use the `spacebar` to shoot bullets
  + Don't get hit by enemy bullets
  + If you clear an entire swarm of aliens, the next wave will start shortly
+ **Errors:**
The Game can error and raise exceptions if not with its assets. Basically the game file and assets need to be in the same directory. The Python version of v2.0 may give many Tracebacks and Error messages to the console, but the game has the handlers required to catch them.
+ **Possible Bug Fix:**
I will be very grateful to see if the other waves can also have red aliens, as the red aliens got a bug into the wave system- collision detection won't work for them, so I removed them from the subsequent waves. I will be happy to improve this.
+ **Changelog:**
Here is the changelog of the application:
1. **Version 2.0 (Latest):** This version brought on some bug-fixes and new features originally not in Version 1.0 which I am happy to announce:
   + **Introduction Of Wave System:** Once you beat one swarm of aliens, another will come until you lose.
   + **Scoring:** The game has a scoring system and highscore saved in plaintext in a file called `score.spaceinvaders`, and can be hacked if someone put their own high score, which could be very high, into the file to trick the game into thinking that is their real high score. The game has no anti-cheat currently.
   + **Bug Fix:** The alien-moving-out-of-screen bug has been fixed.  
3. **Version 1.0 (Original):** This version was my first attempt at making a game like space invaders in Python compiled to a `*.exe` using `pyinstaller`. It ha only basic features and quite a few bugs patched in version 2:
   Version 1.0 Bugs:
   + If aliens move down without hitting the player, they will just keep moving down until the aliens are just out of the screen.
   + The game has a considerable lag
  





