# define cm to pt
cm = 1/0.0352777776
# define inch to pt
inch = 72

# set margin
margin = 2*cm

# give me the initial condition for formatted string
fs = FormattedString("""The quick brown fox jumps over the lazy dog's face. """*100, 
    fill=0, 
    fontSize=31,
    lineHeight=40,
    font='Gimlet Variable',
    align="justified",
    fontVariations=dict(wght=900),
    )

# until there is no more formatted string left
# make a new page with a textbox
while fs:
    newPage('A3Landscape')
    contentWidth = width()-margin*2
    contentHeight = height()-margin*2
    translate(margin, margin)
    fs = textBox(fs, (0, 0, contentWidth, contentHeight))