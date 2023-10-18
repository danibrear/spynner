import tkinter as tk
import os
import sys
window = tk.Tk()
frameCnt = 31
frames = []

window.attributes('-topmost', True)
window.wm_attributes('-type', 'dock')

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
