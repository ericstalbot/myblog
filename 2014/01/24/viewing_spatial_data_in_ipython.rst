Viewing Spatial Data in IPython
===============================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::


I do a lot of geospatial analysis for my work in transportation. My usual workflow
includes manipulating and analyzing data using IPython, and then viewing the
data by creating matplotlib plots, like this one:

  .. image:: plot.png

However, I frequently have found myself writing data to disk so I could explore 
it more interactively using QGIS. And more recently, I've been creating one-off
HTML documents to view my data in slippy maps. Which got me thinking - how could you
combine the great tools of Python and IPython with the ability to interactively
explore data like you do in a desktop GIS or a web map?

Well, it turned out to be a lot easier than I expected. IPython is already
set up to render objects as HTML. All you have to do is provide a `_repr_html_`
method which returns an HTML string. So I wrote a class that is initialized
with a mapping in geojson format, and that has a `_repr_html_` method that returns
an HTML web map powered by Leaflet's TileLayer and GeoJSON objects. So after 
about 30 minutes and 60 lines (including a HTML template) this is what I had:

  .. image:: webmap.png
           
Check out what_ on github.

.. _what: https://gist.github.com/ericstalbot/8605945



 








.. geo interface https://gist.github.com/sgillies/2217756

   geojson http://geojson.org/geojson-spec.html

   folium https://github.com/wrobstory/folium

   leaflet http://leafletjs.com/

   integrating objects http://ipython.org/ipython-doc/stable/config/integrating.html#rich-display

   shapely

   fiona

   bburky http://nbviewer.ipython.org/gist/bburky/7763555/folium-ipython.ipynb

   Brianna Laugher https://github.com/pfctdayelise/dapbook