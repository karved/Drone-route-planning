# Modifications to the Dijkstra’s Algorithm

We have used a modified version of the above algorithm which not only helps find the shortest path from source to sink but also does so while satisfying certain constraints such as covering the **maximum area (most number of nodes)** possible, rate of discharge of battery and visiting charging stations if required.

We have used a modified Euclidean formula to calculate the distance between two points on the graph. Since we cannot directly use Euclidean because of the points being in (longitude, latitude) form instead of Cartesian coordinates(x, y), we had to modify it to find our distances in kilometers. 
We have also made use free online converters like https://mygeodata.cloud/converter/kml-to-shp to convert our downloaded KML file from Google Earth/Scribble Maps to SHP files so they can be used by the shapefile module of Python.

### Assumptions  
To cover maximum Area all Nodes must be visited once but not mandatory to visit all Charging Stations. Distance is calculated and not Time so time taken to charge any Drone is considered to be equal. Charging is considered to be 100% at the start and same after visiting Charging Station.

## Cases 

![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/11.png) 

* Since there is a single Drone, it will cover the shortest path on the graph from Source to the Sink. With rate being Zero, it follows Dijkstra’s Algorithm.

* When Rate is high, the single Drone may or may not complete its path depending on edge weights as there is no charging station to recover it.

* The Drone when low on battery, will detour to its nearest charging stations. This may occur anytime during its course from original source to sink. Now to reach the charging station, it will apply the same Dijkstra's Algorithm to reach the closest charging station. After replenishing its battery, it will again apply the same Algorithm from Charging station to its original Sink. This way it will complete its route. There may be a case where reaching the charging station requires a lot of distance to be covered and it may fall back to the previous case and not complete its journey.  

![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/12.png)  

* There are multiple Drones now, rate is 0 so absence of Charging stations does not affect the planning. The first Drone will follow the route given by Dijkstra's Algorithm, *shortest path*. **The second Drone will follow the second shortest path from the outgoing edges of source**. If the source has N outgoing edges, all edges will lead to a unique path thus covering the maximum area possible. The third Drone will cover the third shortest path and so on.  

    If the number of Drones < N then shortest path outgoing from source in increasing order will be routed till limit reaches no. of Drones.   
    
    If Drones = N then all N outgoing routes from source will be routed.   
    
    If Drones > N then the algorithm will search from Nodes which *have not been visited at least once*. Every Drone is routed to those univisted Nodes using Dijkstra's Algorithm and then from those Nodes using the same algorithm, drone is routed to the original sink / destination.  

    If all nodes are visited at least once and Drones are still left to be routed, then those are redundant Drones as they wont have a *Unique Path*. Output will then consist of the Minimum Number of Drones required.

* When there is a rate of discharge and no charging station, the Drones may or may not cover their routes. Their incomplete nodes can be completed by other Drones if they have sufficient battery to sustain. The unvisited nodes will be routed the same way as the above case.

* When there are charging stations present, all cases are combined and lead to some complexity. Initial Drones are planned through increasing shortest routes, if they drain, they find the shortest path to the nearest charging station. They may or may not make it. Now after replenishing from the charging station they find the shortest path till the original sink. *If the sink is not visited even once*, it will find the shortest path to the sink. *If the sink has been visited once* using the same shortest route from that particular Charging station, *it will find an alternate shortest path covering univisted Nodes*.   

    If all nodes are visited once in the vicinity and the reach of the charging station, it will revert back to the *original shortest path route*.   
 
    Once the main source is done with outgoing edges, it will find routes for unvisited nodes. The same cases are followed if it drains out of battery in the path of reaching it. Goes to the charging station and continues.  

    Once all nodes are visited **Maximum Area is covered**. The remaining Drones are redundant and a minimum number of Drones is displayed.


### Note
When reaching a point where rate is too high or battery is insufficient to make it to any path for a particular Drone after considering all cases. The remaining Drones after it are not routed and the process ends.

## Example
![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/13.png) 


There are **3 Drones with a rate of 7% per unit**. The locations can be referred from the image.  Use Drone Route Planning from **A to H.
Charging Station Node D.**

![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/14.png) 

Drone 1 has taken the shortest path of the graph, **A→ B→ E→ H.**
Cost is 11 units. Battery remaining is 100 - (7 x 11) = 23%. Therefore remaining nodes are C,G,F.  

#### Note: It is not mandatory to visit charging stations.  

![alt text](https://github.com/karved/Drone-route-planning/blob/master/pics/15.png)  

Considering the second shortest path from A→ H is from C.                  
C→ G→ H. Weighs 15 units.  

Traversing node to node,   
A→ C, 2 units covered Battery = 100 - (7 x 2) = 86% .  
C→ G weights 10 units. Battery = 86 -(7x10) = 16%.  

Now, G→ H weight is 3 units. Battery, 16- (7x3) **< 0**. Therefore this route **can not** be taken. Drone 2 has to detour to its nearest Charging Station which is D at a distance of 1 unit.  

G→ D, 1 unit. Battery= 16 - 7 = 15%. Route can be taken. Reaching D, Battery is fully charged.  

Applying shortest path from D, path is D→ G→ H. Cost is 4 units. But G is **already visited** and so is E. The **unvisited** Node F is selected sacrificing the shortest path.  

D→ F → H , total 9 units. Battery= 100 - (7 x 9)= 37%.   

Final Path combining both is obtained, **A→ C → G→ D &  D→ F→ H**.  
Total = 22 units with 37% Battery.  

Now all the nodes are visited at least once, so Drone 3 is redundant.
**Hence Minimum number of Drones required is 2.**

