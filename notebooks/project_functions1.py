import pandas as pd
import numpy as np

# Function to reset index and drop the index column
def reset_index(dataframe):
    dataframe = dataframe.reset_index(drop=True)
    return dataframe

# Function to produce master electricity dataframe
def electricitymaster(path):
    
    # Load data
    df = pd.read_csv(path)
    # Create dataframe with desired columns
    df_1 = df[["year", "country", "population", "gdp"]]
    # Create another dataframe with columns that contain the string 'elec'
    df_2 = df.loc[:, df.columns.str.contains("elec")]
    
    # Method Chain 1 (create master electricity dataframe)
    df_electricity = (
        pd.concat([df_1, df_2], join='outer', axis=1)
        .dropna(subset=["electricity_generation"])
        .dropna(axis=0, thresh=5)
        .dropna(subset=["population"])
    )
    
    # Remove unwanted data entries and reset index)
    df_electricity = df_electricity[df_electricity["country"].str.contains("World|Asia|income|America|Europe|Africa|Oceania")==False]
    df_electricity = reset_index(df_electricity)
    
    return df_electricity

# Function to produce the electricity comparison dataframe
def electricitycomp(path):
    
    # Call the electricity master function
    df_electricity = electricitymaster(path)

    # Method Chain 2 (create electricity comparison dataframe)
    df_comp = (
        df_electricity[["year", "country", "population", "gdp", "carbon_intensity_elec", "low_carbon_electricity", "low_carbon_elec_per_capita", "low_carbon_share_elec", "electricity_generation", "per_capita_electricity", "electricity_demand"]]
        .rename(columns={"year" : "Year", "country" : "Country", "population" : "Population", "gdp" : "GDP", "carbon_intensity_elec" : "Carbon Intensity", "low_carbon_electricity" : "Low Carbon Electricity", "low_carbon_elec_per_capita" : "Per Capita Low Carbon", "low_carbon_share_elec" : "Share from Low Carbon Sources", "electricity_generation" : "Electricity Generation", "per_capita_electricity" : "Per Capita Generation", "electricity_demand" : "Electricity Demand"})
    )
    
    # Remove rows from prior to the year 2000
    df_comp = df_comp[df_comp["Year"] >= 2000]
    # Add a new column for per capita electricity demand converted from terawatt-hours to kilowatt-hours
    df_comp["Per Capita Demand"] = (df_comp["Electricity Demand"] * 1e9) / df_comp["Population"]
    # Call reset index function
    df_comp = reset_index(df_comp)
    
    return df_comp

# Function to produce the electricity comparison mean values dataframe
def electricitymean(path):
    
    # Call the electricity mean function
    df_comp = electricitycomp(path)
    
    # Further widdle down dataframe to look at the mean values from 2016-2020
    df_mean = df_comp[df_comp["Year"] >= 2016]
    df_mean = df_mean[df_mean["Year"] <= 2020]
    
    # Find the mean values over the 5 year span for each country
    df_mean = df_mean.groupby(["Country"], as_index=False).mean()
    
    # Sort according to per capita electricity generation
    df_mean = df_mean.sort_values(["Per Capita Generation"], ascending=False)
    
    # Call function to reset index
    df_mean = reset_index(df_mean)
    
    return df_mean

# Function to produce the electricity mix dataframe
def electricitymix(path):
    
    # Call the electricity master function
    df_electricity = electricitymaster(path)

    # Create dataframe with desired columns
    df_3 = df_electricity[["year", "country"]]
    # Create another dataframe with columns that contain the string 'elec_per_capita'
    df_4 = df_electricity.loc[:, df_electricity.columns.str.contains("elec_per_capita")]
    
    # Method Chain 3 (create energy mix dataframe)
    df_elecmix = (
        pd.concat([df_3, df_4], join='outer', axis=1)
        .drop(columns=["other_renewables_elec_per_capita", "renewables_elec_per_capita", "low_carbon_elec_per_capita"])
        .rename(columns={'year' : 'Year', 'country' : 'Country'})
    )
    
    # Simplify column labels
    df_elecmix.columns = df_elecmix.columns.str.replace('_elec_per_capita', '')
    
    # Keep only the top 10 countries and remove all other data entries
    df_elecmix = df_elecmix[df_elecmix["Country"].str.contains("Iceland|Norway|Bahrain|Kuwait|Canada|Qatar|Sweden|United Arab Emirates|United States|Finland")==True]
    df_elecmix = df_elecmix[df_elecmix["Country"].str.contains("United States Virgin Islands")==False]
    
    # Convert columns to rows using pd.melt
    df_elecmix = pd.melt(df_elecmix, id_vars=["Year", "Country"], value_vars=["biofuel", "coal", "fossil", "gas", "hydro", "nuclear", "oil", "other_renewables_exc_biofuel", "solar", "wind"], var_name="Electricity Mix", value_name="Per Capita Electricity (KW-hrs)")
    
    # Filter dataset and reset index
    df_elecmix = df_elecmix[df_elecmix["Year"] >= 2000]
    df_elecmix = df_elecmix[df_elecmix["Per Capita Electricity (KW-hrs)"] != 0]
    df_elecmix = df_elecmix.dropna(subset=["Per Capita Electricity (KW-hrs)"])
    df_elecmix = reset_index(df_elecmix)
    
    return df_elecmix