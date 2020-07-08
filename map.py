import folium
import json
import locale
locale.setlocale(locale.LC_ALL, '')

data = json.load(open('summary.json'))
x = 0
confirmed_location = data['confirmed']['locations']
death_location = data['deaths']['locations']
recovered_location = data['recovered']['locations']

html = """Country name:<br> <a href="https://www.google.com/search?q=%%22%s+corona+virus+count%%22" target="_blank">%s</a><br>
Province:<br> <a href="https://www.google.com/search?q=%%22%s+corona+virus+count%%22" target="_blank">%s</a> <br>
Confirmed Cases: %s cases <br> Death cases: %s cases <br> Recovery cases: %s cases"""

def colorize(elvation_pass):
    if elvation_pass < 100:
        return "blue"
    elif elvation_pass >= 500 and elvation_pass < 1000:
        return "orange"
    else:
        return "red"

map1 = folium.Map(location=[38.58, -99.09], zoom_start=3, tiles='Stamen Terrain')
fgvolc = folium.FeatureGroup(name="Corona_Tracker")
for elems, elems1, elems2 in zip(confirmed_location,death_location,recovered_location):
    lat = confirmed_location[x]['coordinates']['lat']
    lon = confirmed_location[x]['coordinates']['long']
    el = confirmed_location[x]['latest']
    name = confirmed_location[x]['country']
    province = confirmed_location[x]['province']
    deaths = death_location[x]['latest']
    recovered = recovered_location[x]['latest']
    x = x + 1
    iFrame = folium.IFrame(html=html % (name, name, province, province, '{:n}'.format(el), '{:n}'.format(deaths), '{:n}'.format(recovered)), width=200, height=100)
    fgvolc.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(iFrame), icon=folium.Icon(color=colorize(el))))


fgpop = folium.FeatureGroup(name="Population")
fgpop.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map1.add_child(fgvolc)
map1.add_child(fgpop)
map1.add_child(folium.LayerControl())

map1.save('index.html')
