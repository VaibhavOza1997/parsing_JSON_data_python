import json
import urllib.request
from datetime import datetime
import time

# {
#   "type": "FeatureCollection",
#   "metadata": {
#     "generated": 1762889628000,
#     "url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
#     "title": "USGS All Earthquakes, Past Week",
#     "status": 200,
#     "api": "1.14.1",
#     "count": 1628
#   },
#   "features": [
#     {
#       "type": "Feature",
#       "properties": {
#         "mag": 1.05,
#         "place": "6 km NNW of Lake Elsinore, CA",
#         "time": 1762888893650,
#         "updated": 1762889104336,
#         "tz": null,
#         "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ci40483818",
#         "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci40483818.geojson",
#         "felt": null,
#         "cdi": null,
#         "mmi": null,
#         "alert": null,
#         "status": "automatic",
#         "tsunami": 0,
#         "sig": 17,
#         "net": "ci",
#         "code": "40483818",
#         "ids": ",ci40483818,",
#         "sources": ",ci,",
#         "types": ",nearby-cities,origin,phase-data,scitech-link,",
#         "nst": 17,
#         "dmin": 0.04499,
#         "rms": 0.15,
#         "gap": 94,
#         "magType": "ml",
#         "type": "earthquake",
#         "title": "M 1.1 - 6 km NNW of Lake Elsinore, CA"
#       },
#       "geometry": {
#         "type": "Point",
#         "coordinates": [-117.3468333, 33.7186667, 3.07]
#       },
#       "id": "ci40483818"
#     },

#Output : Date&time(formated) | Place(CA) | Magnitude
now = int(time.time() * 1000)
with urllib.request.urlopen('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson') as response:
    json_data = response.read().decode('utf-8')
    data = json.loads(json_data)
    for ft in data['features']:
        p=ft['properties']
        place=p['place']
        mag=p['mag']
        epoch_time=p['time']
        seven_days = 7 * 24 * 60 * 60 * 1000
        cutoff = now - seven_days
        if ("California" in place or ", CA" in place) and epoch_time>=cutoff:
            dt=datetime.fromtimestamp(epoch_time / 1000)
            formatted_time=dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            print(f"{formatted_time} | {place} | M {mag}")
#print(json_data)