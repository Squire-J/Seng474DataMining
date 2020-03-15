from pyephem_sunpath.sunpath import sunpos
from datetime import datetime

def FetchLabel():
    thetime = datetime(2018, 5, 23, 13)
    lat = 28.6
    lon = 77.2
    tz = 5.5

    alt, azm = sunpos(thetime, lat, lon, tz, dst=False)
    print(alt, azm)s