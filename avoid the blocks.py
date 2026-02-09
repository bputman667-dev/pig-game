#added large fast moving blocks that give more points for dodging
#added score counter
#added ball that gives 20 points if hit
#made player die if they leave the screen
#added scaling over time
#added restart ability
#added a mean message if you get an OS error
#added blocks that move from the side

import tkinter as tk
import random

#declare constants

WIDTH = 400
HEIGHT = WIDTH*.75
PLAYER_SIZE = 30
ENEMY_SIZE = 20
score = 0
texts = []

root = tk.Tk()
root.title("avoid the blocks")
root.geometry(str(WIDTH) + "x" + str(int(HEIGHT)))

canvas = tk.Canvas(root, bg="black")
canvas.pack()

player = canvas.create_rectangle(180, 220, 180+PLAYER_SIZE, 220+PLAYER_SIZE, fill="blue")

enemies =[]
power_enemies = []
point_balls = []
side_blocks = []

alive = True

#defining movement functions for player
def move_left(event):
    canvas.move(player, -20, 0)

def move_right(event):
    canvas.move(player, 20, 0)

def move_up(event):
    canvas.move(player, 0, -20)

def move_down(event):
    canvas.move(player, 0, 20)

#binding movement functions to keys
root.bind("a", move_left)

root.bind("d", move_right)

root.bind("w", move_up)

root.bind("s", move_down)

#restart
def restart(event):
    global alive
    global enemies
    global power_enemies
    global point_balls
    global player
    global score
    canvas.delete("all")
    alive = True
    player = canvas.create_rectangle(180, 220, 180+PLAYER_SIZE, 220+PLAYER_SIZE, fill="blue")
    enemies = []
    power_enemies = []
    point_balls = []
    score = 0
    label.config(text = str(score))
root.bind("r", restart)



def spawn_enemy(type):
    global score
    #spawns normal enemy
    if(type == "normal"):
        x = random.randint(0, WIDTH-ENEMY_SIZE)
        enemy = canvas.create_rectangle(x, 0, x+ENEMY_SIZE+(1+(score*0.1)), ENEMY_SIZE+(1+(score*0.1)), fill="cyan")
        enemies.append(enemy)
        print(enemies)
    #spawns powerful enemy
    elif(type == "powerful"):
        x = random.randint(0, WIDTH-ENEMY_SIZE*2)
        enemy = canvas.create_rectangle(x, 0, x+ENEMY_SIZE*2+(1+(score*0.2)), ENEMY_SIZE*2+(1+(score*0.2)), fill="cyan")
        power_enemies.append(enemy)
        print(power_enemies)
    #spawns point ball
    elif(type == "point_ball"):
        x = random.randint(0+ENEMY_SIZE, WIDTH+ENEMY_SIZE)
        enemy = canvas.create_oval(x, 0, x+ENEMY_SIZE/2, ENEMY_SIZE/2, fill="red")
        point_balls.append(enemy)
        print(point_balls)
    elif(type == "side_block"):
        y = random.randint(0+ENEMY_SIZE, WIDTH+ENEMY_SIZE)
        enemy = canvas.create_rectangle(0, y, ENEMY_SIZE+(1+(score*0.1)), y+ENEMY_SIZE+(1+(score*0.1)), fill="cyan")
        side_blocks.append(enemy)
        print(side_blocks)
#main function
def run_game():
    global score
    global texts
    global alive
    global enemies
    global label
    stopper = 0
    stopper2 = 1
    #canvas.create_text(20, 20, text = str(score), fill = "white")

    #defines a game over
    if not alive:
        canvas.delete("all")
        canvas.create_text(WIDTH//2, HEIGHT//2, text = "GAME OVER", fill="white")
    #runs game if player is alive
    if alive:
        random_roll = random.randint(1,60)
        #spawns enemy 1/20 times
        if(random_roll == 1 or random_roll == 2 or random_roll == 3) and stopper < 20 and stopper2==1:
            for i in range(1):
                spawn_enemy("normal")
                random_roll = 20
                stopper = stopper+5
        #spawns powerful enemy 1/60 times if the score is over 15
        elif(random_roll == 4 and score > 15):
            spawn_enemy("power_enemy")
            random_roll = 20
            stopper = stopper+10
        #spawns point ball 1/60 times
        elif(random_roll == 5):
            spawn_enemy("point_ball")
        elif(random_roll == 30):
            spawn_enemy("side_block")
        #prevents too many enemy spawns in a row
        if(stopper >= 20 or stopper2 == 2):
            stopper = stopper - 1
            stopper2 = 2
        if(stopper == 0):
            stopper2 = 1
        #moves the normal enemies, if they pass the bottom, +1 point
        for enemy in enemies:
            canvas.move(enemy, 0, 10)

            if canvas.bbox(enemy) and canvas.bbox(player):
                ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
                px1, py1, px2, py2 = canvas.bbox(player)

                if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                    alive = False
                    pass
            if canvas.bbox(enemy)[1] > HEIGHT:
                score = score+1
                label.config(text = str(score))
                
                enemies.remove(enemies[0])
        #moves the power enemies, if they pass the bottom, +5 points, moves faster than normal enemy
        for enemy in power_enemies:
            canvas.move(enemy, 0, 15+(1+((score-15)*0.1)))

            if canvas.bbox(enemy) and canvas.bbox(player):
                ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
                px1, py1, px2, py2 = canvas.bbox(player)

                if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                    alive = False
                    pass
            if canvas.bbox(enemy)[1] > HEIGHT:
                score = score+5
                label.config(text = str(score))
                
                power_enemies.remove(power_enemies[0])
        #moves point balls, if it touches the player, +20 points. Moves faster than normal enemy
        for enemy in point_balls:
            canvas.move(enemy, 0, 15+(1+((score-15)*0.1)))
            if point_balls != []:
                try:
                    if canvas.bbox(enemy)[1] > HEIGHT:
                        canvas.delete(enemy)
                        point_balls.remove(point_balls[0])
                    elif canvas.bbox(enemy) and canvas.bbox(player):
                        ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
                        px1, py1, px2, py2 = canvas.bbox(player)

                        if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                            score = score+20
                            label.config(text = str(score))
                            point_balls.remove(point_balls[0])
                            canvas.delete(enemy)
                except TypeError:
                    pass
        for enemy in side_blocks:
            canvas.move(enemy, 10, 0)

            if canvas.bbox(enemy) and canvas.bbox(player):
                ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
                px1, py1, px2, py2 = canvas.bbox(player)

                if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                    alive = False
                    pass
            if canvas.bbox(enemy)[1] > WIDTH:
                score = score+1
                label.config(text = str(score))
                
                side_blocks.remove(side_blocks[0])
        #stops player from leaving the screen, with some leeway
        if canvas.bbox(player):
            px12, py12, px22, py22 = canvas.bbox(player)
            if px12 < -10 or px22 > WIDTH+10 or py12 < -10 or py22 > HEIGHT+10:
                alive = False
    #runs every 50 ms
    root.after(50, run_game)

try:
    label = tk.Label(root, text = str(score))
    label.pack()
    run_game()
    root.mainloop()
except OSError:
    print("whomp whomp, skill issue")
