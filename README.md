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
5) **All Unique Routes plotted on another Google Map as the final output with a different colour for each traversed route.**

## Technology
* Python 
   * **NumPy**
   * **gmplot**
   * **webbrowser**
   * **Tkinter** for GUI
   * **pyshp**
   * **pandas**
   * **math**
* Shapefile (SHP)
* Keyhole Markup Language (KML)

## Implementation

### Modifications to the Dijkstra’s Algorithm
---

> We have used a modified version of the above algorithm which not only helps find the shortest path from **source to sink** but also does so while satisfying certain constraints such as covering the maximum area (**most number of nodes**) possible, rate of discharge of battery and visiting charging stations if required.

> We have used a modified **Euclidean** formula to calculate the distance between two points on the graph. Since we cannot directly use Euclidean because of the points being in (longitude, latitude) form instead of Cartesian coordinates(x, y), we had to modify it to find our distances in kilometers. 
> We have also made use free online converters like https://mygeodata.cloud/converter/kml-to-shp to convert our downloaded **KML file from Google Earth/Scribble Maps to SHP** files so they can be used by the shapefile module of Python.

#### Assumptions
> To cover maximum Area all Nodes must be visited **once** but not mandatory to visit **all** Charging Stations. Distance is calculated and not Time so time taken to charge any Drone is considered to be equal. Charging is considered to be **100%** at the start and same after visiting Charging Station.


