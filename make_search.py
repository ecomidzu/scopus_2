from pybliometrics.scopus import ScopusSearch
from pybliometrics.scopus import AbstractRetrieval
import pandas as pd
import numpy as np
from get_reqs import make_list, new_project
from tqdm import tqdm
from make_conf import rework_config
import warnings
import requests

warnings.filterwarnings("ignore")

key = ''
reqs = 'TITLE-ABS-KEY-AUTH(Taxation systems) AND SUBJAREA(ECON) AND (PUBYEAR < 2020) AND (PUBYEAR > 2010)'
data = {'title': []}
df_total = pd.DataFrame(data)
n = 0
number_of_except = 0
try:
    s = ScopusSearch(reqs, subscriber=False)
    df = pd.DataFrame(s.results)
except:
    print('too big')
df.to_excel('query_res.xlsx')