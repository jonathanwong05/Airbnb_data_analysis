import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads the dataset from a csv file and returns a dataframe
    """
    df = pd.read_csv(file_path, encoding='latin-1', low_memory=False)
    return df

def clean_listing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses the listings dataset
    """
    # Drop duplicates
    df = df.drop_duplicates()

    # Convert host_since to datetime
    df['host_since'] = pd.to_datetime(df['host_since'], errors='coerce')

    # Convert binary columns to booleans
    boolean_cols = ['instant_bookable', 'host_is_superhost', 'host_has_profile_pic', 'host_identity_verified']
    for col in boolean_cols:
        # Convert to string, strip spaces, and replace 't'/'f'
        df[col] = (df[col].astype(str).str.strip().replace({'t': True, 'f': False}))
        # Convert to boolean if the replacement was successful
        df[col] = df[col].astype(bool)
    
    # Drop rows missing essential numeric columns
    essential_cols = ['price', 'latitude', 'longitude']
    df = df.dropna(subset=essential_cols)

    # Drop listings missing review scores
    review_cols = [
        'review_scores_rating',
        'review_scores_accuracy',
        'review_scores_cleanliness',
        'review_scores_checkin',
        'review_scores_communication',
        'review_scores_location',
        'review_scores_value'
    ]
    df = df.dropna(subset=review_cols)

    return df

def clean_reviews_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses the reviews dataset
    """
    # Drop duplicates
    df = df.drop_duplicates()

    # Convert 'date' to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop rows missing listing_id or date
    df = df.dropna(subset=['listing_id', 'date'])