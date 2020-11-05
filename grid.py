

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


r, g, b = hex_to_rgb('#FF00FF')

#fill(r, g, b)
for page in range(10):
    newPage(1000, 1000)
    for y in range(0, height(), 100):
        for x in range(0, width(), 100):
            fill(random(), random(), random())
            oval(x, y, 100, 100)
            
saveImage('~/desktop/colorfulGrid.gif')