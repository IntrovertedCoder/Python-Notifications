try:
    from tkinter import *
    import mss
    import numpy as np
    import cv2
except ImportError as e:
    print('Couldn\'t load module {}'.format(e))


def rgbtohex(rgb):
    '''
    Converts a rgb tuple eg: (255, 255, 255)
    to #ffffff because tkinter wont accept rgb values
    '''
    return('#%02x%02x%02x' % rgb)


def averageColorInverted(width, height,
                         x, y):
    '''
    Get the average color of specified cords, and invert it.
    Used when setting the text color, Makes it easier to read.
    And makes it adaptive.
    Returns a tuple of rgb values. Recommend to put into rgbtohex
    '''
    mon = {'top': y, 'left': x, 'width': width, 'height': height}

    with mss.mss() as sct:
        im = np.asarray(sct.grab(mon))
        average = cv2.resize(im, (1, 1))[0][0]
        inverted = []
        inverted.append(abs(average[0] - 255))
        inverted.append(abs(average[1] - 255))
        inverted.append(abs(average[2] - 255))
        return(rgbtohex(tuple(inverted)))


def averageColor(width, height,
                 x, y):
    '''
    Get the average color of specified cords, and does not invert it.
    Honestly idk what this version is used for just thought to include it xD.
    And makes it adaptive.
    Returns a tuple of rgb values. Recommend to put into rgbtohex
    '''
    mon = {'top': y, 'left': x, 'width': width, 'height': height}

    with mss.mss() as sct:
        im = np.asarray(sct.grab(mon))
        average = cv2.resize(im, (1, 1))[0][0]
        inverted = []
        print(average)
        inverted.append(abs(average[0] - 255))
        inverted.append(abs(average[1] - 255))
        inverted.append(abs(average[2] - 255))
        return(rgbtohex(tuple(inverted)))


def notification(titleStr, textStr, exitTime,
                 bgColor, fgColor, transparentColor,
                 width, height,
                 x, y):
    '''
    Show window
    titleStr is the title of the window, size 17 and bold
    textStr is the body of the message, size 12 and normal
    exitTime is how long to show the window for in ms
    bgColor is the color of the background
    fgColor is the color of the text
    transparentColor is the color to make transparent
    Set to some random color for no transparency
    width and height are the width and height of tkinter window
    x and y are coords of window
    '''
    root = Tk()

    # Convert x y width and height to str
    width = str(width)
    height = str(height)
    x = str(x)
    y = str(y)

    def quit():
        root.destroy()

    # root.attributes('-alpha', 0.5)
    # Get rid of window title
    root.overrideredirect(1)
    # Set geometry to value
    root.geometry(width + 'x' + height + '+' + x + '+' + y)

    titleFrame = Frame(root, bg=bgColor).pack(side=LEFT)
    titleLab = Label(root, text=titleStr, font=(
        "Courier", 17, 'bold'),
        foreground=fgColor, bg=bgColor).pack(side=TOP)

    textFrame = Frame(root, bg=bgColor).pack(side=LEFT)
    textLab = Label(root, text=textStr, font=(
        "Courier", 12, 'bold'),
        foreground=fgColor, bg=bgColor).pack(side=TOP)

    root.config(bg=bgColor)

    root.attributes("-topmost", 1)  # Always on top
    root.attributes('-transparentcolor', transparentColor)
    root.after(exitTime, quit)
    root.mainloop()
