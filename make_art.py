from PIL import Image, ImageDraw, ImageFilter
import math, random
random.seed(1847)
S=768
im=Image.new('RGB',(S,S)); p=im.load()
# deep space gradient
for y in range(S):
 for x in range(S):
  r=math.hypot(x-S*.52,y-S*.48)/S
  glow=max(0,1-r*1.45)
  aur=math.exp(-((x-S*.68)**2+(y-S*.28)**2)/(2*170**2))
  p[x,y]=(int(5+18*glow+12*aur), int(8+12*glow+22*aur), int(25+42*glow+35*aur))
# soft nebula layer
neb=Image.new('RGBA',(S,S),(0,0,0,0)); nd=ImageDraw.Draw(neb)
for _ in range(90):
 x=random.randint(-100,S+100); y=random.randint(-100,S+100); r=random.randint(20,120)
 col=random.choice([(50,210,230,12),(180,60,255,13),(255,100,190,10),(50,120,255,10)])
 nd.ellipse((x-r,y-r,x+r,y+r),fill=col)
neb=neb.filter(ImageFilter.GaussianBlur(35)); im=Image.alpha_composite(im.convert('RGBA'),neb)
d=ImageDraw.Draw(im)
# stars
for _ in range(520):
 x=random.randrange(S); y=random.randrange(S); a=random.randrange(50,220); r=random.choice([1,1,1,2])
 d.ellipse((x-r,y-r,x+r,y+r),fill=(150,210,255,a))
# central luminous flower / planet
cx,cy=384,392
# orbital rings
for k in range(7):
 box=(cx-105-k*26,cy-58-k*14,cx+105+k*26,cy+58+k*14)
 d.ellipse(box,outline=(70,210,255,90-k*9),width=2)
# petals from logarithmic spiral
for i in range(96):
 t=i/96*math.pi*12
 rad=18+4.8*t
 x=cx+math.cos(t)*rad*1.25; y=cy+math.sin(t)*rad*.72
 rr=13+int(7*math.sin(t*1.7)**2)
 hue=(i*11)%255
 col=(90+int(120*math.sin(t)**2),40+int(120*(1-math.sin(t)**2)),180+int(65*math.cos(t*.5)**2),210)
 d.ellipse((x-rr,y-rr*.55,x+rr,y+rr*.55),fill=col,outline=(180,245,255,180),width=1)
# crystal stems and blooms
for i in range(13):
 ang=-2.7+i*.46; length=120+random.randint(-18,30)
 x2=cx+math.cos(ang)*length; y2=cy+math.sin(ang)*length*.65
 d.line((cx,cy,x2,y2),fill=(45,225,200,150),width=3)
 pts=[]
 for q in range(6):
  a=q*math.pi/3; rr=18 if q%2==0 else 8
  pts.append((x2+math.cos(a)*rr,y2+math.sin(a)*rr*.7))
 d.polygon(pts,fill=(40,210,190,110),outline=(160,255,240,220))
# core glow
for rr in range(72,3,-3):
 a=int(3+70*(1-rr/72)**2)
 d.ellipse((cx-rr,cy-rr,cx+rr,cy+rr),fill=(70,190,255,a))
d.ellipse((cx-18,cy-18,cx+18,cy+18),fill=(245,255,210,255))
# foreground frame arcs
for k in range(5):
 d.arc((-160-k*24,500-k*15,930+k*24,1100+k*15),190,350,fill=(80,120,255,100-k*12),width=2)
# subtle border
for k in range(3): d.rounded_rectangle((12+k*5,12+k*5,S-12-k*5,S-12-k*5),radius=28,outline=(100,220,255,80-k*20),width=1)
im.convert('RGB').save('/home/ubuntu/makefun-login/coolest-art-entry/entry.png',optimize=True)
