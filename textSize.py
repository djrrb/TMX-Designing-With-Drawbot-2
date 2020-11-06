import random

# make a list of message to print
messages = ['Hello worlp!', '¿Como estás?', 'drawbot is fun', 'sometimes']

# loop through message
for message in messages:
    fontName = random.choice(installedFonts())
    # new page
    newPage(1000, 1000)
    
    # dress rehersal
    # get the formattedString at 1pt, so that we know the textSize
    fs = FormattedString(message, 
        fontSize=1, 
        font=fontName,
        lineHeight=1,
        )

    # divide doc width that by that to get a fontSize that will fit perfectly
    w, h = textSize(fs)
    multiplier = width() / w
    print(multiplier)
    
    # now, give us the formatted string with the correct font size
    fs = FormattedString(message, 
        fontSize=multiplier, 
        font=fontName,
        lineHeight=multiplier,
        )
    
    # get the dimensions of that
    w, h = textSize(fs)
    
    # get the offset by figuring out margin
    xoffset = (width()-w)/2
    yoffset = (height()-h)/2-fs.fontDescender()

    # draw the text
    fill(1, 0, 0)
    rect(xoffset, yoffset, w, h)
    fill(0)
    text(fs, (xoffset, yoffset-fs.fontDescender()))