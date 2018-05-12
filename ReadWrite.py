#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 15:22:24 2016

@author: markprosser
PURPOSE: speedread speed read articles
"""
#still to do
#keep paragraphs in input file 




from IPython import get_ipython
#get_ipython().magic('%matplotlib qt')
#import matplotlib as mpl
get_ipython().magic('matplotlib inline')
get_ipython().magic('%reset -f')


import sys
sys.path.append('/Users/markprosser/Desktop')
sys.path.append('PythFunctions')
sys.path.append('ExtraPackages/easygui')
sys.path.append('ExtraPackages/PyUserInput-0.1.11')
sys.path.append('pyobjc-framework-Quartz-3.2.1')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import datetime
import math
from datetime import timedelta
#from Function import show_plot
import io
import tkinter as tk
import re
import subprocess
import platform



#jap 3 @0.25

gap=0
delay=0.1

#0.10= 339
#0.09= 356
#0.08= 382
#0.073= 400
#0.07= 409
#0.06= 441
#0.05= 477
#0.04= 513
#0.03= 564
#0.02= 617
#0.01= 674

gate=1



#################### opening and reading in
#with io.open('ReadWriteOutput/ReadWriteInput.txt', "r", encoding='utf-8-sig') as f:
with io.open('/Users/markprosser/Desktop/ReadWriteInput.txt', "r", encoding='utf-8-sig') as f:
    data = f.read()



    
    
#################### splitting up block of chinese text
def encrypt(string, length):
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))

if gap==0:
    pass
else:
    data=encrypt(data, gap)



#################### opens up write out file       
text_file = open("/Users/markprosser/Desktop/Output.html", "w", encoding='utf-8-sig')





#################### looping through words  
#################### displaying to tkinter window  
#################### write to output file
w = 1000; h = 200; x = 150; y = 300
ssplit = data.split()
print(len(ssplit))



def onKeyPress(event):
    print(a)
    text_file.write("""<span style="background-color: #FFFF00; font-family: 'Liberation Sans',sans-serif">{}</span>""".format(a+' '))
    gate=0
    
def raise_app(root: tk): #this function automatically activates the tkinter frame in MacOS10.10
    root.attributes("-topmost", True)
    if platform.system() == 'Darwin':
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
        script = tmpl.format(os.getpid())
        output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
    root.after(0, lambda: root.attributes("-topmost", False))

    
#for i in range(3, 0, -1):
#  try:
#    f()
#  except IOError:
#    if i == 1:
#      raise
#    print('retry')
#  else:
#    break
    
for i in range(0,len(ssplit)):
        
        a=ssplit[i]
           
        if i==0:

            root = tk.Tk()
            root.geometry("%dx%d+%d+%d" % (w, h, x, y))
            root.attributes("-topmost", True)
            T = tk.Text(root, height=4, width=30, font = ('Comic Sans MS',55), bg = 'blue', fg = 'white')
            T.tag_configure('tag-center', justify='center')
            T.insert(tk.END, a,'tag-center')
            T.place(x=500, y=150, anchor="center")
            root.update()
            root.bind('<space>', onKeyPress) 
            text_file.write("""<span style="color: black; font-family: 'Liberation Sans',sans-serif">{}</span>""".format(a+' '))
            raise_app(root)
            time.sleep(delay)
           
       
        elif (i > 0) and (i < len(ssplit)-1):#len(ssplit)): 
            if gate == 0:
                babe = 1
            else:
                try:
                    if i%1000 == 0:
                        print(i)
                    T.delete('1.0', tk.END)
                    T.insert(tk.END, a,'tag-center')
                    root.update()
                    root.bind('<space>', onKeyPress)
                    root.bind('<Return>', onKeyPress)
                    text_file.write("""<span style="color: black; font-family: 'Liberation Sans',sans-serif">{}</span>""".format(a+' '))
                    text_file.flush()
                    raise_app(root)
                    time.sleep(delay)
                    #root.quit()
                except:
                    pass
                    #time.sleep(delay/5)
        else: 
            T.delete('1.0', tk.END)
            T.insert(tk.END, a,'tag-center')
            root.update()
            root.bind('<space>', onKeyPress)
            root.bind('<Return>', onKeyPress)
            text_file.write("""<span style="color: black; font-family: 'Liberation Sans',sans-serif">{}</span>""".format(a+' '))
            text_file.flush()
            raise_app(root)
            #time.sleep(delay)
            time.sleep(1)
            root.destroy()
