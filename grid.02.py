# use the colorsys library to convert HSV values
import colorsys

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# define a function that is a triangle
def triangle(x, y, w, h):
    # define a polygon using a series of (x,y) tuples
    polygon((x, y),
        (x+w/2, y+h),
        (x+w, y),
        #(h/2, w*5)
        )
        
# define a function that is an arbitrary shape
def shape(x, y, w, h):
    bp = BezierPath()
    # move to the point where we want to start
    bp.moveTo((x, y))
    # draw a line to the top right
    bp.lineTo((x+w, y+h))
    # make a random weirdo curve
    # randint() gets a random integer between 2 values 
    bp.curveTo(
        (x+w+randint(-50, 50), y+h/2),
        (x+w/2, y+randint(-50, 50)),
        (x+randint(-50, 50), y+randint(-50, 50))
        )
    # close the path
    bp.closePath()
    # now draw the path to the canvas
    drawPath(bp)


#r, g, b = hex_to_rgb('#FF00FF')
#fill(r, g, b)

# define the size of our grid
grid = 100

# do a loop for each page
for page in range(10):
    # make a new page with a background
    newPage(1000, 1000)
    fill(1)
    rect(0, 0, width(), height())
    # do a loop for each row
    for y in range(0, height(), grid):
        # do a loop for each column
        for x in range(0, width(), grid):
            # derive our hue and value 
            h = x / width()
            v = y / height()
            # let saturation be 1 always
            # convert HSV to RGB
            r, g, b = colorsys.hsv_to_rgb(h, 1, v)
            # fill with RGB
            fill(r, g, b)
            
            # get a random number between 0 and 1
            myRandomNumber = random()
            # use this number to determine what shape we draw
            if myRandomNumber < 1/4:
                oval(x, y, grid, grid)
            elif myRandomNumber < 2/4:
                triangle(x, y, grid, grid)
            elif myRandomNumber < 3/4:
                shape(x, y, grid, grid)
            else:
                rect(x, y, grid, grid)
           
# save the results
saveImage('~/desktop/colorfulGrid.gif')