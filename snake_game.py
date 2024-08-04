import pygame
pygame.init()
import random

speed = 25
score = 0
prom = 0

body =[] 
body.append(pygame.Rect(300,300,25,25))

start = True
x_food = random.randint(7, 593)
y_food = random.randint(7, 593)
width, haight = 600, 600 
font = pygame.font.SysFont(None, 24)


def points(window, text, x , y):
    img = font.render(text, True, (255,255,255))
    window.blit(img,(x,y))


window = pygame. display.set_mode((width, haight))
pygame.display.set_caption('Snake game')
running = True

deset = 0
dodaj = False

while running:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            running = False 

    print(body)
    deset+=1
    if deset == 100:
        keys = pygame.key.get_pressed()

        if dodaj:
            if prom == "l":
                body.append(pygame.Rect(body[-1].x+25,body[-1].y,25,25))
            if prom == "r":
                body.append(pygame.Rect(body[-1].x-25,body[-1].y,25,25))
            if prom == "u":
                body.append(pygame.Rect(body[-1].x,body[-1].y+25,25,25))
            if prom == "d":
                body.append(pygame.Rect(body[-1].x,body[-1].y-25,25,25))
            
            dodaj = False

        for i in range(len(body)-1,0,-1):
            body[i] = pygame.Rect(body[i-1].x,body[i-1].y,25,25) 

        if prom == "l":
            body[0].x -= speed
        if prom == "r":
            body[0].x += speed
        if prom == "u":
            body[0].y -= speed
        if prom == "d":
            body[0].y += speed

        if keys[pygame.K_LEFT]:
            body[0].x -= speed
            prom = "l"
        if keys[pygame.K_RIGHT]:
            body[0].x += speed
            prom = "r"
        if keys[pygame.K_UP]:
            body[0].y -= speed
            prom = "u"
        if keys[pygame.K_DOWN]:
            body[0].y += speed
            prom = "d"
        deset = 0

    if body[0].x >= 595  or body[0].y >= 595 or body[0].x <= 5 or body[0].y <= 5:
        running = False

    s = "score: " + str(score)
    points(window,s,0,0)

    window.fill((0, 0, 0))
    food = pygame.draw.circle(window, (0, 125, 125), (x_food, y_food), 7)
    head = pygame.draw.rect(window, (255, 0, 0), body[0])
    for b in body:
        pygame.draw.rect(window, (255, 0, 0), b)
    pygame.display.update()


    if head.colliderect(food):
        score += 1
        x_food = random.randint(7, 593)
        y_food = random.randint(7, 593)
        dodaj = True
        
pygame.quit()

