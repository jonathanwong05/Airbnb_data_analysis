# all imports
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import altair as alt
import pandas as pd
import folium
from folium.plugins import HeatMap

load_listing = load_data('Listings.csv')
listing_data = clean_listing_data(load_listing)
alt.data_transformers.disable_max_rows()

## visual 1: scatter
scatter(listing_data,'review_scores_rating','price')
## visual 2: geospatial heatmap
geospatial_hm(listing_data,'latitude','longitude','price')
