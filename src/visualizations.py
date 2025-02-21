## scatter plot to show the price correlation with the guest satisfaction (e.g., price vs. ratings)
def scatter(df, x_key, y_key):
    return alt.Chart(df).mark_circle().encode(
        x=alt.X(x_key, title=x_key),
        y=alt.Y(y_key, title=y_key)
    ).properties(title=f'{x_key} vs. {y_key}', width=500, height=400)
    
## geospatial heatmap to visualize high-and-low priced locations
def geospatial_hm(data,lat,long,x):
    # base map centered around the mean latitude and longitude
    hm = folium.Map(location=[data[lat].mean(), data[long].mean()], zoom_start=12)
    # map layer
    heat_data = list(zip(data[lat], data[long], data[x]))
    HeatMap(heat_data, radius=10, blur=15, max_zoom=1).add_to(hm)
    return hm
