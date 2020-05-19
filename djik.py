import numpy as np
from project import *
import gmplot
import webbrowser
from tkinter import *
from tkinter import messagebox
"""
n = int(input("Enter the no. of Nodes: "))
print ("Enter the Matrix:")
matrix = np.array([],dtype="int")

for i in range(0,n):
    entries = list(map(int, input().split()))
    matrix = np.append(matrix,entries)
matrix = matrix.reshape(n,n)
print("\nEntered Matrix:\n {0}\n".format(matrix))
"""

"""
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
"""
#pathy=pathy
new=2

n= n
matrix= weight_matrix
print(n)
print(matrix)


gmap1= gmplot.GoogleMapPlotter(mean_lat, mean_long, 13)
gmap2= gmplot.GoogleMapPlotter(mean_lat, mean_long, 13)

gmap1.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
gmap2.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

#gmap1.scatter(lat_list, long_list, 'red', size=40, marker=False)
#gmap2.scatter(lat_list, long_list, 'red', size=40, marker=False)
#map3.scatter(lat_list, long_list, 'red', size=40, marker=False)
points=0
for i, j in zip(lat_list, long_list):
    gmap1.marker(i, j, "red", title=chr(points+65))
    gmap2.marker(i, j, "red", title=chr(points+65))
    points= points + 1


for i in range(len(sf)):
    for j in range(len(sf)):
        if edge_matrix[i][j].get()==1 and i>j:
            edge_lat_list=[]
            edge_long_list=[]
            edge_lat_list.append(lat_list[i])
            edge_long_list.append(long_list[i])
            edge_lat_list.append(lat_list[j])
            edge_long_list.append(long_list[j])
            gmap1.plot(edge_lat_list, edge_long_list, 'black', edge_width= 2.5)

gmap1.draw(pathy+"map40.html")
url= pathy+"map40.html"
webbrowser.open(url, new=new)

"""
# Souce Sink
source = ord(str(input("Select Source Node: ")))
source= source-65
sink = ord(str(input("Select Sink Node: ")))
sink= sink-65


# Charging Stations
bol = int(input("Do u want Charging Stations? 0 or 1: "))
if(bol==1):
    chst = list(map(str,input("Enter Charging Stations: ").split(",")))
    while chr(sink+65) in chst:
        print("Invalid Entry")
        chst = list(map(str,input("Enter Charging Stations: ").split(",")))
    
    print(chst)
else:
    chst=[]
"""

def details():
    global source, sink, chst, drones, depr
    chst= []
    source= ord(src.get())
    sink= ord(snk.get())
    source= source - 65
    sink= sink - 65
    for i in range(n):
        if chst_check[i].get()==1:
            chst.append(chr(i+65))
    drones= dro.get()
    depr= depre.get()
    charge_screen.destroy()

charge_screen= Tk()
charge_screen.geometry("800x600+200+200")
Label(charge_screen, text="Choose source node: ").place(x=30, y=30)
list1= []
src= StringVar()
snk= StringVar()
for i in range(n):
    list1.append(chr(i+65))
droplist= OptionMenu(charge_screen, src, *list1)
src.set('A')
droplist.config(width=5)
droplist.place(x= 150, y= 30)
Label(charge_screen, text="Choose sink node: ").place(x= 30, y= 70)
droplist1= OptionMenu(charge_screen, snk, *list1)
snk.set('A')
droplist1.config(width= 5)
droplist1.place(x= 150, y= 70)
Label(charge_screen, text="Choose charging stations if needed: ").place(x=30, y= 100)
chst_check=[]
for i in range(n):
    chst_check.append(IntVar(charge_screen))
xrange= 250
for i  in range(n):
    Checkbutton(charge_screen, text=chr(i+65), variable= chst_check[i]).place(x= xrange, y=100)
    xrange= xrange +30
dro= IntVar()
depre= IntVar()
Label(charge_screen, text="Enter no. of drones: ").place(x=30, y=130)
Entry(charge_screen, textvar= dro).place(x=150, y=130)
Label(charge_screen, text="Enter rate of loss: ").place(x= 30, y= 150)
Entry(charge_screen, textvar= depre).place(x=150, y=150)
Button(charge_screen, text="OK", command=details).place(x=30, y= 180)
charge_screen.mainloop()

if (len(chst))>0:
    charge_stn=[]
    plot_chst_lat=[]
    plot_chst_long=[]
    for i in chst:
        charge_stn.append(ord(i)-65)
    for i in charge_stn:
        plot_chst_lat.append(lat_list[i])
        plot_chst_long.append(long_list[i])

    #gmap1.scatter(plot_chst_lat, plot_chst_long, 'blue', size=40, marker=False)
    #gmap2.scatter(plot_chst_lat, plot_chst_long, 'blue', size=40, marker=False) 
    points=0
    for i, j in zip(plot_chst_lat, plot_chst_long):
        #gmap1.marker(i, j, "blue", title=chst[points])
        gmap2.marker(i, j, "blue", title=chst[points])
        points= points + 1


"""
# No. of Drones and Battery
drones = int(input("Enter No. of Drones: "))
depr=(int(input("Enter the Loss Rate(% per unit): ")))
while((0>depr) or (depr>100)):
    print("Invalid Entry")
    depr=(int(input("Enter the Loss Rate(% per unit): ")))
"""

battery = np.arange(drones)
battery.fill(100)


# Redundant variable and reached
red=0
reached=0


# Weight,prev,Taken,remaining arrays
w= np.arange(n)
prev= np.arange(n)
taken= np.arange(n)
taken.fill(0)
rem= np.arange(n)
rem.fill(0)
taken[source]=1
rem[source]=rem[sink]=1
for i in range(0,len(chst)):
    chst[i]= ord(chst[i])-65
    rem[chst[i]]= 1 

# Route list
route= []

# Djikstras Algo
def djik(source):
    # Source connect
    for i in range(0,n):
        if(taken[i]==0):
            if((i !=source)  and (i not in chst)):
                if ((w[i]>(w[source]+matrix[source,i])) and (matrix[source,i]!= 0)):
                
                    w[i]=(w[source]+matrix[source,i])
                    prev[i]=source

        elif((taken[i]!=0) and (np.count_nonzero(taken)== (n-len(chst)))):
        
            if((i !=source)  and (i not in chst)):
             if ((w[i]>(w[source]+matrix[source,i])) and (matrix[source,i]!= 0)):
                    
                    w[i]=(w[source]+matrix[source,i])
                    prev[i]=source
            
                
                

    # Sort outgoing source nodes
    b = {x:w[x] for x in range(0,n)}
    b=dict(sorted(b.items(), key = 
                lambda kv:(kv[1], kv[0]))) 
#    Remaining nodes
    for j in b:
        if((j!=source)):
            for i in range(0,n):
                if((i!=source) and (i not in chst)):
                    if ((w[i]>(w[j]+matrix[j,i])) and (matrix[j,i]!= 0)):
                        
                        w[i]=(w[j]+matrix[j,i])
                        prev[i]=j
                      

#   Safe Side Rep 
    for j in b:
        if((j!=source)):
            for i in range(0,n):
                if((i!=source) and (i not in chst)):
                    if ((w[i]>(w[j]+matrix[j,i])) and (matrix[j,i]!= 0)):
                        
                        w[i]=(w[j]+matrix[j,i])
                        prev[i]=j
                      


# Traversal
def loc (x,source):
        global red
        route.append(x)
        
       
        
    # NO path
        if(prev[x]==99999):
            red=red+1
            route.append("none")
            
            
    # Penultimate node
        elif(prev[x]==source):
            route.append(source)
          
            
    # General node
        else:
            loc(prev[x],source)


# Calc Route
color_count=0
flag=0

def calc(bat):
    global color_count, flag , reached
    route.reverse()
    # print(route)
    weight = 0
    a=0
    if(route[0]!="none"):

        mylist.insert(END,chr(route[0]+65)+"-> ")
        print(chr(route[0]+65),end="-> ")

        if(len(route)>1):
            for i in range(1,len(route)):
             if((route[i]!="none") and (route[i-1]!="none")):
                if(((bat-(depr*(matrix[route[i-1],route[i]])))>=0)):

                    weight = weight +  (matrix[route[i-1],route[i]])
                    bat = bat-(depr*(matrix[route[i-1],route[i]]))
                    rem[route[i]]=1
                    taken[route[i]]=1


                    print(chr(route[i]+65),end="-> ")
                    mylist.insert(END,chr(route[i]+65)+"-> ")

                else:
                    if((len(chst)!= 0) and (reached == 0)):
                        s=route[-1]
                        s1=route[i-1]
                        
                        global plot_lat_list
                        global plot_long_list
                        global color

                        plot_lat_list=[]
                        plot_long_list=[]
                        for i in route[:-1]:
                            plot_lat_list.append(lat_list[i])
                            plot_long_list.append(long_list[i])
                        color= colors[color_count]
                        gmap2.plot(plot_lat_list, plot_long_list, color, edge_width=2.5)
                        flag=1
                        #print(route)
                        
                        route.clear()
                        bat,a= djik2(s,s1,bat)
                        break

                    else:
                        print("No charge stn.")
                        mylist.insert(END,"No charge stn.")
                        weight = 99999
                        break

             else:
                print("none",end="")
                mylist.insert(END,"none")
                break
    else:
        print("None")
    
    #print(route)
    plot_lat_list=[]
    plot_long_list=[]
    for i in route:
        plot_lat_list.append(lat_list[i])
        plot_long_list.append(long_list[i])
    color= colors[color_count]
    gmap2.plot(plot_lat_list, plot_long_list, color, edge_width=2.5)
    if flag==0:
        color_count= color_count + 1
    flag=0

    
    return bat,(weight+a)

# Djikstras for charging station
def djik2(sink,source,battery):
    
    global flag
   

    prev.fill(99999)
    w.fill(99999)
    rem[source]=1
    w[source]= 0
    route.clear()
    djik3(source)
    global reached
    reached = 1

    minis = 99999
    mini =0
    for i in range(0,len(chst)):
        if(minis>w[chst[i]]):
            minis = w[chst[i]]
            mini = chst[i]

    if(minis!=99999):
        loc(mini,source)
        bat,a= calc(battery)
        if(a < 99999):
            prev.fill(99999)
            w.fill(99999)

            rem[mini]=1
            w[mini]= 0
            route.clear()
            taken[sink]=0
            djik(mini)
            loc(sink,mini)
            flag=1
            bat,wgt= calc(100)

            return bat,(a+wgt)

        else:  
            reached = 0
            return bat,a

    else:
        a=99999
        print("no charge stn.")
        return battery,a




# Djikstras Algo for finding Charge Stn.
def djik3(source):
    # Source connect
    for i in range(0,n):
            if((i !=source)):
                if ((w[i]>(w[source]+matrix[source,i])) & (matrix[source,i]!= 0)):
                
                    w[i]=(w[source]+matrix[source,i])
                    prev[i]=source


    # Sort outgoing source nodes
    b = {x:w[x] for x in range(0,n)}
    b=dict(sorted(b.items(), key = 
                lambda kv:(kv[1], kv[0]))) 

#    Remaining nodes
    for j in b:
        if((j!=source)):
            for i in range(0,n):
                if((i!=source)):
                    if ((w[i]>(w[j]+matrix[j,i])) & (matrix[j,i]!= 0)):
                        
                        w[i]=(w[j]+matrix[j,i])
                        prev[i]=j
                      

#   Safe Side Rep 
    for j in b:
        if((j!=source)):
            for i in range(0,n):
                if((i!=source) ):
                    if ((w[i]>(w[j]+matrix[j,i])) & (matrix[j,i]!= 0)):
                        
                        w[i]=(w[j]+matrix[j,i])
                        prev[i]=j
                      


root = Tk() 
root.title("DROUTER")
root.geometry("600x600")    
# #set window color
root['bg']='black'

label = Label(root, text = "\n---------Shortest Path---------",foreground="white",font="calibri",background="black")
label.pack()
  

mylist = Text(root,height=250,font="calibri",width=30,foreground="white",background="black", borderwidth=0,highlightthickness=0) 
mylist.pack(pady=20) 


print("\n---------Shortest Path---------")
dno=0
arr = np.transpose(np.nonzero(matrix[0]))
path = len(arr)


for i in range(0,n):
    if(matrix[0,i]!=0):
        if(i in chst ):
            path=path-1

dumd= drones
m = path if path<drones else drones
i=0
while(i<m):
    

    prev.fill(99999)
    w.fill(99999)
    w[source]= 0

    djik(source)
    
    if(w[sink]!=99999):
        dno=dno+1
        mylist.insert(END,"Drone {0}:\n".format(dno))
        print("Drone {0}:".format(dno))
        loc(sink,source)
        reached=0
        battery[dno-1],wgt= calc(battery[dno-1])
        route=[]
        if((wgt<99999) and (wgt>0)):
            mylist.insert(END,wgt)
            print(wgt)
            mylist.insert(END,"\nBattery: {0}%\n\n".format(battery[dno-1]))
            print("Battery: {0}%\n".format(battery[dno-1]))
        else:
            dno=dno-1
            drones=drones+1

       
    else:
        path=path-1

    i=i+1
    for j in range(i+1,len(arr)):
        if(taken[arr[j,0]]==1):
            path=path-1
    
    m = path if path<drones else drones

  

s= source
c = {x:w[x] for x in range(0,n)}
c=dict(sorted(c.items(), key = 
                lambda kv:(kv[1], kv[0]))) 



if(drones>path):
   
    for i in c:
      
        if((rem[i]==0) and (dno<dumd) ):
            taken.fill(0)
            prev.fill(99999)
            w.fill(99999)
            source = s
            w[source]= 0
            rem[source]=1

            djik(source)
            loc(i,source)
            dno=dno+1
            mylist.insert(END,"Drone {0}:\n".format(dno))
            print("Drones {0}:".format(dno))
            flag=1
            reached=0
            battery[dno-1],wgt =calc(battery[dno-1])
            route=[]
            if((wgt<99999) and (wgt>0)):
                a= wgt
            
                taken.fill(0)
                prev.fill(99999)
                w.fill(99999)
                source = i
                w[source]= 0
                rem[i]=1

                djik(source)
                loc(sink,source)
                reached=0
                battery[dno-1],wgt =calc(battery[dno-1])
                route=[]
                if((wgt<99999) and (wgt>0)):
                   
                    mylist.insert(END,a+wgt)
                    print(a+wgt)
                    
                    print("Battery: {0}%\n".format(battery[dno-1]))
                    mylist.insert(END,"\nBattery: {0}%\n\n".format(battery[dno-1]))
                    
                else:
                    dno=dno-1
                    drones=drones+1
    
            elif(wgt == 0):
                continue
            

            else:
                dno=dno-1
                drones=drones+1
            
            path=path+1

          
       
    for i in range(dno,dumd):
        mylist.insert(END,"Drone {0}:\nNo unique path".format(i+1))
        print("Drone {0}:\nNo unique path".format(i+1))
        red=red+1

    

if(red!=0):
    mylist.insert(END,"\n\nMin. Drones Req: {0}".format(dumd-red))
    print("\nMin. Drones Req: {0}".format(dumd-red))



gmap2.draw(pathy+"map50.html")
url= pathy+"map50.html"
webbrowser.open(url, new=new)

root.mainloop() 

