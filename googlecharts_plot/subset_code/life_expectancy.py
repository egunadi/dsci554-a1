import pandas as pd
import csv

def pivot_life_expectancy_data():
    life_expectancy_filepath = '../../data/life_expectancy.original.csv'
    
    life_expectancy_df = pd.read_csv(life_expectancy_filepath, delimiter=',', encoding='utf-8')
    
    life_expectancy_df = life_expectancy_df[['Country or Area', 'Year(s)', 'Value']]
    
    life_expectancy_df = life_expectancy_df[life_expectancy_df['Value'].notna()]
    
    life_expectancy_df = pd.pivot_table(life_expectancy_df, 
                                        values = 'Value', 
                                        index=['Year(s)'], 
                                        columns = 'Country or Area').reset_index()
    
    life_expectancy_df = life_expectancy_df.rename(columns={'Year(s)': 'Year'})
    
    life_expectancy_df['Year'] = life_expectancy_df['Year'].astype(str)
    
    life_expectancy_df.to_csv('../subset_data/life_expectancy.processed.csv', 
                              encoding='utf-8', index=False,
                              quoting=csv.QUOTE_NONNUMERIC,
                              quotechar="'")

if __name__ == '__main__':
    pivot_life_expectancy_data()
