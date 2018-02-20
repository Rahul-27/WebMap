import folium
import pandas
data = pandas.read_excel("tour.xlsx",sheetname=0)
nam = data["Name"]
lat = data["Latitude"]
lon = data["Longitude"]
date = data["Built"]

def marker_color(dt):
    if 500 < dt < 1500:
        return 'green'
    elif 1500 <= dt < 1800:
        return 'orange'
    else:
        return 'red'

map = folium.Map([0, 0], zoom_start = 2.5, min_zoom = 2)
fg = folium.FeatureGroup(name = "Tourist spots")
for lt,ln,nm,dt in zip(lat,lon,nam,date):
    fg.add_child(folium.CircleMarker(location = [lt,ln], radius = 5, weight = 0.2, popup = nm, fill_opacity = 0.8, fill_color = marker_color(dt)))
fp = folium.FeatureGroup(name = "Population")
fp.add_child(folium.GeoJson(data =(open("world.json",'r', encoding="utf-8-sig")),
style_function = lambda x: {"fillColor" : "green" if x["properties"]["POP2005"] < 20000000
else "orange" if 20000000 <= x["properties"]["POP2005"] < 40000000
else "red"}))
map.add_child(fp)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Wbmap.html")
