"""Main module."""
import ipyleaflet

class Map(ipyleaflet.Map):
    def __init__(self, center=[20, 0], zoom=2, **kwargs):
        super().__init__(center=center, zoom=zoom, **kwargs)
        self.add_control(ipyleaflet.LayersControl())

        def add_tile_layer(self, url, name, attribution):
            tile_layer = ipyleaflet.TileLayer(url=url, name=name, attribution=attribution)
            self.add_layer(tile_layer)

        def add_basemap(self, name):
            if isinstance(name, str):
                basemap = eval(f"basemaps.{name}")
                self.add(basemap)
            else:
                self.add(name)

