from PIL import Image

def aspect_ratio(width,height):
      x, y = width, height
      while y:
        x, y = y, x % y
      print('アスペクト比: ',str(width/x),':',str(height/x))

image = Image.open('C:\python/tapioca.png')
width = int(image.size[0])
height = int(image.size[1])
print('width:',str(width),' height:',str(height))  
aspect_ratio(width,height) 

