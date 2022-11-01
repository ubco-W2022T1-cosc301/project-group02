import pandas as pd

# Function to load data
def load_data(path):
    raw_data = pd.read_csv(path)
    return raw_data;

# Function to only keep the necessary columns and remove NaN cells
def clean_data(dataframe):
    cleaned_df = dataframe[['country', 'year', 'coal_cons_change_pct', 'coal_cons_change_twh', 'coal_cons_per_capita', 'coal_consumption', 'coal_elec_per_capita', 'coal_electricity', 'coal_prod_change_pct', 'coal_prod_change_twh', 'coal_prod_per_capita', 'coal_production', 'coal_share_elec', 'coal_share_energy']]
    cleaned_df = cleaned_df.dropna()
    return cleaned_df

# Function to create a data frame for 1990 values
def data_1990(path):
    df = load_data(path)
    df = clean_data(path)
    df = df.loc[df["year"] == 1990]
    return df

# Function to create a data frame for 2018 values
def data_1990(path):
    df = load_data(path)
    df = clean_data(path)
    df = df.loc[df["year"] == 2018]
    return df


# Function that wraps together the method chains
def load_and_process(path):
    # Method Chain 1
    df1 = (
        pd.read_csv(path)[['country', 'year', 'coal_cons_change_pct', 'coal_cons_change_twh', 'coal_cons_per_capita', 'coal_consumption', 'coal_elec_per_capita', 'coal_electricity', 'coal_prod_change_pct', 'coal_prod_change_twh', 'coal_prod_per_capita', 'coal_production', 'coal_share_elec', 'coal_share_energy']]
        .dropna()
    )
    # Method Chain 2
    df2 = (
        df1
        .rename(columns={'year' : 'Year', 'country' : 'Country'})
        .rename(columns={'coal_cons_change_pct' : 'Annual percentage change in coal consumption', 'coal_cons_change_twh' : 'Annual change in coal consumption, measured in terawatt-hours'})
        .rename(columns={'coal_cons_per_capita' : 'Per capita primary energy consumption from coal, measured in kilowatt-hours', 'coal_consumption' : 'Primary energy consumption from coal, measured in terawatt-hours'})
        .rename(columns={'coal_elec_per_capita' : 'Per capita electricity generation from coal, measured in kilowatt-hours', 'coal_electricity' : 'Electricity generation from coal, measured in terawatt-hours	'})
        .rename(columns={'coal_prod_change_pct' : 'Annual percentage change in coal production', 'coal_prod_change_twh' : 'Annual change in coal production, measured in terawatt-hours'})
        .rename(columns={'coal_prod_per_capita' : 'Per capita coal production, measured in kilowatt-hours', 'coal_production' : 'Coal production, measured in terawatt-hours'})
        .rename(columns={'coal_share_elec' : 'Share of electricity generation that comes from coal', 'coal_share_energy' : 'Share of primary energy consumption that comes from coal'})
        .sort_values('Year', ascending = True)
    )
    return df2
  