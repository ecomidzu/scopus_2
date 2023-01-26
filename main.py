from pybliometrics.scopus import ScopusSearch
from pybliometrics.scopus import AbstractRetrieval
import pandas as pd
import numpy as np
import time
from get_reqs import make_list, new_project
from tqdm import tqdm
from make_conf import rework_config
import warnings
warnings.filterwarnings("ignore")


all_start = time.time()
rework_config('88cc291ce61bc3fc47719150c98cd579')
#095077ce05f051edc5d39203344338ae API_key
reqs = make_list()
data = {'title': []}
df_total = pd.DataFrame(data)
def isNaN(num):
    return num != num
num_of_reqs = []
n = 0
number_of_except = 0
for g in range(32,len(reqs)):
    start = time.time()
    sta_1 = start
    try:
        s = ScopusSearch(reqs[g], subscriber=False)
        print('Время на запрос, секунд: ', time.time()-start)
        df = pd.DataFrame(s.results)
    except:
        s1 = ScopusSearch(reqs[g] + 'AND (PUBYEAR > 2014)', subscriber=False)
        print('Время на запрос 1, секунд: ', time.time() - start)
        s2 = ScopusSearch(reqs[g] + 'AND (PUBYEAR < 2015)', subscriber=False)
        print('Время на запрос 3, секунд: ', time.time() - start)
        df1 = pd.DataFrame(s1.results)
        df2 = pd.DataFrame(s2.results)
        df = pd.concat([df1, df2])
    num_of_reqs.append(df.shape[0])
    num_of_reqs_pd = pd.DataFrame(num_of_reqs)
    num_of_reqs_pd.to_excel('num_of_reqs.xlsx')
    df_med = pd.DataFrame()
    for i in tqdm(range(df.shape[0])):
        df_inter = pd.DataFrame()
        try:
            ab = AbstractRetrieval(df['eid'][i], view='META')
        except:
            try:
                ab = AbstractRetrieval(df['doi'][i], view='META')
            except Exception as e:
                print(e)
                number_of_except +=1
                continue
        try:
            rrr = ab.__dict__
            r1 = {}
            for key in rrr:
                r1[key] = [rrr[key]]
            df_inter = pd.DataFrame.from_dict(r1)
        except:
            number_of_except += 1
            continue
        df_total = pd.concat([df_total, df_inter])
        df_med = pd.concat([df_med, df_inter])
        if i%100 == 0 or i == df.shape[0]-1:
            sta_1 = time.time() - start
            print('Общее время обработки, секунд: ', sta_1)
            df_med.to_excel('med_base_' + str(n) + '.xlsx')
            n+=1
            df_med = pd.DataFrame()
    print(df.shape[0])
    if df.shape[0] != 0:
        df_total.to_excel('base_meta_' + reqs[g][0:30] + '.xlsx')
    df_total = pd.DataFrame(data)
    print('Общее время обработки результатов, секунд: ', time.time()-start)
    print('Общее кол-во ошибок:', number_of_except)
print('Процесс завершён за время, секунд: ', time.time()-all_start)
print('Общее кол-во ошибок:', number_of_except)