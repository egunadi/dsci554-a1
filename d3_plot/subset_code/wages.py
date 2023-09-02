import pandas as pd

def pivot_wages_data():
    wages_filepath = '../../data/wages.original.csv'
    
    wages_df = pd.read_csv(wages_filepath, delimiter=',', encoding='utf-8')
    
    wages_df = wages_df[['Year', 'Sex', 'Value']]
    
    wages_df = wages_df[wages_df['Sex'].isin(['Men', 'Women'])]
    
    wages_df = pd.pivot_table(wages_df, 
                              values = 'Value', 
                              index = ['Year'], 
                              columns = 'Sex').reset_index()
    
    wages_df = wages_df.rename(columns={'Year': 'year',
                                        'Men': 'men',
                                        'Women': 'women'})
    
    wages_df.to_csv('../subset_data/wages.processed.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    pivot_wages_data()
