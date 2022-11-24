from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import os
texts = [
    'Yare yare'
    'Я люблю рогалики'
    'Прослушайте текст и напишите сжатое изложение'
]

def f(name,text):
    name = 'img/' + name + '.jpg'
    im = Image.new('RGB', (500,500), color=('#FAACAC'))
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 20, encoding='UTF-8')
    draw_text.text(
        (20,100),
        text,
        fill=('#1C0606'),
        font= font
    )
    im.save(name)
def f1():
    direc = 'img/'
    files = os.listdir(direc)
    imag = list(filter(lambda x: x.endswith('.jpg'), files))
    clips = [ImageClip('img/' + m).set_duration(2) for m in imag]

    final = concatenate_videoclip(clips, method='compose')
    final.write_videofile('test.mp4', fps=24)

for i in range(len(texts)):
    f(str(i),texts[i])
    
f1()
    
    
