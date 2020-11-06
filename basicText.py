cm = 1/0.0352777776
inch = 72
margin = 2*cm

newPage('A3Landscape')

rect(margin, margin, width()-margin*2, height()-margin*2)



translate(margin, margin)
fill(1)
fontSize(50)
font('Gimlet Variable')
openTypeFeatures(ss01=True)
fontVariations(wdth=75, wght=900)


text('Hello World', (0, 0))