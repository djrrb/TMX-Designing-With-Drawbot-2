

for page in range(360):
    
    
    # make new page
    newPage(1000, 1000)

    stroke(1, 0, 0)
    fill(None)
    # define a rectangle size
    rectSize = width()

    # move (0, 0) to the middle of the canvas
    translate(width()/2, height()/2)
    # draw a rectangle centered on (0, 0)
    
    for iteration in range(30):
        rect(-rectSize/2, -rectSize/2, rectSize, rectSize)
        scale(.9)
        rotate(page)
        #skew(2)
        
saveImage('/Users/david/Desktop/spiral.mp4')