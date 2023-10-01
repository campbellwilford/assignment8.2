#Create a map that shows all the Big 12 schools (NCAA code 108) and their corresponding information as shown in the pictures.
#The link between the tow JSON files is the name of the university.
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

ncaa_infile = open('schools.geojson', 'r')
ncaa_data = json.load(ncaa_infile)

universities_infile = open('univ.json', 'r')
universities_data = json.load(universities_infile)

big_12_schools = []

for university in universities_data:
    if university['instnm'] == 'Big 12' and university['NCAA']['NAIA conference number football (IC2020)'] == '108':
        big_12_schools.append(university)

school_names = []
lats = []
lons = []
hover_texts = []

for school in big_12_schools:
    school_names.append(school['instnm'])
    lats.append(float(school['Latitude location of institution (HD2020)']))
    lons.append(float(school['Longitude location of institution (HD2020)']))
    hover_texts.append(f"Name: {school['NAME']}<br>City: {school['CITY']}<br>State: {school['STATE']}")

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': 10,
        'color': 'blue',
        'opacity': 0.7,
        'line': {'width': 0.5, 'color': 'white'},
    }
}]

layout = {
    'title': 'Big 12 Schools',
    'geo': {
        'showland': True,
        'showcoastlines': True,
        'projection': {'type': 'mercator'},
    }
}

fig = {'data': data, 'layout': layout}

outfile = open('big_12_schools_map.html', 'w')
offline.plot(fig, filename=outfile.name)

ncaa_infile.close()
universities_infile.close()
outfile.close()