## scatterplot: price vs. review ratings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import altair as alt
load_listing = load_data('Listings.csv')
listing_data = clean_listing_data(load_listing)
alt.data_transformers.disable_max_rows()
scatterplot = alt.Chart(listing_data).mark_circle().encode(
    x=alt.X('review_scores_rating:Q', title='Review Ratings'),
    y=alt.Y('price:Q', title='Listing Prices')).properties(title='Price vs. Ratings', width=500, height=400)
