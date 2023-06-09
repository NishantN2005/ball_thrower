import pygame as pg
from sys import exit

class Text(pg.sprite.Sprite):
    def __init__(self,x,y,vyi,vxi):
        super().__init__()
        pg.draw.rect(screen,'White',pg.Rect(50,250,230,100), 2)
        font=pg.font.Font(None,25)
        font2=pg.font.Font(None,23)
        y=round(abs(y-400),2)
        text_surf=font.render(f'x-pos: {x}  y-pos:{y}   ',False,'White')
        num_surf=font.render(f'vxi={vxi}             vyi={vyi}',False,'White')
        restart_surf=font2.render(f'PRESS SPACE TO RESTART',False,'White')
        screen.blit(text_surf,(60,260))
        screen.blit(num_surf,(60,300))
        screen.blit(restart_surf,(60,330))

pg.init()
screen=pg.display.set_mode((800,400))
pg.display.set_caption('Physics')
clock=pg.time.Clock()
vxi=0
vyi=0
index=0
arr=[]
animation_start=False
#music/sounds
shoot_sound=pg.mixer.Sound('shootsd.mp3')
shoot_sound.set_volume(0.3)
bg_music=pg.mixer.Sound('bg.mp3')
bg_music.set_volume(0.3)
bg_music.play(loops=-1)
#circle timer
pg.draw.circle(screen,'White',(50,200),5)
circle_timer=pg.USEREVENT+1
pg.time.set_timer(circle_timer,900)
#mouse state control
mouse_up=False
#space state control
space_pressed=False
#Vectors
#this vector starts 
vector1=pg.math.Vector2(50,200)
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.MOUSEBUTTONUP:
             mouse_up=True
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                animation_start=False
                arr.clear()
                index=vxi=vyi=0
                
    if not mouse_up and animation_start==False:
        screen.fill('Black')
        pg.draw.circle(screen,'White',(50,200),5)
        pg.event.get()
        if pg.mouse.get_pressed()[0]==True:
            #pg.draw.circle(screen,'White',(50,200),5)
            (mx,my)=pg.mouse.get_pos()
            vector2=pg.math.Vector2(mx,my)
            pg.math.Vector2.magnitude
            pg.draw.line(screen,'White',(50,200),(mx,my),3)
            vector3=vector2-vector1
            vxi=vector3.x
            vyi=(vector3.y)*-1
            Text(50,200,vyi,vxi)
    if mouse_up and animation_start==False:
         shoot_sound.play()
         mouse_up=False
         vxi=vector3.x
         vyi=(vector3.y)*-1
         for t in range(1000):
            x=round(50+(vxi*t),2)
            y=round(200+((vyi*t)+((-9.8*(t*t)))/2)*-1,2)
            if y>400:
                break
            else:
                arr.append((x,y))
         animation_start=True
    if animation_start:
        space_pressed=False
        screen.fill('Black')
        pg.draw.circle(screen,'White',arr[index],5)
        Text(arr[index][0],arr[index][1],vyi,vxi)
        if index<len(arr)-1:
            index+=1
        else:
            index=0
    pg.display.update()
    clock.tick(15)