import numpy as np
import pandas as pd
import shapefile as shp
import math
from math import radians, sin, cos, acos
from tkinter import filedialog
from tkinter import *
import gmplot
import webbrowser
from PIL import ImageTk,Image
import os

l=[]
# print(l)
"""
def euclidean_dist(x1, y1, x2, y2):
    return int((math.sqrt((x1-x2)**2 + (y1-y2)**2))*300)
"""
def dist_points(x1, y1, x2, y2):
     return int(6371.01 * acos(sin(radians(x1))*sin(radians(x2)) + cos(radians(x1))*cos(radians(x2))*cos(radians(y1) - radians(y2))))
  
def inputs():
    global ip_screen, n, edge_matrix, check_matrix, sf, pathy, lat_list, long_list, colors
    global mean_lat, mean_long
    sf = shp.Reader(root.filename)
    n= len(sf)
    for i in range(n):
        l.append(sf.shape(i).points[0])
        
    pathy=root.filename[::-1]
    pathy= pathy[:(pathy.find('/')-1):-1]
    # print(pathy)
    
    
    lat_list=[]
    long_list=[]
    colors= ["blue", "cyan", "green", "purple", "yellow", "brown", "violet"]
    for i in range(len(sf)):
        lat_list.append(l[i][1])
        long_list.append(l[i][0])
        mean_lat= np.mean(lat_list)
        mean_long= np.mean(long_list)
    
    new=2
    gmap3= gmplot.GoogleMapPlotter(mean_lat, mean_long, 13)
    gmap3.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
    points=0
    for i, j in zip(lat_list, long_list):
        gmap3.marker(i, j, "red", title=chr(points+65))
        points= points + 1
    gmap3.draw(pathy+"map30.html")
    url= (pathy+"map30.html")
    webbrowser.open(url, new=new)

    root.destroy()
    ip_screen= Tk()
    ip_screen.title("D-Route")
    ip_screen.geometry("600x500")
    #set window color
    ip_screen['bg']='bisque'

    edge_matrix= [[] * i for i in range(n)]
    for i in range(n):
        for j in range(n):
            edge_matrix[i].append(IntVar(ip_screen))
   
    text1=65
    text2=65
    for i in range(n):
        Label(ip_screen,background="bisque", font=("calibri","15","bold"),width=6,text=chr(text1)).grid(row= 1, column=i, padx=20)
        text1= text1 + 1
    for i in range(n):
        Label(ip_screen,background="bisque",font=("calibri","15","bold"),width=6,text=chr(text2)).grid(row=i+2, sticky= W, pady=20)
        text2= text2 + 1
    zero_var=0
    for i in range(n):
        for j in range(n):
            if i==j:
                Checkbutton(ip_screen,bg="bisque", variable=zero_var).grid(row=i+2, column= j, padx=20)
            elif i<j:
                Checkbutton(ip_screen,bg="bisque", variable=edge_matrix[i][j]).grid(row=i+2, column= j, padx=20)
            else:
                Checkbutton(ip_screen,bg="bisque",variable=edge_matrix[j][i]).grid(row=i+2, column= j, padx=20)
    Button(ip_screen,font=("calibri","15"),width=7,activebackground="grey",bg="white",text="Next -->", command= submit).grid(sticky=S)
    ip_screen.mainloop()
    #print(sf.shape(2).shapeTypeName)
    #n= len(sf)
    #print(sf.bbox)
    #print(sf.shapes())
    #print(sf.shape(0))
    #print(sf.shape(0).points)
    """
    for i in range(n):
        for j in range(n):
            if i==j:
                ip=0
            elif i<j:
                ip= int(input("Is there an edge between {0} and {1} (1 for yes, 0 for no)? ".format(chr(i+65), chr(j+65))))
                edge_matrix[i][j]= ip
                edge_matrix[j][i]= ip
    """        

    
def submit():
    ip_screen.destroy()
    global weight_matrix
    weight_matrix= np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if edge_matrix[i][j].get()==1:
                edge_matrix[j][i].set(1)
    for i in range(n):
        for j in range(n):
            if edge_matrix[i][j].get()==1:
                #weight_matrix[i][j]= euclidean_dist(l[i][0], l[i][1], l[j][0], l[j][1])
                weight_matrix[i][j]= dist_points(l[i][1], l[i][0], l[j][1], l[j][0])
                
            
    weight_matrix= np.matrix(weight_matrix)
    print("The matrix is: ")
    print(weight_matrix)


def sel ():
    
    root.filename =  filedialog.askopenfilename(initialdir = "recent",title = "Select a Shapefile",filetypes = (("Shapefiles", "*.shp"),("all files","*.*")))

    e1.delete(1.0,END)
    e1.insert(END, root.filename)


root = Tk()
root.title("D-Route")
root.geometry("600x650")
 



#set width and height

canvas=Canvas(root,width=600,height=400)

# used drone.jpeg from pics folder , took file directory of running file and traversed to pics folder
target_path_2 = os.path.join(os.path.dirname(__file__), '..\pics\drone.jpeg')

image=ImageTk.PhotoImage(Image.open(target_path_2))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()


#set window color
root['bg']='bisque'


button =Button(text="Select File",command=sel,font=("calibri","15"),width=10,activebackground="grey",bg="white")
button.pack(pady=20) 
e1 = Text(height=2, width=40)
e1.pack()
button1 =Button(text='Open', command=inputs,font=("calibri","15"),width=10,activebackground="grey",bg="white") 
button1.pack(pady=35) 

root.mainloop()





"""
sf = shp.Reader("points7.shp")
print(len(sf.shapes()))
for i in range(len(sf)):
    print(sf.shape(i).points[0])
print(sf.shapeRecords()[0].record[0])

for i in range(len(sf)):
    print(sf.shape(i).points)
"""
