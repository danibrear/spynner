import tkinter as tk
import os
import sys
window = tk.Tk()
frameCnt = 31
frames = []


window.wm_attributes('-type', 'dock')
window.attributes('-alpha', 0.9)
window.tk.call('wm', 'overrideredirect', window, True)
window.attributes('-topmost', True)

## Uncomment to add a close button
# close = tk.Label(window, text="×", fg="white", bg="#252525", font="Helvetica 12 bold")
# close.pack(side="bottom", fill="x", pady=1)
# close.bind('<Button-1>', lambda e: window.destroy())

windowX = 0
windowY = 0

def startmove(event):
    global windowX, windowY
    windowX = event.x
    windowY = event.y

def stopmove(event):
    global windowX, windowY
    windowX = None
    windowY = None

def domove(event):
    global windowX, windowY
    deltax = event.x - windowX
    deltay = event.y - windowY
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry("+%s+%s" % (x, y))

window.bind('<ButtonPress-1>', startmove)
window.bind('<ButtonRelease-1>', stopmove)
window.bind('<B1-Motion>', domove)


GIF_SIZE = 200
SHRINK = 3

OFFSET = GIF_SIZE // SHRINK
PADDING = GIF_SIZE // SHRINK // 2

for i in range(0, frameCnt):
    img = tk.PhotoImage(file='{}/spinner.gif'.format(os.path.dirname(os.path.realpath(__file__))),format = 'gif -index %i' %(i))
    img = img.subsample(SHRINK, SHRINK)
    frames.append(img)

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    window.after(30, update, ind)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.title('Spinner')
window.geometry('{}x{}+{}+{}'.format(GIF_SIZE//SHRINK, GIF_SIZE//SHRINK, screen_width//2-OFFSET, screen_height//2-OFFSET))
label = tk.Label(window)
window.resizable(False, False)

label.pack()
window.after(0, update, 0)
window.mainloop()
