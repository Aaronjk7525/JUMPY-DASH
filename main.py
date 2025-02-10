import pgzrun
from pgzero.builtins import keyboard, keys
from platformer import *
import time

TILE_SIZE=18
ROWS= 18
COLS =18

WIDTH = TILE_SIZE*ROWS
HEIGHT = TILE_SIZE*COLS
TITLE="One piece" 

platforms=build("tiles3.csv",TILE_SIZE)
points=build("tiles4.csv",TILE_SIZE)


player= Actor("p_right")
player.bottomleft = (0,HEIGHT-TILE_SIZE)
player.velocity_x = 3
player.velocity_y = 0
player.jumping = False
player.alive = True
gravity = 1
jump_velocity = -10
over = False
WIN = False

def draw():
    screen.clear() 
    screen.fill("skyblue") 
    for platform in platforms:
        platform.draw()
    for point in points:
        point.draw()
    
    if player.alive:
        player.draw()
    else:
        # Display "GAME OVER" text when the player is not alive
        screen.draw.text("!!!GAME OVER!!!", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="red")

    if WIN:
        # Display "YOU WIN" text when the player wins
        screen.draw.text("YOU WIN!", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="green")

    

def update():
    global over,WIN,platforms,points
    if keyboard.LEFT and player.midleft[0] > 0: 
        player.x-=player.velocity_x
        player.image ="p_left"
        #if player collided with plateform
        if player.collidelist(platforms)!=-1:
            object=platforms[player.collidelist(platforms)]
            player.x = object.x + (object.width/2 + player.width/2 )

    elif keyboard.RIGHT and player.midright[0] < WIDTH: 
        player.x+=player.velocity_x
        player.image ="p_right"
        #if player collided with plateform
        if player.collidelist(platforms)!=-1:
            object=platforms[player.collidelist(platforms)]
            player.x = object.x - (object.width/2 + player.width/2 )


    #handles gravity
    player.y += player.velocity_y
    player.velocity_y += gravity
    #if player collided with platform
    if player.collidelist(platforms)!=-1:
        #get object tht player collided with
        object=platforms[player.collidelist(platforms)]
        if player.velocity_y>=0:
             player.y = object.y - (object.height/2 + player.height/2 )
             player.jumping = False 
        else:
             player.y = object.y + (object.height/2 + player.height/2 )
        player.velocity_y = 0


    # getting points
    for point in points:
        if player.colliderect(point)>0:
            points.remove(point)
    if len(points)==0:
        WIN = True
        over = True
        
        
def on_key_down(key):
    if key == keys.UP and not player.jumping:
        player.velocity_y = jump_velocity
        player.jumping = True
 
pgzrun.go()
