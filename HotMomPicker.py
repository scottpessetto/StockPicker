
#%%
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd


#%%
df = data.get_data_yahoo(['COP','XOM'],
                        start='2019-01-01',
                        end='2019-02-28')


#%%
df['Adj Close'].plot()


#%%
wiki_tick = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')


#%%
table = wiki_tick[0]
header = table.iloc[0]
wiki_slice = table[1:]
corrected_wiki = wiki_slice.rename(columns=header)
corrected_wiki


#%%
#quandl stock list
url = 'https://s3.amazonaws.com/quandl-production-static/end_of_day_us_stocks/ticker_list.csv'
c=pd.read_csv(url)
stock_list = c.Ticker
#Nasdaq stock list
url = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download'
c=pd.read_csv(url)
stock_list = c.Symbol


#%%
stock_list=corrected_wiki.Symbol
df_test = data.get_data_yahoo(stock_list,
                        start='2000-01-01',
                        end='2019-02-04')


#%%
adj_close_SP500 = df_test['Adj Close']
roller = adj_close_SP500.pct_change(periods=30)
roller = roller.loc['2019-01-01':]

roller


#%%
def momentum_picker(stock_df, 
                    start_cash = 10000,
                    start_date = '2016-01-02', 
                    window=30):
    
    rolling = stock_df.pct_change(periods=window)

    rolling = rolling.loc[start_date:, :]
    
    row_count = len(rolling)
    
    num_runs = row_count // window
    
    for x in range(1, num_runs): #might need to add +1 to num runs
        num_days = x * window
        print(rolling.iloc[num_days - 1].idxmax(),rolling.iloc[num_days - 1].max())
        company = rolling.iloc[num_days - 1].idxmax()
        date = rolling.index[num_days - 1]
        print(date)
        temp_rolling =  rolling[company]
        
        print(temp_rolling.iloc[num_days+window -1])
        
        start_cash = start_cash* (1+ temp_rolling.iloc[num_days+window -1])
        
        #print(rolling.iloc[num_days])
    print('\n End Cash: ' + str(start_cash))


#%%
momentum_picker(adj_close_SP500, 
                start_date='2017-01-01',
                window = 47)


#%%
#OPTOMOZE A FUNCTION


#%%
#Russel isharese index
url = 'https://www.ishares.com/us/products/239714/ishares-russell-3000-etf/1467271812596.ajax?fileType=csv&fileName=IWV_holdings&dataType=fund'
c=pd.read_csv(url, skiprows=9)
#stock_list = c.Ticker


#%%
c


