import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.espncricinfo.com/series/8048/scorecard/1175356"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)

# Get the title
title = soup.title.text
title = title[0:title.find(',')]
print(title)
text = soup.get_text()
body = soup.body


# writing into the file

body.write('D:/sample file.txt')