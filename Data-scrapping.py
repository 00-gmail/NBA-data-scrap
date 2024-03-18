import pandas as pd
import requests
pd.set_option('display.max_columns', None)  # so we can see at L columns in a wide DataFrame
import time
import numpy as np


api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS'


headers = {'authority':'stats.nba.com',
'method':'GET',
'path':'/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS',
'scheme':'https',
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br, zstd',
'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
'Origin':'https://www.nba.com',
'Referer':'https://www.nba.com/',
'Sec-Ch-Ua':'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-site',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

r = requests.get(url=api_url,headers=headers).json()

cols = r['resultSet']['headers']



df_cols = ['Year','Season_type'] + cols

years= ['2012-13' , '2013-14' , '2014-15' , '2015-16' , '2016-17' , '2017-18' , '2018-19' , '2019-20' , '2020-21' , '2021-22']
season_types = ['Regular%20Season' , 'Playoffs']

df = pd.DataFrame(columns=df_cols)

begin_loop = time.time()

for y in years:
  for s in season_types :
    m_api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season='+y+'&SeasonType='+s+'&StatCategory=PTS'
    r = requests.get(url=m_api_url,headers=headers).json()
    df1 = pd.DataFrame( r['resultSet']['rowSet'], columns=cols)
    df2 = pd.DataFrame({'Year':[y for i in range(len(df1))],'Season _ type':[s for i in range(len(df1))]})
    df3 = pd.concat([df2,df1], axis=1)
    df = pd.concat([df,df3], axis=0)
    print(f'Finished scraping data from the {y} {s}')
    lag = np.random.uniform(low=5,high=10)
    print(f'...waiting {round(lag,1)} seconds...')
    time.sleep(lag)
print(f'Process completed! ! Total run time:{round(time.time()-begin_loop,1)} seconds')




df.to_excel('NBA_Data.xlsx', index=False)