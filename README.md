# Drone Route Planning

### Problem Statement
---
 Planning a route (for **Shortest Time to cover Area**) and schedule of Drones for **Mapping** a given area.

 The **input** provided will be:
1) Map of area to be covered. (**Shapefile**) 
2) **Number** of drones. 
3) **Source** and **Sink** Locations 
4) Depreciation **Rate** (% per unit)
5) Location of automatic **Charging station**.

**Output** will be:
1) **Minimum** number of Drones required to map the area.
2) **All Unique Routes** taken by each drone.
3) Remaining **Battery** of each Drone after completing its journey.
4) A **Google Map** plotted with all **Nodes** and **Charging stations** and **edges** connecting them.
5) **All Unique Routes plotted on another Google Map as the final output with a different random colour for each traversed route.**

## Technology
* Python 
   * **NumPy**
   * **gmplot**
   * **pyshp**
   * **webbrowser**
   * **Tkinter** for GUI
   * **Pillow**
   * **pandas**
   * **math**
   * **random**
   * **os**
* Google Maps / Google Earth 
* Shapefile (SHP)
* Keyhole Markup Language (KML)

## Implementation

Algorithms used, Cases covered and Example can be found **[here](https://github.com/karved/Drone-route-planning/blob/master/Implementation.md)**.

## Screenshots 
![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/1.png)
|||
|--|--|
|![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/2.png)|![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/3.png)|
|![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/4.png)|![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/5.png)|

## Pre-setup
Follow these steps to convert any map into a **```.shp``` (Shapefile)** format :
1. Open Google Maps  
2. Go to **Your places →  MAPS →  CREATE MAP**   

3. Add a **Title**, **Layer** and **Plot** desired points on the map. 

4. Click on **Export to KML/KMZ**.  

5. Select the layer →  **Export as KML** →  **Download**.  
   A **```.kml```** file will be downloaded.  

6. Convert this file to **```.shp```**.  
   You can use online converters like https://mygeodata.cloud/converter/kml-to-shp

7. Download this  ```.shp``` file.

## Setup
1. Clone this repository or download zip.  
2. Open this repository on terminal. Navigate to [src](https://github.com/karved/Drone-route-planning/tree/master/src) folder by typing ```cd src```.

3. Type (if mentioned above **python modules** are not installed)  

   ```
   pip install numpy, gmplot, pyshp, pandas, Pillow
   ``` 
   
4. To run the project,
   ```
    python3 djik.py
   ```
5. All set.
