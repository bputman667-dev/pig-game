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

player = canvas.create_rectangle(180, 250, 180+PLAYER_SIZE, 250+PLAYER_SIZE, fill="blue")

enemies =[]
power_enemies = []

alive = True


def move_left(event):
    canvas.move(player, -20, 0)

def move_right(event):
    canvas.move(player, 20, 0)

def move_up(event):
    canvas.move(player, 0, -20)

def move_down(event):
    canvas.move(player, 0, 20)

root.bind("a", move_left)

root.bind("d", move_right)

root.bind("w", move_up)

root.bind("s", move_down)

def spawn_enemy(type):
    global score
    if(type == "normal"):
        x = random.randint(0, WIDTH-ENEMY_SIZE)
        enemy = canvas.create_rectangle(x, 0, x+ENEMY_SIZE+(1+(score*0.1)), ENEMY_SIZE+(1+(score*0.1)), fill="cyan")
        enemies.append(enemy)
        print(enemies)
    elif(type == "powerful"):
        x = random.randint(0, WIDTH-ENEMY_SIZE*2)
        enemy = canvas.create_rectangle(x, 0, x+ENEMY_SIZE*2+(1+(score*0.2)), ENEMY_SIZE*2+(1+(score*0.2)), fill="cyan")
        power_enemies.append(enemy)
        print(power_enemies)

def run_game():
    global score
    global texts
    global alive
    global enemies
    global label
    stopper = 0
    stopper2 = 1
    #canvas.create_text(20, 20, text = str(score), fill = "white")

    if not alive:
        canvas.delete("all")
        canvas.create_text(WIDTH//2, HEIGHT//2, text = "GAME OVER", fill="white")
    if alive:
        random_roll = random.randint(1,60)
        if(random_roll == 1 or random_roll == 2 or random_roll == 3) and stopper < 20 and stopper2==1:
            for i in range(1):
                spawn_enemy("normal")
                random_roll = 20
                stopper = stopper+5

        elif(random_roll == 4 and score > 15):
            spawn_enemy("powerful")
            random_roll = 20
            stopper = stopper+10
        
        if(stopper >= 20 or stopper2 == 2):
            stopper = stopper - 1
            stopper2 = 2
        if(stopper == 0):
            stopper2 = 1
        
        for enemy in enemies:
            canvas.move(enemy, 0, 10)

            if canvas.bbox(enemy) and canvas.bbox(player):
                ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
                px1, py1, px2, py2 = canvas.bbox(player)

                if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                    #alive = False
                    pass
            if canvas.bbox(enemy)[1] > HEIGHT:
                score = score+1
                label.config(text = str(score))
                
                enemies.remove(enemies[0])
        for enemy in power_enemies:
            canvas.move(enemy, 0, 15+(1+((score-15)*0.1)))

            if canvas.bbox(enemy) and canvas.bbox(player):
                ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
                px1, py1, px2, py2 = canvas.bbox(player)

                if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                    #alive = False
                    pass
            if canvas.bbox(enemy)[1] > HEIGHT:
                score = score+5
                label.config(text = str(score))
                
                power_enemies.remove(power_enemies[0])
            
    root.after(50, run_game)

label = tk.Label(root, text = str(score))
label.pack()
run_game()
root.mainloop()

