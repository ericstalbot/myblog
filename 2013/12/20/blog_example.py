




import cPickle
import matplotlib.pyplot as plt
import fiona.crs
import networkx

fig, ax = plt.subplots(1,1)


g = cPickle.load(open('mygraph.pickle'))
g.transform(fiona.crs.from_epsg(32617))
g.draw(ax, node_args = {'s':0}, edge_args = {'c':'0.5'})

origin, destination = '194912632', '195049052'
path = networkx.shortest_path(g, origin, destination)

x,y = g.xy(*path)
ax.plot(x,y, c = 'b', lw = 4)

scatter_args = dict(zorder = 10, c = 'orange', s = 80, edgecolor = 'none')

x,y = g.xy(origin)
ax.scatter(x,y, **scatter_args)

x,y = g.xy(destination)
ax.scatter(x,y, **scatter_args)

ax.set_ylim(4.802e6 + 1000, 4.802e6 + 2500)
ax.set_xlim(1.328e6 + 500, 1.328e6 + 1800)
ax.set_aspect('equal')

plt.savefig('interchange.png')
plt.close()


    
    
    
    
    
