import matplotlib
matplotlib.use("Agg")
import networkx as nx
import numpy as np
import osmnx as ox
import settings 
import simulation

import matplotlib.backends.backend_agg as agg



from shapely.geometry import Point
import geopandas
import random

#location_point = (38.736828, -9.138222) #IST


#G = ox.graph_from_point(location_point, distance=1000, distance_type='bbox', network_type='all')
#ox.save_graphml(G, filename = 'Alameda.graphml')
#ox.save_gdf_shapefile(G, filename='Alameda-shape')

#G = ox.load_graphml('Alameda.graphml')
# G = ox.load_graphml('sanfrancisco.graphml')
# G = ox.load_graphml('lowermanhattan.graphml')
#G = ox.project_graph(G)

#para mudar a distancia (dist) convem mudar tb o dpi


    


""" 
# configure the inline image display
img_folder = 'images'
extension = 'png'
size = 600

library = ox.geocode("Palácio Galveias")
museum = ox.geocode("Instituto Superior Técnico")

listp=[library,museum]

place = 'Alameda_buildings'
point = (38.736828, -9.138222) # IST """

def make_plot(G):
        
    ec = ['grey' if data['oneway'] else '#e0e0e0' for u, v, key, data in G.edges(keys=True, data=True)]

    #ex
    #(38.7414116, -9.143627785022142)
    #lat = 38.7414116
    #lng = -9.143627785022142


    nodes, _ = ox.graph_to_gdfs(G)

    #generate random agent in map
    lng = random.uniform(nodes['x'].min(), nodes['x'].max())
    lat = random.uniform(nodes['y'].min(),nodes['y'].max())
    print(lat)
    print(lng)


    # get nearest node incident to nearest edge to reference point
    geom, u, v = ox.get_nearest_edge(G, (lat, lng))
    nn = min((u, v), key=lambda n: ox.great_circle_vec(lat, lng, G.nodes[n]['y'], G.nodes[n]['x']))
   
    fig, ax = ox.plot_graph(G, fig_height=settings.fig_height, node_size=0, edge_color=ec, edge_linewidth=0.5, show=False, close=False, save=False,
    filename=settings.place)



    ax.scatter(lng, lat, c='r', marker='x')
    ax.scatter(G.nodes[nn]['x'], G.nodes[nn]['y'], c='r', s=50, zorder=2)

    #plt.savefig(settings.place)
    ax.set_frame_on(False)
    ax.set_clip_on(False)
    fig.set_figheight(settings.fig_height)
    fig.set_figwidth(settings.fig_height)

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()

    return fig, ax, raw_data, size


    """  gdf = ox.footprints.footprints_from_point(point=settings.point, distance=settings.dist)
    #ec = ['grey' if data['oneway'] else '#e0e0e0' for u, v, key, data in G.edges(keys=True, data=True)]

    fig, ax = ox.plot_figure_ground(point=settings.point, dist=settings.dist, network_type=settings.network_type, 
    street_widths=settings.street_widths, save=False, show=False, close=True)

    fig, ax = ox.footprints.plot_footprints(gdf, fig=fig, ax=ax, color=settings.bldg_color, 
    set_bounds=False, save=True, show=False, close=True, filename=settings.place, dpi=settings.dpi)
    #plt.show() """


class map:
    def __init__(self):
        self.img_folder = 'images'
        self.extension = 'png'
        self.size = 600
        self.G = ox.graph_from_point(settings.point,distance=settings.dist, distance_type='bbox', network_type=settings.network_type)
        ec = ['grey' if data['oneway'] else '#e0e0e0' for u, v, key, data in self.G.edges(keys=True, data=True)]
        self.fig, self.ax = ox.plot_graph(self.G, fig_height=settings.fig_height, node_size=0, edge_color=ec, edge_linewidth=0.5, show=False, 
        close=False, save=False, filename=settings.place)
        nodes, _ = ox.graph_to_gdfs(self.G)
        self.max_x=nodes['x'].max()
        self.max_y=nodes['y'].max()
        self.min_x=nodes['x'].min()
        self.min_y=nodes['y'].min()
        print(self.max_x)
        print(self.max_y)

        #generate random agent in map
        x = random.uniform(self.min_x, self.max_x)
        y = random.uniform(self.min_y, self.max_y)


        #plt.savefig(settings.place)

        #self.G = ox.project_graph(self.G)
        # self.library = ox.geocode("Palácio Galveias")
        # self.museum = ox.geocode("Instituto Superior Técnico")

        # self.listp=[library,museum]

        #print(settings.point)


    def reload_frame(self):



        # get nearest node incident to nearest edge to reference point
        self.fig, self.ax, raw_data, size  = make_plot(self.G)
        return raw_data, size
        #Image('{}/{}.{}'.format(self.img_folder, settings.place, self.extension), height=self.size, width=self.size)

    




        








