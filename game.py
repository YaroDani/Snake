import pygame
pygame.init()
import random
screen_width=500
screen_height=680
screen= pygame.display.set_mode((screen_width,screen_height))
red=(255,0,0)
green=(0,255,40)
black=(0,0,0)
dark_green=(0,200,0)
white=(255,255,255)
timer= pygame.time.Clock()

game_over=False

font = pygame.font.SysFont('Areal',20)
cell_size=20
snake_body=[]
snake_lenght=3


for i in range(snake_lenght):
    snake_body.append(pygame.Rect((screen_width/2)-(cell_size*i),screen_height/2,cell_size,cell_size))

snake_direction="right"
new_direction="right"

apple_position=pygame.Rect(random.randint(0,screen_width-cell_size),random.randint(0,screen_height-cell_size),cell_size,cell_size)

while not game_over:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT and snake_direction != "left":
                new_direction="right"
            if event.key==pygame.K_LEFT and snake_direction != "right":
                new_direction="left"
            if event.key==pygame.K_DOWN and snake_direction != "up":
                new_direction="down"
            if event.key==pygame.K_UP and snake_direction != "down":
                new_direction="up"
    snake_direction=new_direction
    if snake_direction=="up":
        snake_body.insert(0,pygame.Rect(snake_body[0].left,snake_body[0].top-cell_size,20,20))
    elif snake_direction=="down":
        snake_body.insert(0,pygame.Rect(snake_body[0].left,snake_body[0].top+cell_size,20,20))
    elif snake_direction=="left":
        snake_body.insert(0,pygame.Rect(snake_body[0].left-cell_size,snake_body[0].top,20,20))
    elif snake_direction=="right":
        snake_body.insert(0,pygame.Rect(snake_body[0].left+cell_size,snake_body[0].top,20,20))


    if snake_body[0].colliderect (apple_position):
        apple_position=pygame.Rect(random.randint(0,screen_width-cell_size),random.randint(0,screen_height-cell_size),cell_size,cell_size)
        snake_lenght+=1
    if len(snake_body)>snake_lenght:
        snake_body.pop()
    if snake_body[0].left<0 or snake_body[0].right>screen_width or snake_body[0].bottom>screen_height or snake_body[0].top<0:
        game_over=True
    for i in range (1,len(snake_body)):
        if snake_body[0].colliderect(snake_body[i]):
            game_over=True
    screen.fill(black)
    for i in range(len(snake_body)):
        if i == 0:
            pygame.draw.circle(screen,green,snake_body[i].center,cell_size/2)
        else :
            pygame.draw.circle(screen,green,snake_body[i].center,cell_size/2)
            pygame.draw.circle(screen,dark_green,snake_body[i].center,cell_size/4)
    pygame.draw.circle(screen,red,apple_position.center,cell_size/2)
    score=font.render(f"З'їджено яблук:{snake_lenght-3}",True,white)
    screen.blit(score,(10,10))
    pygame.display.update()
    timer.tick(5)