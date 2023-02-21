import requests
import pandas as pd
from pybliometrics.scopus import AbstractRetrieval
from tqdm import tqdm
import time
import warnings
from make_conf import rework_config

key = ''
rework_config(key)
warnings.filterwarnings("ignore")
new = pd.read_excel(r'C:\Users\misha\Downloads\Telegram Desktop\total_result.xlsx')
number_of_except=0
df_total = pd.DataFrame()
df_med = pd.DataFrame()
i=0
n=0
start = time.time()
for eid in tqdm(new['eid']):
    ab = AbstractRetrieval(eid, view='META')
    try:
        rrr = ab.__dict__
        r1 = {}
        for key in rrr:
            r1[key] = [rrr[key]]
        df_inter = pd.DataFrame.from_dict(r1)
    except:
        print(ab)
        number_of_except += 1
        continue
    df_total = pd.concat([df_total, df_inter])
    df_med = pd.concat([df_med, df_inter])
    if i % 100 == 0 or i == new.shape[0] - 1:
        sta_1 = time.time() - start
        print('Общее время обработки, секунд: ', sta_1)
        df_med.to_excel('med_base_' + str(n) + '.xlsx')
        n += 1
        df_med = pd.DataFrame()
    i+=1
    df_total.to_excel('base.xlsx')
print('Общее время обработки результатов, секунд: ', time.time()-start)
print('Общее кол-во ошибок:', number_of_except)