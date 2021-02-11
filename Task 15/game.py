#**************************************# Task 15: Game #**************************************#
# Dear person looking at the code,
# VS code has some issues using the pygame lib, due to this I used pycharm to program this file, I tried running
# the program in VS code and get the error where it can't find my pictures. I spoke to my onsite mentor (serge)
# and he said it's fine as long as it works and the code is correct. I'm sorry if you fall into the same issues
# as I was not able to find a fix for this issue. Thank you again and hope this will not get me marked down
#**************************************# Task 15: Game #**************************************#

import pygame
import random

#**************************************# Initialize #**************************************#

pygame.init() #This initializes the pygame lib

#**************************************# Screen Creation #**************************************#

screen_height = 680                                             #This is the applications boxes width and height
screen_width = 1040

screen = pygame.display.set_mode((screen_width, screen_height)) #This creates the game window (using the above size to create the window size)

#**************************************# Player Icons #**************************************#

player = pygame.image.load("player_icon.png")   #The following lines of code are just grabbing our pictures
                                                #We'll be using in our game. All of which are currently stored
enemy1 = pygame.image.load("enemy_icon1.png")   #In the root file where the program file is.
enemy2 = pygame.image.load("enemy_icon2.png")
enemy3 = pygame.image.load("enemy_icon3.png")


prize = pygame.image.load("prize.png")

#**************************************# Player Icon Sizes #**************************************#

player_height = player.get_height()     #Here we just get the image height
player_width = player.get_width()       #Here we get the image width

#**************************************# Enemy Icon Sizes #**************************************#

enemy1_height = enemy1.get_height()     #We get the image height
enemy1_width = enemy1.get_width()       #Get get the image width

enemy2_height = enemy2.get_height()     #Same as the above statments and will follow through for the rest of the statments
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

#**************************************# Prize Icon Sizes #**************************************#

prize_height = prize.get_height()
prize_width = prize.get_width()

#**************************************# Starting Positions #**************************************#

player_x_position = 0          #Here we set the players starting position (0,0 being the top left)
player_y_position = 0

#**************************************# Enemy Position #**************************************#

enemy1_x_position =  random.randint(0, screen_width - enemy1_width)     #All the code below uses random string
enemy1_y_position =  random.randint(0, screen_height - enemy1_height)   #(all starting at 0 and have a max of
                                                                        #What the screen width/height is)
enemy2_x_position =  random.randint(0, screen_width - enemy2_width)     #It will then randomly place them
enemy2_y_position =  random.randint(0, screen_height - enemy1_height)   #on the screen.

enemy3_x_position =  random.randint(0, screen_width - enemy3_width)
enemy3_y_position =  random.randint(0, screen_height - enemy1_height)

#**************************************# Prize Position #**************************************#

prize_x_position = random.randint(0, screen_width - prize_width)    #Same as the enemy spawn points, we use
prize_y_position = random.randint(0, screen_height - prize_height)  #random functions to randomly place the
                                                                    #reward on the map.
#**************************************# Keys Used #**************************************#

key_up = False      #We have set all the keys to false as if they are 'True' our place will be constantly
key_down = False    #moving and not be able to move, these are changed to true when we push down the keys
key_left = False
key_right = False

#**************************************# Game Function #**************************************#

while 1: #We use the while statment so that the program is always running until we reach a point where it can close (such as hitting a monster, getting the prize or closing the game)

    screen.fill(0)  # Clears the screen.
    screen.blit(player, (player_x_position,player_y_position))  #The following lines take the picture of the
                                                                #character we want to draw and prints it at
    screen.blit(enemy1, (enemy1_x_position, enemy1_y_position)) #the position we placed the character. This
    screen.blit(enemy2, (enemy2_x_position, enemy2_y_position)) #means that we'll never not be able to see them
    screen.blit(enemy3, (enemy3_x_position, enemy3_y_position)) #unless it's a black image

    screen.blit(prize, (prize_x_position, prize_y_position))

    pygame.display.flip()                                       # This updates the screen so that the images load

# **************************************# Movement/Keys #**************************************#

    for event in pygame.event.get():

        if event.type == pygame.QUIT:   #This checks if a user closes the program, if they did it will
            pygame.quit()               #run this if statment and end the program (so that it does not
            exit(0)                     #run in the background)
                                        # This event checks if the user press a key down.

# **************************************# Keys Pushed down #**************************************#

        if event.type == pygame.KEYDOWN:    #This checks if we're pushing the key down

            if event.key == pygame.K_UP:  # This explain all the other ifs under this. If we push the up arrow
                key_up = True             # key, it will set the key_up to 'True' so that they move upwards
            if event.key == pygame.K_DOWN:# same goes for down, left and right.
                key_down = True
            if event.key == pygame.K_LEFT:
                key_left = True
            if event.key == pygame.K_RIGHT:
                key_right = True

# **************************************# Keys Lifted #**************************************#

        if event.type == pygame.KEYUP:      #This checks if the key is not being pressed
                                            #if it isn't we then set the movement to 'False'
            if event.key == pygame.K_UP:    #so that they stop moving.
                key_up = False
            if event.key == pygame.K_DOWN:
                key_down = False
            if event.key == pygame.K_LEFT:
                key_left = False
            if event.key == pygame.K_RIGHT:
                key_right = False

    # **************************************# Movement #**************************************#

    if key_up == True:              #This is the same for all the statment, if we pressed the up arrow key, it will move them up
        if player_y_position > 0:   #This checks if the player is at the border, and if they are they won't be able to move in that direction
            player_y_position -= 1  #The reason this is -1 is 0,0 is at the top left, so moving up more would take us into -1 which means any movement up would minus 1
    if key_down == True:
        if player_y_position < screen_height - player_width:  #The above statment (key_up == True) is the same for this, please refer to that
            player_y_position += 1
    if key_left == True:
        if player_x_position > 0:
            player_x_position -= 1
    if key_right == True:
        if player_x_position < screen_width - player_width:
            player_x_position += 1

# **************************************# Player hitbox #**************************************#
    playerBox = pygame.Rect(player.get_rect())     #Here we're creating the players hitbox so that the program knows when it's been hit or not

    playerBox.top = player_y_position              #The following updates the playerBox position to the player's position,
    playerBox.left = player_x_position             #in effect making the box stay around the player image.

# **************************************# Enemy's hitbox #**************************************#

    enemy_box1 = pygame.Rect(enemy1.get_rect())    #Refer to player hitbox documentation, the same function is
    enemy_box1.top = enemy1_y_position             #Used here.
    enemy_box1.left = enemy1_x_position

    enemy_box2 = pygame.Rect(enemy2.get_rect())
    enemy_box2.top = enemy2_y_position
    enemy_box2.left = enemy2_x_position

    enemy_box3 = pygame.Rect(enemy3.get_rect())
    enemy_box3.top = enemy3_y_position
    enemy_box3.left = enemy3_x_position

# **************************************# prize hitbox #**************************************#

    prizeBox = pygame.Rect(enemy1.get_rect())   #Refer to player hitbox documentation, the same function is
    prizeBox.top = prize_y_position             #Used here.
    prizeBox.left = prize_x_position
    # Test collision of the boxes:

# **************************************# hitbox collision (enemy) #**************************************#

    if playerBox.colliderect(enemy_box1) or playerBox.colliderect(enemy_box2) or playerBox.colliderect(enemy_box3): #This checks if the players hitbox touched any of the enemies hitboxes

        print("You lose!") #If we did collide we'll print the "you lose" message

        pygame.quit()      #The program will then quit out
        exit(0)

# **************************************# hitbox interaction (prize) #**************************************#

    if playerBox.colliderect(prizeBox): #If our player collides with the prize box this function will run
        print("You win!")               #Then it will print out "you win!" and then the program will close

        pygame.quit()
        exit(0)

# **************************************# enemy movement #**************************************#

    enemy1_x_position -= 0.15   #Each of these is telling the enemies which direction they should move and at what speed

    enemy2_y_position -= 0.15

    enemy3_x_position -= 0.15   #Enemy 3 will move in a diagonal direction as it moves on both the
    enemy3_y_position -= 0.15   # X and Y positions.

    # **************************************# End of code :) #**************************************#