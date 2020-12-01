import csv
import pandas as pd
import re
import numpy as np
from operator import itemgetter



def rimpiazza_caratteri_inutili(file_Originale):
    # Read in the file
    with open(file_Originale, 'r') as file:
        filedata = file.read()

    # Replace dei diversi caratteri, non utili
    filedata = filedata.replace('?', '.')
    filedata = filedata.replace('!', '.')
    filedata = filedata.replace(';', '')
    filedata = filedata.replace(',', '')
    filedata = filedata.replace(':', '.')
    filedata = filedata.replace('"', '')

    # scrive il file precedente in un altro privato dei caratteri rimpiazzati
    with open('../processing_fileOriginale/Nikon coolpix 4300-Copia.txt', 'w') as file:
        file.write(filedata)

def rimozione_titoli_t(file_originale_caratteri_rimpiazzati):
    # rimuovi i titoli denominati con [t] dal file
    file1 = open(file_originale_caratteri_rimpiazzati)
    file2 = open('../processing_fileOriginale/Nikon coolpix 4300.Copia2.txt', 'w')

    for line in file1.readlines():
        if not (line.startswith('[t]')):
            # print(line)
            file2.write(line)
    file2.close()
    file1.close()

def trasforma_in_csv(file_originale_processato):
    with open(file_originale_processato, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split("##") for line in stripped if line)
        with open('../csv/Gold.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Target-Polarity', 'Sentence'))
            writer.writerows(lines)


def trasforma_csv_in_df_colonne_to_list(file_csv):
    dfP = pd.read_csv(file_csv)
    sentence = dfP['Sentence'].tolist()
    target_polarity = dfP['Target-Polarity'].tolist()
    new_target_polarity = ['NA1' if x is np.nan else x for x in target_polarity]
    return sentence, new_target_polarity


def process_list_target_polarity(target_polarity):
    list_target_polarity = []
    for str in target_polarity:
        x = str.split()
        list_tmp = []
        for j in x:
            y = j.split('[')
            list_tmp.append(y)
        list_target_polarity.append(list_tmp)
    return list_target_polarity


def listaTarget_from_listaTargetPolarity(list_target_polarity):
    lista_target = []
    for k in list_target_polarity:
        lista_target_tmp = []
        for ind in k:
            a = itemgetter(0)(ind)
            lista_target_tmp.append(a)
        lista_target.append(lista_target_tmp)
    return lista_target


def listaPolarity_from_listaTargetPolarity(list_target_polarity):
    lista_polarity = []
    for kk in list_target_polarity:
        lista_polarity_tmp = []
        for ind1 in kk:
            index = 1
            if len(ind1) > index:
                b = itemgetter(1)(ind1)
                lista_polarity_tmp.append(b)
            else:
                lista_polarity_tmp.append('NA1')
        lista_polarity.append(lista_polarity_tmp)

    lista_polarity_process = []
    for jj in lista_polarity:
        lista_polarity_process_tmp = []
        for jjj in jj:
            if (jjj.__contains__(']')):
                x = jjj.replace("]", "")
                lista_polarity_process_tmp.append(x)
            else:
                lista_polarity_process_tmp.append(jjj)
        lista_polarity_process.append(lista_polarity_process_tmp)
    return lista_polarity_process




def scrivere_sentence_file(file, file_csv):
    sentence, target_polarity = trasforma_csv_in_df_colonne_to_list(file_csv)
    with open(file, 'w') as f:
        for item in sentence:
            f.write("%s\n" % item)



def process_file(file_originale_processato):
    with open(file_originale_processato) as f:
        with open(file_prova, 'w') as f1:
            for line in f:
                f1.write(re.sub(r'([]])([a-z])', r'\1 \2', line))



def process_list_polarity_gold(lista_polarity_gold):
    l = []
    for i in lista_polarity_gold:
        l1 = []
        for j in i:
            z = re.sub(r'[+]\d', "positive", j)
            # w = re.sub(r'[-]\d', 'negative', j)
            l1.append(z)
            # prova1.append(w)
        l.append(l1)

    l2 = []
    for k in l:
        l3 = []
        for y in k:
            w = re.sub(r'[-]\d', 'negative', y)
            l3.append(w)
            # prova1.append(w)
        l2.append(l3)
    return l2


file_Originale = '../processing_fileOriginale/Nikon coolpix 4300.txt'
file_originale_caratteri_rimpiazzati = '../processing_fileOriginale/Nikon coolpix 4300-Copia.txt'
file_originale_processato = '../processing_fileOriginale/Nikon coolpix 4300.Copia2.txt'
file_originale_processato_csv = '../csv/Gold.csv'
input = 'input.txt'
file_prova = '../processing_fileOriginale/Nikon coolpix 4300.Copia2 - Copia.txt'


rimpiazza_caratteri_inutili(file_Originale)
rimozione_titoli_t(file_originale_caratteri_rimpiazzati)
process_file(file_originale_processato)
trasforma_in_csv(file_prova)
trasforma_csv_in_df_colonne_to_list(file_originale_processato_csv)
scrivere_sentence_file(input, file_originale_processato_csv)








