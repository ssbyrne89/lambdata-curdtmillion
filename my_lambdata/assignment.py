from pandas import DataFrame

# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
# (Handle Washington DC and territories like Puerto Rico etc.)

def add_state_names(my_df):
    # TODO: add a column of corresponding state names
    
    return my_df

if __name__ == "__main__":
    
    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
