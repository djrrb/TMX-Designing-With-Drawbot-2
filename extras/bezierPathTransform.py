# run this in drawbot
# controls the font to be used
theFont = 'Verdana'
# controls the text to be set
theText = 'Hello world!'


# write the text into a bezier path so we can see its points
b = BezierPath()
# draw the text into the canvas
b.text(theText, font=theFont, fontSize=150)

# move to the center of the canvas
translate(width()/2, height()/2)


# transform matrix: (xy, xx, yy, yx, x, y)
b.transform((
    .8, #xy = horizontal stretch
    .5, #xx = vertical skew
    2, #yy = horizontal skew
    3, #yx = vertical stretch
    0, #x = x offset
    0, #y = y offset
    ))

# draw the bounding box

boundX, boundY, boundW, boundH = b.bounds()

# move to half the width of the path
translate(-boundW/2, -boundH/2)

# draw the bounding box
stroke(1, 0, 0)
fill(None)
rect(boundX, boundY, boundW-boundX, boundH-boundY)

# draw the bezier path
fill(0)
stroke(None)
drawPath(b)