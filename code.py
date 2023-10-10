import os
import re
import time
from time import sleep,time
import bs4
from seleniumbase import Driver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from PrettyColorPrinter import add_printer

add_printer(1)


def obter_dataframe(query="*"):
    df = pd.DataFrame()
    while df.empty:
        df = get_df(
            driver,
            By,
            WebDriverWait,
            expected_conditions,
            queryselector=query,
            with_methods=True,
        )
    return df


driver = Driver(uc=True)
sleep(5)
driver.get("https://22bet.com/br/line/football/1268397-brazil-campeonato-brasileiro-serie-a")
sleep(5)
pasta=r'c:\odds_22betcom'
os.makedirs(pasta,exist_ok=True)
while True:
    try:
        df=obter_dataframe(query="div.c-events__item.c-events__item_col")
        df=df.aa_innerHTML.apply(bs4.BeautifulSoup).apply(lambda soup: [x.text.strip() for x in soup.find_all('span', class_='c-events__team')] + [x.text.strip() for x in soup.find_all('span', class_='c-bets__inner')][:3]).apply( lambda q: q if len(q)==5 else pd.NA).dropna().apply( lambda x: x if all([re.match(r'^\d+\.\d+$',y) for y in x[2:]]) else pd.NA).dropna().apply(pd.Series).rename( columns={0: 'team1_nome', 1: 'team2_nome' , 2: 'team1', 3: 'empate', 4: 'team2'}).astype({'team1': 'Float64', 'empate': 'Float64', 'team2': 'Float64'}).reset_index(drop=True)
        nome_arquivo = os.path.join(pasta, str(time())+'.xlsx')
        print(nome_arquivo)
        df.to_excel(nome_arquivo)
    except Exception as e:
        print(e)
