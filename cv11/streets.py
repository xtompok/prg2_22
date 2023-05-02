import geopandas as gp
import networkx as nx
import matplotlib.pyplot as plt
from math import hypot

gdf = gp.read_file("streets.geojson")
gdf.to_crs(epsg=5514,inplace=True)

G = nx.Graph()

for (idx,feature) in gdf.iterrows():
	if feature.geometry.geometryType() != "LineString":
		continue
	coords = feature.geometry.coords
	print(list(coords))
	mempoint = coords[0]
	for point in coords[1:]:
		length = hypot(point[0]-mempoint[0],point[1]-mempoint[1])
		G.add_edge(mempoint, point, index=idx, weight=length)
		mempoint = point

print(nx.info(G))
T = nx.minimum_spanning_tree(G, weight="weight")
nx.draw(G,with_labels = False, pos = {n: [n[0],n[1]] for n in list(G.nodes)})
nx.draw(T,with_labels = False, edge_color = "red", pos = {n: [n[0],n[1]] for n in list(G.nodes)})
plt.show()