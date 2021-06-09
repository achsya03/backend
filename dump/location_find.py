#load_ext autotime
import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import plotly_express as px
import tqdm
from tqdm._tqdm_notebook import tqdm_notebook

class Location_Find():
    #neighbourhood
    def find(self, lat, long):
        locator = Nominatim(user_agent="myGeocoder")
        coordinates = str(lat)+", "+str(long)
        location = locator.reverse(coordinates)
        result = location.raw['address']
        
        return result