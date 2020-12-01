import csv
import pandas as pd
import numpy as np

def target_to_csv(target):
    with open(target, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split("#") for line in stripped if line)
        with open('../csv/Targ.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Sentence', 'Target'))
            writer.writerows(lines)

def opinion_to_csv(opinion):
    with open(opinion, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split("#") for line in stripped if line)
        with open('../csv/Opi.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Sentence', 'Opinion'))
            writer.writerows(lines)

def column_from_dfT(csv_target):
    tar = []
    dfT = pd.read_csv(csv_target)
    sent = dfT['Sentence'].tolist()
    target = dfT['Target'].tolist()
    new_target = ['NA' if x is np.nan else x for x in target]
    for str in new_target:
        x = str.split()
        # print(x)
        tar.append(x)
    return sent, tar




def column_from_dfO(csv_opinion):
    op=[]
    dfO = pd.read_csv(csv_opinion)
    opinion = dfO['Opinion'].tolist()
    new_opinion = ['NA' if x is np.nan else x for x in opinion]
    for str in new_opinion:
        x = str.split()
        # print(x)
        op.append(x)
    return op



def polarity_lista(op, opinion_lexicon_positive, opinion_lexicon_negative):
    polarity = []
    for i in op:
        pol = []
        for j in i:
            with open(opinion_lexicon_positive) as f:
                with open(opinion_lexicon_negative) as f1:
                    if j in f.read():
                        pol.append('positive')
                    elif j in f1.read():
                        pol.append('negative')
                    else:
                        pol.append('NA')
        polarity.append(pol)
    return polarity


def process_lista_target(lista_target_estratti):
    n = len(max(lista_target_estratti, key=len))
    lista_target_estratti2 = [x + ['NA'] * (n - len(x)) for x in lista_target_estratti]
    return n, lista_target_estratti2


def process_lista_target_gold(lista_target_gold, n):
    lista_target_gold2 = [x + ['NA1'] * (n - len(x)) for x in lista_target_gold]
    return lista_target_gold2

def lista_correct_target(lista_target_estratti_P, lista_target_gold_P):
    list_tmp = []
    for x, y in zip(lista_target_estratti_P, lista_target_gold_P):
        a = set(x).intersection(y)
        list_tmp.append(a)

    list_correct_target = []
    for item in list_tmp:
        if item == set():
            list_correct_target.append('no')
        else:
            list_correct_target.append('si')
    x = 0
    for i in list_correct_target:
        if i == 'si':
            x = x+1
    return list_correct_target, x, list_correct_target.__len__()



def process_lista_polarity(lista_polarity_estratta):
    n = len(max(lista_polarity_estratta, key=len))
    # print(p)
    lista_polarity_estratta2 = [x + ['NA'] * (n - len(x)) for x in lista_polarity_estratta]
    return n, lista_polarity_estratta2


def process_lista_polarity_gold(lista_polarity_gold, n):
    lista_polarity_gold2 = [x + ['NA1'] * (n - len(x)) for x in lista_polarity_gold]
    return lista_polarity_gold2


def lista_corect_polarity(lista_polarity_estratta_P, lista_polarity_gold_P):
    list_tmp = []
    for x, y in zip(lista_polarity_estratta_P, lista_polarity_gold_P):
        a = set(x).intersection(y)
        list_tmp.append(a)
    # print(list)

    list_correct_polarity = []
    for item in list_tmp:
        if item == set():
            list_correct_polarity.append('no')
        else:
            list_correct_polarity.append('si')
    # print(list2.__len__())
    return list_correct_polarity






