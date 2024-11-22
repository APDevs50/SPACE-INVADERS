import tkinter as tk
import os
import threading
import time
import random
import sys
import subprocess
import ast


game_over = False
root = tk.Tk()
root.geometry("500x300")
root.resizable(False,False)
root.title("SPACE INVADERS")
logo = tk.PhotoImage(file=os.path.join(os.getcwd(),"logo.png"))
scores = []
score = 10
# Set the window's icon
root.iconphoto(True, logo)
canvas = tk.Canvas(root,bg="#000000",width=500,height=300)
canvas.pack()
class Scoreboard:
    def __init__(self):
        self.myself = canvas.create_text(60, 10, font=('F77 Minecraft Regular', -15, 'normal'), text=f"Score: {score}", fill="#00ff00")
        self.highscore_display = canvas.create_text(420, 10, font=('F77 Minecraft Regular', -15, 'normal'), text="", fill="#00ff00", justify='left')
        self.updateThread = threading.Thread(target=self.update)
        self.updateThread.daemon = True
        self.updateThread.start()

    def update(self):
        while True:
            canvas.itemconfig(self.myself, text=f"Score: {score}")
            self.update_highscore_display()
            time.sleep(0.1)

    def update_highscore_display(self):
        high = self.highscore()
        canvas.itemconfig(self.highscore_display, text=f"High Score: {high}")

    def highscore(self):
        high = 0
        if os.path.isfile(os.path.join(os.getcwd(), "SCORE.spaceinvaders")):
            with open("SCORE.spaceinvaders", 'r') as f:
                try:
                    scorets = f.readline().strip()
                    if scorets:
                        high = int(scorets)
                except Exception as e:
                    print(f"Error reading highscore: {e}")
        return high

    def update_highscore(self):
        high = self.highscore()
        if score > high:
            with open("SCORE.spaceinvaders", 'w') as f:
                f.write(str(score))




scorer = Scoreboard()
scorer.highscore()
class Player:
    def __init__(self):
        self.myself = tk.PhotoImage(file=os.path.join(os.getcwd(),"Player.png"))
        self.img = canvas.create_image(100,268,anchor=tk.NW,image=self.myself)
    def move_right(self,ev):
        curr_coords = canvas.coords(self.img)
        if curr_coords[0] + 10 >= 450:
            #print("ILLEGAL")
            return
        canvas.move(self.img, 10, 0)
        #print(self.whereami())
    def move_left(self,ev):
        curr_coords = canvas.coords(self.img)
        if curr_coords[0] - 10 <= 0:
            #print("ILLEGAL")
            return
        canvas.move(self.img, -10, 0)
        #print(self.whereami())
    def whereami(self):
        return canvas.coords(self.img)
player = Player()
class Bullet:
    def __init__(self):
        self.myclones = []
        self.blaster = []
        self.origx = []
        self.daemonThread = threading.Thread(target=self.ascend)
        self.daemonThread.daemon = True
        self.daemonThread.start()
    def shoot(self,ev):
        self.blaster.append(tk.PhotoImage(file=os.path.join(os.getcwd(),"Bullet.png")))
        self.origx.append(int(player.whereami()[0]+25))
        self.meid = canvas.create_image(self.origx[-1],255,anchor=tk.NW,image=self.blaster[-1])
        self.myclones.append(self.meid)
    def ascend(self):
        self.l1 = threading.Lock()
        self.l1.acquire()
        while True:
            if game_over == True:
                return
            for i in self.myclones:
                try:
                    if canvas.coords(i)[1] == 0:
                        canvas.delete(i)
                        self.todel = self.myclones.index(i)
                        self.myclones.remove(i)
                        del self.origx[self.todel]
                        del self.blaster[self.todel]
                    else:
                        canvas.move(i,0,-10)
                except:
                    #print("Crash averted")
                    continue
            time.sleep(0.05)
        self.l1.release()
    def whereamim(self):
        bulletcoords = []
        for i in self.myclones:
            bulletcoords.append(canvas.coords(i))
        return coords
    
class Enemy_bullet:
    def __init__(self):
        self.myselveswhowannakill = []
        self.origcoords = []
        self.img = tk.PhotoImage(file=os.path.join(os.getcwd(),"Bullet.png"))
    def spawn(self,x,y,whoshot):
        if whoshot == "green":
            self.keid = canvas.create_image(x+16,y+32,anchor=tk.NW,image=self.img)
            self.myselveswhowannakill.append(self.keid)
        else:
            self.keid = canvas.create_image(x+24,y+32,anchor=tk.NW,image=self.img)
            self.myselveswhowannakill.append(self.keid)
    def descend(self):
        while True:
            if game_over == True:
                return
            for i in self.myselveswhowannakill:
                try:
                    if canvas.coords(i)[1] >= 300:
                        canvas.delete(i)
                        self.myselveswhowannakill.remove(i)
                        #print("DEL")
                    else:
                        canvas.move(i,0,10)
                        #print("GO!")
                    #print("Something")
                except Exception as e:
                    #print(f"Crashpad: {e}")
                    continue
            time.sleep(0.05)

alien_revenge = Enemy_bullet()
daethro = threading.Thread(target=alien_revenge.descend)
daethro.daemon = True
daethro.start()
            
            
            
        
class Alien:
    def __init__(self):
        self.myselves = []
        self.origcoords = []
        self.finales = []
        self.x = 100
        self.y = 100
        self.num = 0   # Alien movement speed
        self.currentimage = 1
        self.daemonThreade = threading.Thread(target=self.move_aliens_left)
        self.daemonThreade.daemon = True
        self.daemonThreade.start()

    def create(self):
        for i in range(18):
            self.switch = tk.PhotoImage(file=os.path.join(os.getcwd(), "Green_Alien_Frame_2.png"))
            self.qorig = tk.PhotoImage(file=os.path.join(os.getcwd(), "Green_Alien_Frame_1.png"))
            self.myselves.append(tk.PhotoImage(file=os.path.join(os.getcwd(), "Green_Alien_Frame_1.png")))
            self.origcoords.append([self.x, self.y])
            self.ceid = canvas.create_image(self.origcoords[i][0], self.origcoords[i][1], anchor=tk.NW, image=self.myselves[-1])
            self.finales.append(self.ceid)
            if self.x > 400:  # Create aliens in rows
                self.x = 100
                self.y += 40
                continue
            self.x += 40
    def animate(self):
        for i in self.finales:
            if self.currentimage == 1:
                canvas.itemconfig(i, image=self.switch)
            else:
                canvas.itemconfig(i, image=self.qorig)
                
        if self.currentimage == 1:
            self.currentimage = 2
        else:
            self.currentimage = 1
    def move_aliens_left(self):
        if game_over == True:
            return
        for i in self.finales:
            canvas.move(i,-10,0)
        self.animate()
        self.num += 1
        time.sleep(1)
        if self.num != 5:
            self.move_aliens_left()
        else:
            self.num = 0
            self.move_aliens_down('left')
    def move_aliens_down(self,mode):
        if game_over == True:
            return
        for i in self.finales:
            canvas.move(i,0,10)
        self.animate()
        time.sleep(1)
        if mode == 'left':
            self.move_aliens_right()
        else:
            self.move_aliens_left()

    def move_aliens_right(self):
        if game_over == True:
            return
        for i in self.finales:
            canvas.move(i,10,0)
        self.animate()
        self.num += 1
        time.sleep(1)
        if self.num != 5:
            self.move_aliens_right()
        else:
            self.num = 0
            self.move_aliens_down('right')
    def whereamij(self):
        aliencoords = []
        for i in self.finales:
            aliencoords.append(canvas.coords(i))

    def powerblast(self):
        if game_over == True:
            return
        global alien_revenge
        while True:
            try:
                shooter = random.choice(self.finales)
                coords = canvas.coords(shooter)
                #print("Someone Shot...")
                alien_revenge.spawn(coords[0],coords[1],"green")
            except:
                print("Error")
            finally:
                time.sleep(7)


enemies = Alien()
enemies.create()
enemiesthread = threading.Thread(target = enemies.powerblast)
enemiesthread.daemon = True
enemiesthread.start()
class Alien_Tenacity_1:
    def __init__(self):
        self.myselves = []
        self.origcoords = []
        self.finales = []
        self.x = 100
        self.y = 60
        self.num = 0   # Alien movement speed
        self.currentimage = 1
        self.daemonThreade = threading.Thread(target=self.move_aliens_left)
        self.daemonThreade.daemon = True
        self.daemonThreade.start()

    def create(self):
        for i in range(6):
            self.switch = tk.PhotoImage(file=os.path.join(os.getcwd(), "Blue_Alien_Frame_2.png"))
            self.qorig = tk.PhotoImage(file=os.path.join(os.getcwd(), "Blue_Alien_Frame_1.png"))
            self.myselves.append(tk.PhotoImage(file=os.path.join(os.getcwd(), "Blue_Alien_Frame_1.png")))
            self.origcoords.append([self.x, self.y])
            self.ceid = canvas.create_image(self.origcoords[i][0], self.origcoords[i][1], anchor=tk.NW, image=self.myselves[-1])
            self.finales.append(self.ceid)
            if self.x > 400:  # Create aliens in rows
                self.x = 100
                self.y += 40
                continue
            self.x += 60
    def animate(self):
        for i in self.finales:
            if self.currentimage == 1:
                canvas.itemconfig(i, image=self.switch)
            else:
                canvas.itemconfig(i, image=self.qorig)
                
        if self.currentimage == 1:
            self.currentimage = 2
        else:
            self.currentimage = 1
    def move_aliens_left(self):
        if game_over == True:
            return
        for i in self.finales:
            canvas.move(i,-10,0)
        self.animate()
        self.num += 1
        time.sleep(1)
        if self.num != 5:
            self.move_aliens_left()
        else:
            self.num = 0
            self.move_aliens_down('left')
    def move_aliens_down(self,mode):
        if game_over == True:
            return
        for i in self.finales:
            canvas.move(i,0,10)
        self.animate()
        time.sleep(1)
        if mode == 'left':
            self.move_aliens_right()
        else:
            self.move_aliens_left()

    def move_aliens_right(self):
        if game_over == True:
            return
        for i in self.finales:
            canvas.move(i,10,0)
        self.animate()
        self.num += 1
        time.sleep(1)
        if self.num != 5:
            self.move_aliens_right()
        else:
            self.num = 0
            self.move_aliens_down('right')
    def whereamij(self):
        aliencoords = []
        for i in self.finales:
            aliencoords.append(canvas.coords(i))
            
    def powerblast(self):
        if game_over == True:
            return
        global alien_revenge
        while True:
            try:
                shooter = random.choice(self.finales)
                coords = canvas.coords(shooter)
                #print("Someone Shot...")
                alien_revenge.spawn(coords[0],coords[1],"blue")
            except:
                print("Error")
            finally:
                time.sleep(6)
                
bluey = Alien_Tenacity_1()
bluey.create()
dd = threading.Thread(target=bluey.powerblast)
dd.daemon = True
dd.start()
class Alien_Tenacity_2:
    def __init__(self):
        self.myselves = []
        self.origcoords = []
        self.finales = []
        self.x = 100
        self.y = 20
        self.num = 0   # Alien movement speed
        self.currentimage = 1
        self.daemonThreade = threading.Thread(target=self.move_aliens_left)
        self.daemonThreade.daemon = True
        self.daemonThreade.start()

    def create(self):
        for i in range(6):
            self.switch = tk.PhotoImage(file=os.path.join(os.getcwd(), "Red_Alien_Frame_2.png"))
            self.qorig = tk.PhotoImage(file=os.path.join(os.getcwd(), "Red_Alien_Frame_1.png"))
            self.myselves.append(tk.PhotoImage(file=os.path.join(os.getcwd(), "Red_Alien_Frame_1.png")))
            self.origcoords.append([self.x, self.y])
            self.ceid = canvas.create_image(self.origcoords[i][0], self.origcoords[i][1], anchor=tk.NW, image=self.myselves[-1])
            self.finales.append(self.ceid)
            if self.x > 400:  # Create aliens in rows
                self.x = 100
                self.y += 40
                continue
            self.x += 60
    def animate(self):
        for i in self.finales:
            if self.currentimage == 1:
                canvas.itemconfig(i, image=self.switch)
            else:
                canvas.itemconfig(i, image=self.qorig)
                
        if self.currentimage == 1:
            self.currentimage = 2
        else:
            self.currentimage = 1
    def move_aliens_left(self):
        if game_over == True:
            return
        for i in self.finales:
            canvas.move(i,-10,0)
        self.animate()
        self.num += 1
        time.sleep(1)
        if self.num != 5:
            self.move_aliens_left()
        else:
            self.num = 0
            self.move_aliens_down('left')
    def move_aliens_down(self,mode):
        if game_over == True:
            return
        for i in self.finales:
            canvas.move(i,0,10)
        self.animate()
        time.sleep(1)
        if mode == 'left':
            self.move_aliens_right()
        else:
            self.move_aliens_left()

    def move_aliens_right(self):
        if game_over == True:
            return
        for i in self.finales:
            canvas.move(i,10,0)
        self.animate()
        self.num += 1
        time.sleep(1)
        if self.num != 5:
            self.move_aliens_right()
        else:
            self.num = 0
            self.move_aliens_down('right')
    def whereamij(self):
        aliencoords = []
        for i in self.finales:
            aliencoords.append(canvas.coords(i))
            
    def powerblast(self):
        if game_over == True:
            return
        global alien_revenge
        while True:
            try:
                shooter = random.choice(self.finales)
                coords = canvas.coords(shooter)
                #print("Someone Shot...")
                alien_revenge.spawn(coords[0],coords[1],"red")
            except:
                print("Error")
            finally:
                time.sleep(5)
                
red_light = Alien_Tenacity_2()
red_light.create()
df = threading.Thread(target=red_light.powerblast)
df.daemon = True
df.start()
killer = Bullet()
class CollisionDetection:
    def detectbullet(self):
        try:
            global score
            for bullet in killer.myclones:
                box = canvas.bbox(bullet)
                if box is None:  # Check if the bullet exists
                    continue
                to_kill = canvas.find_overlapping(*box)
                for i in to_kill:
                    if i in enemies.finales:
                        canvas.delete(i)
                        canvas.delete(bullet)
                        killer.myclones.remove(bullet)
                        enemies.finales.remove(i)
                        score += 10
                        break
                    elif i in bluey.finales:
                        canvas.delete(i)
                        canvas.delete(bullet)
                        bluey.finales.remove(i)
                        killer.myclones.remove(bullet)
                        score += 20
                        break
                    elif i in red_light.finales:
                        canvas.delete(i)
                        canvas.delete(bullet)
                        killer.myclones.remove(bullet)
                        red_light.finales.remove(i)
                        score += 30
                        break
        except Exception as e:
            print("Error: (detectbullet)", e)                
    def detectdeath(self):
        try:
            global game_over
            sbox = canvas.bbox(player.img)
            l = canvas.find_overlapping(*sbox)
            if len(l) > 1:
                scorer.update_highscore()
                overlay = tk.Canvas(canvas, width=canvas.winfo_width(), height=canvas.winfo_height(), bg='black', highlightthickness=0)
                overlay.place(x=0, y=0)
                overlay.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2 - 30,
                        text="YOU LOST!", fill="#00ff00", font=("F77 Minecraft Regular", 36, 'bold'))
                restart_button = tk.Button(overlay, text="Restart", font=("F77 Minecraft Regular", 16, 'bold'), command=reset_game, bg="#000000", borderwidth=0, highlightthickness=0, fg="#00ff00")
                restart_button.place(x=200, y=150)

                game_over = True
                canvas.delete("all")
        except Exception as e:
            print("Error: (detectdeath)",e)
  
    def detectvictory(self):
        scorer.update_highscore() 
        global game_over
        if len(red_light.finales) == 0 and len(bluey.finales) == 0 and len(enemies.finales) == 0:
            self.next_wave()
          
    def detect_alien_hit(self):
        global game_over
        try:
            for i in enemies.finales:
                try:
                    if canvas.coords(i)[1] + 32 >= 268:
                        scorer.update_highscore()
                        game_over = True
                        overlay = tk.Canvas(canvas, width=canvas.winfo_width(), height=canvas.winfo_height(), bg='black', highlightthickness=0)
                        overlay.place(x=0, y=0)
                        overlay.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2 - 30,
                            text="YOU LOST!", fill="#00ff00", font=("F77 Minecraft Regular", 36, "bold"))
                        restart_button = tk.Button(overlay, text="Restart", font=("F77 Minecraft Regular", 16, 'bold'), command=reset_game, bg="#000000", borderwidth=0, highlightthickness=0, fg="#00ff00")
                        restart_button.place(x=200,y=150)
                except:
                    continue
            for i in red_light.finales:
                try:
                    if canvas.coords(i)[1] + 32 >= 268:
                        scorer.update_highscore()
                        game_over=True
                        overlay = tk.Canvas(canvas, width=canvas.winfo_width(), height=canvas.winfo_height(), bg='black', highlightthickness=0)
                        overlay.place(x=0, y=0)
                        overlay.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2 - 30,
                            text="YOU LOST!", fill="#00ff00", font=("F77 Minecraft Regular", 36, "bold"))
                        restart_button = tk.Button(overlay, text="Restart", font=("F77 Minecraft Regular", 16, 'bold'), command=reset_game, bg="#000000", borderwidth=0, highlightthickness=0, fg="#00ff00")
                        restart_button.place(x=200,y=150)
                except:
                    continue
            for i in bluey.finales:
                try:
                    if canvas.coords(i)[1] + 32 >= 268:
                        scorer.update_highscore()
                        game_over = True
                        overlay = tk.Canvas(canvas, width=canvas.winfo_width(), height=canvas.winfo_height(), bg='black', highlightthickness=0)
                        overlay.place(x=0, y=0)
                        overlay.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2 - 30,
                            text="YOU LOST!", fill="#00ff00", font=("F77 Minecraft Regular", 36, "bold"))
                        restart_button = tk.Button(overlay, text="Restart", font=("F77 Minecraft Regular", 16, 'bold'), command=reset_game, bg="#000000", borderwidth=0, highlightthickness=0, fg="#00ff00")
                        restart_button.place(x=200,y=150)
                except:
                    continue
        except Exception as e:
            print("Error: (detect_alien_hit)",e)
    def next_wave(self):
        global score, enemies, bluey

        # Display "Next Wave" message
        canvas.delete("all")
        canvas.create_text(250, 150, font=('F77 Minecraft Regular', -30, 'normal'), text="Next Wave", fill="#00ff00")
        root.update()
        time.sleep(2)

        # Reset the canvas
        canvas.delete("all")
        scorer.myself = canvas.create_text(60, 10, font=('F77 Minecraft Regular', -15, 'normal'), text=f"Score: {score}", fill="#00ff00")
        scorer.highscore_display = canvas.create_text(420, 10, font=('F77 Minecraft Regular', -15, 'normal'), text="", fill="#00ff00", justify='left')

        # Reinitialize game entities
        enemies = Alien()
        enemies.create()
        enemiesthread = threading.Thread(target=enemies.powerblast)
        enemiesthread.daemon = True
        enemiesthread.start()

        bluey = Alien_Tenacity_1()
        bluey.create()
        dd = threading.Thread(target=bluey.powerblast)
        dd.daemon = True
        dd.start()

        
        # Reset player position
        player.img = canvas.create_image(100, 268, anchor=tk.NW, image=player.myself)




collbot = CollisionDetection()
def check_if_collide():
    while True:
        if game_over == True:
            return
        collbot.detectbullet()
        collbot.detectdeath()
        collbot.detectvictory()
        collbot.detect_alien_hit()
        print("COLLIDE")
        time.sleep(0.05)
bulldetect = threading.Thread(target=check_if_collide)
bulldetect.daemon = True
bulldetect.start()
def reset_game():
        root.destroy()
        python_executable = sys.executable
        script_path = __file__  # This is the path to your script

        # Run the script using subprocess
        subprocess.run([python_executable, script_path], shell=False)
    
root.bind("<Right>", player.move_right)
root.bind("<Left>",player.move_left)
root.bind("<space>",killer.shoot)
root.mainloop()
