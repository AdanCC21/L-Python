import pgzrun

WIDTH = 800
HEIGHT = 600

car1 = Actor('carro1')
car1.pos = 50, HEIGHT // 3

car2 = Actor('carro2')
car2.pos = 50, 2 * HEIGHT // 3

goal_x = 750

winner = None

def draw():
    screen.clear()
    screen.blit('fondoNegro', (0, 0))
    car1.draw()
    car2.draw()
    screen.draw.line((goal_x, 0), (goal_x, HEIGHT), 'white')
    if winner:
        screen.draw.text(winner, center=(WIDTH//2, HEIGHT//2), fontsize=50, color='white')

def on_key_down(key):
    global winner
    if winner is None and key == keys.UP:
        car1.x += 35
        check_winner()

def on_mouse_down(pos):
    global winner
    if winner is None:
        car2.x += 35
        check_winner()

def check_winner():
    global winner
    if car1.x >= goal_x:
        winner = "Gano el carro1"
    elif car2.x >= goal_x:
        winner = "Gano el carro2"
    
    if winner:
        print(winner)
        exit()

pgzrun.go()
