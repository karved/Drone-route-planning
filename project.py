import numpy as np
import pandas as pd
import shapefile as shp
import math
from math import radians, sin, cos, acos
from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("DROUTER")

def sel ():
    
    root.filename =  filedialog.askopenfilename(initialdir = "recent",title = "Select a Shapefile",filetypes = (("Shapefiles", "*.shp"),("all files","*.*")))

    e1.delete(1.0,END)
    e1.insert(END, root.filename)

root.geometry("400x250")
 

#set window color
root['bg']='black'

button =Button(text="Select File",command=sel,font="calibri",width=10,activebackground="grey")
button.pack(pady=20) 
e1 = Text(height=2, width=40)
e1.pack()
button1 =Button(text='Open', command=root.destroy,font="calibri",width=10) 
button1.pack(pady=35) 

root.mainloop()


sf = shp.Reader(root.filename)
n= len(sf)
l=[]
edge_matrix= np.zeros((n, n), dtype=int)
for i in range(n):
    l.append(sf.shape(i).points[0])
# print(l)
"""
def euclidean_dist(x1, y1, x2, y2):
    return int((math.sqrt((x1-x2)**2 + (y1-y2)**2))*300)
"""
def dist_points(x1, y1, x2, y2):
     return int(6371.01 * acos(sin(radians(x1))*sin(radians(x2)) + cos(radians(x1))*cos(radians(x2))*cos(radians(y1) - radians(y2))))
def inputs():
    
    #print(sf.shape(2).shapeTypeName)
    #n= len(sf)
    #print(sf.bbox)
    #print(sf.shapes())
    #print(sf.shape(0))
    #print(sf.shape(0).points)
    
    for i in range(n):
        for j in range(n):
            if i==j:
                ip=0
            elif i<j:
                ip= int(input("Is there an edge between {0} and {1} (1 for yes, 0 for no)? ".format(chr(i+65), chr(j+65))))
                edge_matrix[i][j]= ip
                edge_matrix[j][i]= ip
                
    weight_matrix= np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if edge_matrix[i][j]==1:
                #weight_matrix[i][j]= euclidean_dist(l[i][0], l[i][1], l[j][0], l[j][1])
                weight_matrix[i][j]= dist_points(l[i][1], l[i][0], l[j][1], l[j][0])
                
            
    weight_matrix= np.matrix(weight_matrix)
    print("The matrix is: ")
    print(weight_matrix)
    return n, weight_matrix


"""
sf = shp.Reader("points7.shp")
print(len(sf.shapes()))
for i in range(len(sf)):
    print(sf.shape(i).points[0])
print(sf.shapeRecords()[0].record[0])

for i in range(len(sf)):
    print(sf.shape(i).points)
"""