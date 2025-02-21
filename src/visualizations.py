## scatter plot to show the price correlation with the guest satisfaction (e.g., price vs. ratings)
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import altair as alt
load_listing = load_data('Listings.csv')
listing_data = clean_listing_data(load_listing)
alt.data_transformers.disable_max_rows()
scatterplot = alt.Chart(listing_data).mark_circle().encode(
    x=alt.X('review_scores_rating:Q', title='Review Ratings'),
    y=alt.Y('price:Q', title='Listing Prices')).properties(title='Price vs. Ratings', width=500, height=400)
# scatterplot

## geospatial heatmap to visualize high-and-low priced locations
import pandas as pd
import folium
from folium.plugins import HeatMap
geospatial = listing_data[['latitude', 'longitude', 'price']].dropna()
# base map centered around the mean latitude and longitude
hm = folium.Map(location=[geospatial['latitude'].mean(), geospatial['longitude'].mean()], zoom_start=12)
# map layer
heat_data = list(zip(geospatial['latitude'], geospatial['longitude'], geospatial['price']))
HeatMap(heat_data, radius=10, blur=15, max_zoom=1).add_to(hm)
# hm
