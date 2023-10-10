
[![YT](https://i.ytimg.com/vi/MBoe-P0fPRY/maxresdefault.jpg)](https://www.youtube.com/watch?v=MBoe-P0fPRY)
[https://www.youtube.com/watch?v=MBoe-P0fPRY]()

Neste vídeo, você aprenderá como raspar as odds do site 22bet.com e salvar esses dados em 
um arquivo do Excel para fins de arbitragem em apostas esportivas. O código Python utilizado 
no vídeo permite extrair informações relevantes das odds de futebol da 22bet.com e organizá-las em um formato conveniente.

## Pacotes para instalar: pip install selenium seleniumbase PrettyColorPrinter a-selenium2df bs4 lxml

## para Excel: pip install "pandas[excel]"

Nosso "código de base" que usamos em todos os vídeos

```python
import re
import time
from time import sleep
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
```



Se você deseja mais informações ou tutoriais detalhados sobre como usar esse código para arbitragem de apostas, não hesite em deixar 
seus comentários ou perguntas abaixo. Esperamos que este vídeo seja útil para você no mundo das apostas esportivas e na busca
por oportunidades de arbitragem. Lembre-se sempre de jogar com responsabilidade e boas apostas! 🔥💰✨

Inscreva-se no canal para mais conteúdo relacionado a tecnologia e apostas esportivas!
