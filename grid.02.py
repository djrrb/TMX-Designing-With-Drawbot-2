import colorsys

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def triangle(x, y, w, h):
    polygon((x, y),
        (x+w/2, y+h),
        (x+w, y),
        #(h/2, w*5)
        )
        
def shape(x, y, w, h):
    bp = BezierPath()
    bp.moveTo((x, y))
    bp.lineTo((x+w, y+h))
    bp.curveTo(
        (x+w+randint(-50, 50), y+h/2),
        (x+w/2, y+randint(-50, 50)),
        (x+randint(-50, 50), y+randint(-50, 50))
        )
    bp.closePath()
    drawPath(bp)


#r, g, b = hex_to_rgb('#FF00FF')

#fill(r, g, b)
for page in range(1):
    newPage(1000, 1000)
    for y in range(0, height(), 100):
        for x in range(0, width(), 100):
            h = x / width()
            v = y / height()
            print(h, v)
            r, g, b = colorsys.hsv_to_rgb(h, 1, v)
            fill(r, g, b)
            
            myRandomNumber = random()
            if myRandomNumber < 1/4:
                oval(x, y, 100, 100)
            elif myRandomNumber < 2/4:
                triangle(x, y, 100, 100)
            elif myRandomNumber < 3/4:
                shape(x, y, 100, 100)
            else:
                rect(x, y, 100, 100)
           
            
#saveImage('~/desktop/colorfulGrid.gif')