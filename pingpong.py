import pygame
import random
pygame.init()
gadget_pair=1
ch=int(input("Enter your choice for gadget pair"))
if ch==1:
    gadget_pair=1
elif ch==2:
    gadget_pair=2
WIDHT,HEIGHT=1000,600
pwn=pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("Pong_But_Better")
direction=[0,1]
angle=[0,1,2]
run=True
player1=player2=0
#color
BLUE=(0,0,255)
RED=(255,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
#for ball
radius=15
ball_x,ball_y = WIDHT/2-radius,HEIGHT/2-radius
ball_vel_x,ball_vel_y=0.7,0.7
dummyball_x,dummyball_y = WIDHT/2-radius,HEIGHT/2-radius
dummyball_vel_x,dummyball_vel_y=0.7,0.7
#paddle
paddle_width,paddle_height=20, 120
left_paddle_y = right_paddle_y =HEIGHT/2 - paddle_height/2
left_paddle_x,right_paddle_x=100 - paddle_width/2 , WIDHT -(100- paddle_width/2)
secondleft_paddle_y = secondright_paddle_y =HEIGHT/2 - paddle_height/2
secondleft_paddle_x,secondright_paddle_x=100 - paddle_width/2 , WIDHT -(100- paddle_width/2)
right_paddle_vel=left_paddle_vel=0
secondright_paddle_vel=secondleft_paddle_vel=0
#gadgets
left_gadget=right_gadget = 0
left_gadget_remaining=right_gadget_remaining =5 
#main loop

while run:
    pwn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run=False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
                secondright_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel= 0.9
                secondright_paddle_vel= 0.9

            if i.key == pygame.K_RIGHT and right_gadget_remaining >0:
                right_gadget=1
            if i.key == pygame.K_LEFT and right_gadget_remaining>0:
                right_gadget=2
            if i.key == pygame.K_w:
                left_paddle_vel= -0.9
                secondleft_paddle_vel= -0.9
            if i.key == pygame.K_s:
                left_paddle_vel= 0.9
                secondleft_paddle_vel= 0.9
            if i.key == pygame.K_d and left_gadget_remaining>0:
                left_gadget=1
            if i.key == pygame.K_a and left_gadget_remaining>0:
                left_gadget=2
        if i.type == pygame.KEYUP:
            secondright_paddle_vel=0
            right_paddle_vel=0
            secondleft_paddle_vel=0
            left_paddle_vel=0
    #ball movement control
    if ball_y<=0 + radius or ball_y >=HEIGHT-radius:
        ball_vel_y*= -1
    if dummyball_y<=0 + radius or dummyball_y >=HEIGHT-radius:
        dummyball_vel_y*= -1
    if ball_x >= WIDHT-radius:
        player1+=1
        ball_x,ball_y=WIDHT/2 - radius ,HEIGHT/2 -radius
        dummyball_x,dummyball_y=WIDHT/2 - radius ,HEIGHT/2 -radius
        secondleft_paddle_y=left_paddle_y
        second_right_paddle_y=right_paddle_y
        dir = random.choice(direction)
        ang=random.choice(angle)
        
        if dir==0:
            if ang==0:
               ball_vel_y,ball_vel_x=-1.4,0.7
               dummyball_vel_y,dummyball_vel_x=-1.4,0.7
            if ang==1:
                ball_vel_y,ball_vel_x = -0.7,0.7
                dummyball_vel_y,dummyball_vel_x = -0.7,0.7
            if ang==2:
                ball_vel_y,ball_vel_x=-0.7,1.4
                dummyball_vel_y,dummyball_vel_x=-0.7,1.4
        if dir==1:
            if ang==0:
               ball_vel_y,ball_vel_x=1.4,0.7
               dummyball_vel_y,dummyball_vel_x=1.4,0.7
            if ang==1:
                ball_vel_y,ball_vel_x = 0.7,0.7
                dummyball_vel_y,dummyball_vel_x = 0.7,0.7
            if ang==2:
                ball_vel_y,ball_vel_x=0.7,1.4
                dummyball_vel_y,dummyball_vel_x=0.7,1.4
        
        ball_vel_x*= -1
        dummyball_vel_x*= -1
    if ball_x <=0 + radius:
         player2+=1
         ball_x,ball_y=WIDHT/2 - radius ,HEIGHT/2 -radius
         dummyball_x,dummyball_y=WIDHT/2 - radius ,HEIGHT/2 -radius
         ball_vel_x,ball_vel_y=0.7,0.7
         dummyball_vel_x,dummyball_vel_y=0.7,0.7
         dir = random.choice(direction)
         ang=random.choice(angle)
        
         if dir==0:
            if ang==0:
               ball_vel_y,ball_vel_x=-1.4,0.7
               dummyball_vel_y,dummyball_vel_x=-1.4,0.7
            if ang==1:
                ball_vel_y,ball_vel_x = -0.7,0.7
                dummyball_vel_y,dummyball_vel_x = -0.7,0.7
            if ang==2:
                ball_vel_y,ball_vel_x=-0.7,1.4
                dummyball_vel_y,dummyball_vel_x=-0.7,1.4
         if dir==1:
            if ang==0:
               ball_vel_y,ball_vel_x=1.4,0.7
               dummyball_vel_y,dummyball_vel_x=1.4,0.7
            if ang==1:
                ball_vel_y,ball_vel_x = 0.7,0.7
                dummyball_vel_y,dummyball_vel_x = 0.7,0.7
            if ang==2:
                ball_vel_y,ball_vel_x=0.7,1.4
                dummyball_vel_y,dummyball_vel_x=0.7,1.4
        #paddle movement controls
    if left_paddle_y >= HEIGHT- paddle_height:
        left_paddle_y= HEIGHT-paddle_height
    if left_paddle_y <=0:
        left_paddle_y=0
    if right_paddle_y >= HEIGHT -paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <=0:
        right_paddle_y=0
    if secondleft_paddle_y >= HEIGHT- paddle_height:
        secondleft_paddle_y= HEIGHT-paddle_height
    if secondleft_paddle_y <=0:
        secondleft_paddle_y=0
    if secondright_paddle_y >= HEIGHT -paddle_height:
        secondright_paddle_y = HEIGHT - paddle_height
    if secondright_paddle_y <=0:
        secondright_paddle_y=0
    #paddle collision
    #left paddle
    if secondleft_paddle_y == left_paddle_y:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
           if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
              ball_x=left_paddle_x + paddle_width
              dummyball_x=left_paddle_x + paddle_width
              ball_vel_x *= -1
              dummyball_vel_x *= -1
    if secondleft_paddle_y != left_paddle_y:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
           if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
              ball_x=left_paddle_x + paddle_width
              dummyball_x=left_paddle_x + paddle_width
              ball_vel_x *= -1
              dummyball_vel_x *= -1
        if secondleft_paddle_x <= ball_x <= secondleft_paddle_x + paddle_width:
           if secondleft_paddle_y <= ball_y <= secondleft_paddle_y + paddle_height:
              ball_x=secondleft_paddle_x + paddle_width
              dummyball_x=left_paddle_x + paddle_width
              ball_vel_x *= -1
              dummyball_vel_x *= -1
    #right paddle
    if secondright_paddle_y == right_paddle_y:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
          if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x=right_paddle_x 
            dummyball_x=right_paddle_x 
            ball_vel_x *= -1
            dummyball_vel_x *= -1
    if secondright_paddle_y != right_paddle_y:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
          if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x=right_paddle_x 
            dummyball_x=right_paddle_x 
            ball_vel_x *= -1
            dummyball_vel_x *= -1
        if secondright_paddle_x <= ball_x <= secondright_paddle_x + paddle_width:
          if secondright_paddle_y <= ball_y <= secondright_paddle_y + paddle_height:
            ball_x=right_paddle_x 
            dummyball_x=right_paddle_x 
            ball_vel_x *= -1
            dummyball_vel_x *= -1
    
    #gadgets in action
    if gadget_pair==1:
         if left_gadget==1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                   ball_x=left_paddle_x + paddle_width
                   ball_vel_x *= -3.5
                   dummyball_vel_x *= -3.5
                   left_gadget=0
                   left_gadget_remaining-=1
         elif left_gadget==2:
            left_paddle_y=ball_y
            left_gadget=0
            left_gadget_remaining-=1
         if right_gadget==1:
             if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x=right_paddle_x + paddle_width
                    ball_vel_x *= -3.5
                    dummyball_vel_x *= -3.52
                    right_gadget_remaining-=1
         elif right_gadget==2:
            right_paddle_y=ball_y
            right_gadget=0
            right_gadget_remaining-=1
    elif gadget_pair==2:
        if left_gadget==1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
              if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x=left_paddle_x + paddle_width
                dummyball_x=left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummyball_vel_x *= -1
                dummyball_vel_y *= -1
                left_gadget=0
                left_gadget_remaining-=1
        elif right_gadget == 2:
            secondleft_paddle_y = left_paddle_y +200
            left_gadget=0
            left_gadget_remaining -= 1
        if right_gadget==1:
             if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
               if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                   ball_x=right_paddle_x 
                   dummyball_x=right_paddle_x 
                   ball_vel_x *= -1
                   dummyball_vel_x *= -1
                   dummyball_vel_y*=-1
                   right_gadget=0
                   right_gadget_remaining -=1
        elif right_gadget ==2:
            secondright_paddle_y=right_paddle_y + 200
            right_gadget=0
            right_gadget_remaining -= 1    
            

    

    #movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    dummyball_x += dummyball_vel_x
    dummyball_y += dummyball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    secondleft_paddle_y += secondleft_paddle_vel
    secondright_paddle_y += secondright_paddle_vel
    
    #scoreboard
    font=pygame.font.SysFont('callibri',32)

    score_1=font.render("Player_1:"+str(player1),True,WHITE)
    pwn.blit(score_1,(25,25))
    score_2=font.render("Player_2:"+str(player2),True,WHITE)
    pwn.blit(score_2,(825,25))
    gadget_left_1=font.render("Gad left: "+str(left_gadget_remaining),True,WHITE)
    pwn.blit(gadget_left_1,(25,65))
    gadget_right_2=font.render("Gad left: "+str(right_gadget_remaining),True,WHITE)
    pwn.blit(gadget_right_2,(825,65))
    #OBJECT
    pygame.draw.circle(pwn,BLUE,(ball_x,ball_y),radius)
    pygame.draw.rect(pwn,RED,pygame.Rect(left_paddle_x,left_paddle_y,paddle_width,paddle_height))
    pygame.draw.rect(pwn,RED,pygame.Rect(right_paddle_x,right_paddle_y,paddle_width,paddle_height))

    #DummyBallSection
    pygame.draw.circle(pwn,BLUE,(dummyball_x,dummyball_y),radius)
    #second paddle
    pygame.draw.rect(pwn,RED,pygame.Rect(secondleft_paddle_x,secondleft_paddle_y,paddle_width,paddle_height))
    pygame.draw.rect(pwn,RED,pygame.Rect(secondright_paddle_x,secondright_paddle_y,paddle_width,paddle_height))
    if left_gadget==1:
        pygame.draw.circle(pwn,WHITE,(left_paddle_x+10,left_paddle_y+10),4)
    if right_gadget==1:
        pygame.draw.circle(pwn,WHITE,(right_paddle_x+10,right_paddle_y+10),4)
    #endscreen
    winning_font=pygame.font.SysFont('callibri',100)
    if player1>=10:
        pwn.fill(BLACK)
        endscreen=winning_font.render("PLAYER_1 WON !!!....",True,WHITE)
        pwn.blit(endscreen,(200,250))
    if player2>=10:
        pwn.fill(BLACK)
        endscreen=winning_font.render("PLAYER_2 WON !!!....",True,WHITE)
        pwn.blit(endscreen,(200,250))
    pygame.display.update()
    
