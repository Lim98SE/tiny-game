import pygame as P
from random import randint as r
z=0;w,h=640,480;D=z;n=2;S=z;Y=32;P.init();W=P.display.set_mode((w,h));C=[[z]*3,[127]*3,[255]*3];p=[240,z];E=[];f=P.font.SysFont("",Y);Z=64;U=16;c=P.time.Clock()
for i in range(n):E.append(P.Rect(((w//n) * i)-Y,z,Y,r(U,288)))
while 1:
 W.fill(C[z])
 for e in P.event.get():
  if e.type==P.QUIT:exit()
  if e.type==P.MOUSEBUTTONDOWN:p[1]=-8
 if not D:
  W.blit(f.render(str(S),1,C[2]),(320,h-Y));p[1]+=0.5;p[z]+=p[1];X=P.Rect(U,p[z],U,U);P.draw.rect(W,C[2],X)
  for e in E:
   e.move_ip(-4,z)
   if e.x<-Y:
    e.x=672;e.h=r(U,288)
   P.draw.rect(W,C[1],e);o=e.h;t=e;b=P.Rect(e.x,128+e.h,e.w,800);P.draw.rect(W,C[1],b);e.update(e.x,z,e.w,o)
   if X.colliderect(t)|X.colliderect(b):D=1
   elif X.y>480:D=1
   else:
    if X.x>e.x:e.move_ip(-99,z);S+=1
 else:W.blit(f.render(str(S),1,C[2]),(Z,Z))
 P.display.update();c.tick(60)