## visual 1: scatter
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import altair as alt
load_listing = load_data('Listings.csv')
listing_data = clean_listing_data(load_listing)
alt.data_transformers.disable_max_rows()
scatter(listing_data,'review_scores_rating','price')

