# run this in drawbot
# controls the font to be used
theFont = 'Verdana'
# controls the text to be set
theText = 'Hello world!'
# page dimensions
newPage(1500, 250)
# write the text into a bezier path so we can see its points
b = BezierPath()
translate(50, 50)
b.text(theText, font=theFont, fontSize=200)
# draw the letters themselves
# semitransparent black fill, opaque black stroke
fill(0, 0, 0, .25)
strokeWidth(.5)
stroke(0)
drawPath(b)
stroke(None)
# loop through each contour in the bezier path
for ci, c in enumerate(b):
    # loop through each segment in the contour
    for si, s in enumerate(c):
        # loop through each point in the segment
        for pi, p in enumerate(s):
            # get the x and y coordinates from the point
            x, y = p
            # this is the tricky bit
            # if this is the first offcurve point, we will
            # connect it to the previous point
            # if not, we will connect it to the last point
            # in the segment, which is the oncurve point
            if pi != len(s)-1:
                if pi == 0:
                    oncurve = c[si-1][-1]
                else:
                    oncurve = s[-1]
                # make green offcurve points 
                fill(0, 1, 0)
                oval(x-2, y-2, 4, 4)
                # connect them to the corresponding 
                # oncurve point with a line
                strokeWidth(.5)
                stroke(0, 1, 0)
                line((oncurve[0], oncurve[1]), (x, y))
                stroke(None)
# loop through everything again, so we draw the oncurves on top
for ci, c in enumerate(b):
    fill(.5, 0, 0)
    for si, s in enumerate(c):
        print(s)
        p = s[-1]
        x, y = p
        rect(x-2, y-2, 4, 4)
        fill(1, 0, 0)