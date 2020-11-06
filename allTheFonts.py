# define cm to pt
cm = 1/0.0352777776
# define inch to pt
inch = 72

# set margin
margin = 2*cm

# give me the initial condition for formatted string
fs = FormattedString('Here are some fonts: ', 
    fill=0, 
    fontSize=20,
    lineHeight=40,
    font='Gimlet Variable',
    align="left",
    
    fontVariations=dict(wght=900),
    )
    
for fontName in installedFonts():
    fs.append(fontName+' ', font=fontName, fill=(random(), random(), random()))

# until there is no more formatted string left
# make a new page with a textbox
while fs:
    newPage('A3Landscape')
    contentWidth = width()-margin*2
    contentHeight = height()-margin*2
    translate(margin, margin)
    fs = textBox(fs, (0, 0, contentWidth, contentHeight))