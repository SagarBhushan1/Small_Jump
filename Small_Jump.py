import pygame
import sys
from pygame.constants import FULLSCREEN, KEYDOWN, SRCCOLORKEY, WINDOWHIDDEN
import random

pygame.init()
SCREENWIDTH ,SCREENHEIGHT = 700,450
FPS = 60


FPSCLOCK = pygame.time.Clock()
Window=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Small Jump")
Score = 0 
Hi_Score = 0
SKY_COLOR = (135,206,235) 

# ---------------player image import  --------------------
player_1=pygame.transform.smoothscale(pygame.image.load("images/player/1.png"),(25,25))
player_2=pygame.transform.smoothscale(pygame.image.load("images/player/2.png"),(28,25))

cloued_img=pygame.transform.smoothscale(pygame.image.load("images/cloued1.png"),(70,40))

button_B_blue= pygame.transform.smoothscale(pygame.image.load("images/button/button_blue.png"),(200,60))
Bottom_Bar= pygame.transform.smoothscale(pygame.image.load("images/Bottom_bar.png"),(40,10))

cuser_img1=pygame.transform.smoothscale(pygame.image.load("images/Mouse_curser1.png"),(25,15))
cuser_img=pygame.transform.smoothscale(pygame.image.load("images/Mouse_curser.png"),(20,20))
nidle_img=pygame.transform.smoothscale(pygame.image.load("images/nidle.png"),(50,25))

jump_sound = pygame.mixer.Sound("audios/jump.wav")
click_sound = pygame.mixer.Sound("audios/click.wav")
hit_sound = pygame.mixer.Sound("audios/hit.wav")

# pygame.mixer.music.stop()     <-----______---______-----> is use to stop all mugic play in baground |

def text(size,mass,color,x_pos,y_pos):
    sss=pygame.font.Font("ARCADEPI.TTF",size)
    text=sss.render(mass,True,color)
    Window.blit(text,(x_pos,y_pos))

def welcome_screen ():
    i=0
    for k in range(150,235):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
        userInput = pygame.key.get_pressed()
        Window.fill((250-k,250-k,250-k))
        text(75,"SMALL",(151,127,215),SCREENWIDTH/2-140,SCREENHEIGHT/2-100)
        text(75,"JUMP",(151,127,215),SCREENWIDTH/2-115,SCREENHEIGHT/2-30)
        text(20,"Loding...",(151,127,215),SCREENWIDTH/2-50,(SCREENHEIGHT/10)*9)
        pygame.draw.rect(Window,(18+(k/2),35+(k/2),1+(k/2)),(0,SCREENHEIGHT-20,(SCREENWIDTH/50)*i,SCREENHEIGHT))
        i+=0.6
        pygame.display.update()
        FPSCLOCK.tick(30)

def Game_over_Screen():
    pygame.mouse.set_visible(False)
    Player_X = SCREENWIDTH/2
    Player_Y = 390-25
    In_box = False
    jump_count = 15
    jump_count_is = 15
    left_click, right_click = False,False
    I = 0 
    J = 0
    while True:
        Mouse_posX , Mouse_posY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if (Mouse_posX>=100 and Mouse_posX<=300) and (Mouse_posY>=390 and Mouse_posY<=450):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        left_click = True
                    if event.button ==3:
                        right_click = True
                if left_click == True or right_click == True:
                    click_sound.play()
                    pygame.time.delay(300)
                    return
            if (Mouse_posX>=400 and Mouse_posX<=600) and (Mouse_posY>=390 and Mouse_posY<=450):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        left_click = True
                    if event.button ==3:
                        right_click = True
                if left_click == True or right_click == True:
                    click_sound.play()
                    pygame.time.delay(300)
                    pygame.quit()
                    sys.exit()
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_RETURN] or userInput[pygame.K_SPACE]:
            click_sound.play()
            pygame.time.delay(300)
            return
        Window.fill(SKY_COLOR)
        if userInput[pygame.K_p]:
            print(Mouse_posX,Mouse_posY)
        Window.fill(SKY_COLOR)
        Window.blit(cloued_img,(-30,100))
        Window.blit(cloued_img,(230,130))
        Window.blit(cloued_img,(650,117))
        Window.blit(cloued_img,(435,245))
        Window.blit(cloued_img,(-20,380))
        Window.blit(cloued_img,(280,385))
        Window.blit(cloued_img,(475,10))

        pygame.draw.rect(Window,(40,40,40),(0,390,SCREENWIDTH,5))

        text(25,f"Hi Score : {Hi_Score}",(151,127,215),15,15)

        Window.blit(button_B_blue,(100,390))
        text(33,"Play",(151,127,215),160,399)

        Window.blit(button_B_blue,(400,390))
        text(33,"Quit",(151,127,215),460,403)


        if Mouse_posX>=0 and Mouse_posY>=380:
            Window.blit(cuser_img,(Mouse_posX-5,Mouse_posY-1))
        else:
            Window.blit(cuser_img1,(Mouse_posX-5,Mouse_posY))
        
        if Mouse_posY<=390:
            if Mouse_posX<=675:
                Player_X = Mouse_posX
        if jump_count==15:
            jump_sound.play()
        if jump_count>=-(jump_count_is):
            neg = 1
            if jump_count< 0:
                neg = -1
            Player_Y -= (jump_count ** 2)/8* neg
            jump_count -= 0.5
        else :
            jump_count = jump_count_is

        if jump_count>=8 or jump_count<=-8:
            Window.blit(player_1,(Player_X,Player_Y))
        else:
            Window.blit(player_2,(Player_X-2,Player_Y))

        if (Mouse_posX>=100 and Mouse_posX<=300) and (Mouse_posY>=390 and Mouse_posY<=450):
            if left_click == True or right_click == True:
                return
        if (Mouse_posX>=400 and Mouse_posX<=600) and (Mouse_posY>=390 and Mouse_posY<=450):
            if left_click == True or right_click == True:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        FPSCLOCK.tick(50)

def main_game():
    pygame.mouse.set_visible(False)
    global Score
    global Hi_Score

    jump_count = 15
    jump_count_is = 15

    B1_X,B1_Y = random.randint(50,450),400
    B2_X,B2_Y = random.randint(50,450),320
    B3_X,B3_Y = random.randint(50,450),230
    B4_X,B4_Y = random.randint(50,450),140
    B5_X,B5_Y = random.randint(50,450),60

    C1_X,C1_Y = -30,0
    C2_X,C2_Y = 230,75
    C3_X,C3_Y = 650,150
    C4_X,C4_Y = 435,225
    C5_X,C5_Y = -20,300
    C6_X,C6_Y = 500,380

    Player_Y = 400
    Player_X = 400

    JUMP = True

    I = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Score = 0
                pygame.quit()
                sys.exit()
        userInput = pygame.key.get_pressed()
        mouse_pos_x,mouse_pos_y = pygame.mouse.get_pos()
        Player_X = mouse_pos_x
        Window.fill(SKY_COLOR)
        if Score>Hi_Score:
            Hi_Score = Score

        Window.blit(cloued_img,(C1_X,C1_Y))
        Window.blit(cloued_img,(C2_X,C2_Y))
        Window.blit(cloued_img,(C3_X,C3_Y))
        Window.blit(cloued_img,(C4_X,C4_Y))
        Window.blit(cloued_img,(C5_X,C5_Y))
        Window.blit(cloued_img,(C6_X,C6_Y))

        if JUMP == False :
            if (Player_X >= B1_X-15 and Player_X+25 <= B1_X+15+Bottom_Bar.get_width()) and (Player_Y+25 <= B1_Y+Bottom_Bar.get_height() and Player_Y+25 >= B1_Y-10):
                jump_count = 15
                JUMP = True
                Player_Y  = B1_Y-25
                Window.blit(player_1,(Player_X,Player_Y))
                jump_sound.play()

            elif (Player_X >= B2_X-15 and Player_X+25 <= B2_X+15+Bottom_Bar.get_width()) and (Player_Y+25 <= B2_Y+Bottom_Bar.get_height() and Player_Y+25 >= B2_Y-10):
                jump_count = 15
                JUMP = True
                Player_Y  = B2_Y-25
                Window.blit(player_1,(Player_X,Player_Y))
                jump_sound.play()

            elif (Player_X >= B3_X-15 and Player_X+25 <= B3_X+15+Bottom_Bar.get_width()) and (Player_Y+25 <= B3_Y+Bottom_Bar.get_height() and Player_Y+25 >= B3_Y-10):
                jump_count = 15
                JUMP = True
                Player_Y  = B3_Y-25
                Window.blit(player_1,(Player_X,Player_Y))
                jump_sound.play()

            elif (Player_X >= B4_X-15 and Player_X+25 <= B4_X+15+Bottom_Bar.get_width()) and (Player_Y+25 <= B4_Y+Bottom_Bar.get_height() and Player_Y+25 >= B4_Y-10):
                jump_count = 15
                JUMP = True
                Player_Y  = B4_Y-25
                Window.blit(player_1,(Player_X,Player_Y))
                jump_sound.play()
            elif (Player_X >= B5_X-15 and Player_X+25 <= B5_X+15+Bottom_Bar.get_width()) and (Player_Y+25 <= B5_Y+Bottom_Bar.get_height() and Player_Y+25 >= B5_Y-10):
                jump_count = 15
                JUMP = True
                Player_Y  = B5_Y-25
                Window.blit(player_1,(Player_X,Player_Y))
                jump_sound.play()
        
        Window.blit(Bottom_Bar,(B1_X,B1_Y))
        Window.blit(Bottom_Bar,(B2_X,B2_Y))
        Window.blit(Bottom_Bar,(B3_X,B3_Y))
        Window.blit(Bottom_Bar,(B4_X,B4_Y))
        Window.blit(Bottom_Bar,(B5_X,B5_Y))

        if B1_Y>450:
            B1_X,B1_Y = random.randint(50,550),-60
        if B2_Y>450:
            B2_X,B2_Y = random.randint(50,550),-60
        if B3_Y>450:
            B3_X,B3_Y = random.randint(50,550),-60
        if B4_Y>450:
            B4_X,B4_Y = random.randint(50,550),-60
        if B5_Y>450:
            B5_X,B5_Y = random.randint(50,550),-60
        
        if C1_Y>450:
            C1_X,C1_Y = random.randint(-40,660),-60
        if C2_Y>450:
            C2_X,C2_Y = random.randint(-40,660),-60
        if C3_Y>450:
            C3_X,C3_Y = random.randint(-40,660),-60
        if C4_Y>450:
            C4_X,C4_Y = random.randint(-40,660),-60
        if C5_Y>450:
            C5_X,C5_Y = random.randint(-40,660),-60
        if C6_Y>450:
            C6_X,C6_Y = random.randint(-40,660),-60

        if JUMP == True :
            if Player_Y<=150:
                B1_Y+= int((jump_count ** 2)/10)
                B2_Y+= int((jump_count ** 2)/10)
                B3_Y+= int((jump_count ** 2)/10)
                B4_Y+= int((jump_count ** 2)/10)
                B5_Y+= int((jump_count ** 2)/10)
                C1_Y += int((jump_count ** 2)/10)/3
                C2_Y += int((jump_count ** 2)/10)/3
                C3_Y += int((jump_count ** 2)/10)/3
                C4_Y += int((jump_count ** 2)/10)/3
                C5_Y += int((jump_count ** 2)/10)/3
                C6_Y += int((jump_count ** 2)/10)/3
                Score += int((jump_count ** 2)/10)
            else:
                if jump_count>=-(jump_count_is):
                    Player_Y -= int((jump_count ** 2)/10)
            
            if jump_count<1:
                JUMP = False
            jump_count -= 0.5
        else:
            Player_Y += int((jump_count ** 2)/10)
            jump_count += 0.5

        if jump_count>=12:
            Window.blit(player_1,(Player_X,Player_Y))
        else :
            Window.blit(player_2,(Player_X,Player_Y))

        text(25,f"SCORE : {Score}",(151,127,215),5,5)

        for i in range(0,700,50):
            Window.blit(nidle_img,(i,430))

        if Player_Y+25 >= 428:
            hit_sound.play()
            text(50,"GAME OVER",(151,127,215),175,200)
            pygame.display.update()
            pygame.time.delay(800)
            Score = 0
            return
        Window.blit(cuser_img1,(mouse_pos_x,mouse_pos_y-7))
        pygame.display.update()
        FPSCLOCK.tick(50)
        
welcome_screen()
while True:
    Game_over_Screen()
    main_game()