Building Blocks for a Web Map
=============================


.. author:: default
.. categories:: none
.. tags:: none
.. comments::


Here's an outline of how I build the bike ride web map:

The back end
------------

- I started out with the Vermont roads geospatial data set from VCGI. 
- I processed the data using Python scripts. 
  A major part of the processing was to translate the data
  into human-readable labels for road type and whether the 
  road is paved or not. Another part of the processing was 
  to assign an "A" node and a "B" node to each roadway segment. 
  This allows the segments to be connected together to
  form a network. 
- Then I uploaded the processed data to CartoDB. This web service 
  layers over PostGIS and provides a SQL API to query the roadway segments data 
  It also provides an interface to style the data using CartoCSS and 
  a JavaScript library to create map layers
  from the styled data for Leaflet.js. 
- The next step was to write a Python function for 
  getting the the shortest path along the network between 
  a pair of points. The function takes a pair of x,y coordinates;
  queries the CartoDB API to get the roadway segments in the 
  neighborhood as GeoJson features; 
  constructs a NetworkX graph using the "anode" 
  and "bnode" attributes of the features; inserts nodes
  for the starting and ending points; finds the shortest path 
  between the points; and then returns an array of x,y points
  giving the shape of the path.
- I then wrapped the shortest path function in a HTTP interface 
  using Flask. The inputs are passed as a HTTP GET parameter,
  and the outputs are returned as JSON. I then deployed the Flask web application 
  on pythonanywhere.com.
- The end result is a routing API that takes a series of waypoints
  as a parameter and returns the shape of the path connecting those
  points.

The front end
-------------

- I created a web page which features a Leaflet.js map,
  and used the CartoDB functions to add my road data as the main layer. 
  I then added interactions using pure JavaScript to allow 
  creating and editing the way points, and connected this user interface
  to the routing API using an asynchronous request.      
- I set up the Flask application on pythonanywhere.com 
  to serve the web page as a static
  template.
- The end result is a web application where users can create and 
  edit waypoints and then get the shape of the path connecting them.

Links
-----

- the web application: http://ericstalbot.pythonanywhere.com/
- project on github: https://github.com/ericstalbot/roadfollowing
  (includes the data processing scripts, path-finding function,
  Flask application, and web page source.)
      
- profile on CartoDB: https://ericstalbot.cartodb.com/me 
  (includes links to the road data and map)

- original road data: http://maps.vcgi.org/gisdata/vtrans/packaged_zips/TransRoad_RDS.zip