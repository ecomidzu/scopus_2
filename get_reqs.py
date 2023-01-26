import pandas as pd
import numpy as np


def make_list():
    reqs = pd.read_excel(r"C:\Users\Миша\Desktop\reqs2.xlsx")
    a = []
    b = []
    for req in reqs['requests']:
        c = 'TRADE AND ' + 'AUTHKEY(' + req + ' AND NOT ' + '((' + ') OR ('.join(
            b) + '))) AND SUBJAREA(ECON OR BUSI OR SOCI)'
        print(c)
        a.append(c)
        b.append(req)
    return a

def new_project():
    return ['AUTHKEY(Sanctions) AND SUBJAREA(ECON)']