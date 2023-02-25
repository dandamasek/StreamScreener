import tkinter as tk
import cv2
import keyboard as key
import threading
from PIL import Image
from PIL import ImageTk
import os



save_this_frame = False
photocount = 0

directory_frames = "frame"
if not os.path.isdir(directory_frames):
   os.makedirs(directory_frames)

def controllIfKeyPressed():
    global save_this_frame
    while True:
        if key.read_key() == "enter":
            save_this_frame = True 
        else:
            print("")


def makeScreenshotsFromVideoTRIGGER():
    thready = threading.Thread(target=makeScreenshotsFromVideo)
    thready.start()

def makeScreenshotsFromVideo():
    cap = cv2.VideoCapture("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4")
    global save_this_frame
    global photolabel1

    count=0
    icount_screend_frame = 0

    #showing stream frame by frame
    while True:
        t,f=cap.read()
        showsize = cv2.resize(f,(800,600))
        f=cv2.resize(f,(1920,1080))
        
        cv2.imshow("stream",showsize)
        
        if save_this_frame and icount_screend_frame != count:
            icount_screend_frame = count

            print("saved")
            
            #printed framy se ti ulozi do frame
            cv2.imwrite(directory_frames+"/a"+str(count)+".png",f)

            save_this_frame = False

            #show photo
            Screendphoto = Image.open(directory_frames+"/a"+str(count)+".png")
            Screendphoto = Screendphoto.resize((640,480))
            Screendphoto = ImageTk.PhotoImage(Screendphoto)

            photolabel1.config(image = Screendphoto)
       
        count=count+1
        cv2.waitKey(30)

    
threadx = threading.Thread(target=controllIfKeyPressed)
threadx.start()

window = tk.Tk()
window.title("Press enter to took a current frame")
window.geometry("640x1980")

photobtn = tk.Button(window, text='PlayStream', command=makeScreenshotsFromVideoTRIGGER)
photobtn.pack(side=tk.TOP, padx=1)

photolabel1 = tk.Label(window)
photolabel1.pack(pady=10)

window.mainloop()



