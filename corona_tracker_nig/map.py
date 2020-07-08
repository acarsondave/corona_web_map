import folium
import pandas
import locale
locale.setlocale(locale.LC_ALL, '')

data = pandas.read_csv("covid_nigeria.txt")
state = list(data["STATE"])
el = list(data["Confirmed"])
lat = list(data["LAT"])
lon =list(data["LON"])
admission = list(data["Admission"])
deaths = list(data["Deaths"])
discharged = list(data["Discharged"])

html = """State: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Confirmed: %s cases<br> Admission: %s cases <br> Discharged: %s cases <br> Deaths: %s cases """

def colorize(elvation_pass):
    if elvation_pass < 1000:
        return "blue"
    elif elvation_pass >= 1000 and elvation_pass < 3000:
        return "orange"
    else:
        return "red"

map1 = folium.Map(location=[9.404974, 7.607418], zoom_start=7, tiles='Stamen Terrain')
fgvolc = folium.FeatureGroup(name="covid_nigeria")
for lati, long, elev, name, ad, dch, die in zip(lat,lon,el,state,admission,discharged,deaths):
    iFrame = folium.IFrame(html=html % (name, name, '{:n}'.format(elev),'{:n}'.format(ad), '{:n}'.format(dch), '{:n}'.format(die)), width=200, height=100)
    fgvolc.add_child(folium.Marker(location=[lati, long], popup=folium.Popup(iFrame), icon=folium.Icon(color=colorize(elev))))

fgpop = folium.FeatureGroup(name="Population")
fgpop.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map1.add_child(fgvolc)
map1.add_child(fgpop)
map1.add_child(folium.LayerControl())

map1.save('map1.html')
