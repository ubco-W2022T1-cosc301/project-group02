import pandas as pd

# Function to load data
def load_data(path):
    raw_data = pd.read_csv(path)
    return raw_data;

# Function to only keep the necessary columns and remove NaN cells
def clean_data(dataframe):
    cleaned_df = dataframe[['country','year', 'cse', 'fccp', 'fse']]
    cleaned_df = cleaned_df.dropna()
    return cleaned_df

# Function to rename columns for ease of typing
def rename(dataframe):
    dataframe.rename(columns = {'coal_share_elec':'cse'})
    dataframe.rename(columns = {'fossil_cons_change_pct':'fccp'})
    dataframe.rename(columns = {'fossil_share_elec':'fse'})
    return dataframe
    
# Function to sort the dataframe from highest to lowest
def sort_by(dataframe, column_name):
    dataframe.sort_values(column_name, ascending = True)
    return dataframe

# Function that wraps together the method chains
def load_and_process(path):
    # Method Chain 1
    df1 = (
        pd.read_csv(path)
        .rename(columns = {'coal_share_elec':'cse'})
        .rename(columns = {'fossil_cons_change_pct':'fccp'})
        .rename(columns = {'fossil_share_elec':'fse'})
        .dropna()
    )
    # Method Chain 2
    df2 = (
        df1
        .sort_values('year', ascending = True)
    )
    # Call function to get rid of unnecessary columns
    df3 = clean_data(df2)
    return df3
