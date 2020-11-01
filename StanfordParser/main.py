import Rule
import Prop
import Processing
import sys
from nltk.tokenize import sent_tokenize
import nltk
import csv
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 2000)
pd.set_option('display.width', 2000)

local_corenlp_path = 'stanford-corenlp-4.0.0/stanford-corenlp-4.0.0'
input = 'input.txt'
target = 'target.txt'
opinion = 'opinion.txt'

#Prop.propagation(input, local_corenlp_path)
Processing.target_to_csv(target)
Processing.opinion_to_csv(opinion)


dfT = pd.read_csv('Targ.csv')
sentence = dfT['Sentence'].tolist()
target = dfT['Target'].tolist()

dfO = pd.read_csv('Opi.csv')
opinion = dfO['Opinion'].tolist()
#print(opinion)
new_opinion=['missing' if x is np.nan else x for x in opinion]


#trasformo opinion in una lista di liste da [' compact best digital available', ' nasty'] a
# [['compact', 'best', 'digital', 'available'], ['nasty']]
op = []
for str in new_opinion:
    x = str.split()
    print(x)
    op.append(x)
#print(op)


polarity = []
for i in op:
    pol = []
    for j in i:
        with open('opinion-lexicon-English/positive-words.txt') as f:
            with open('opinion-lexicon-English/negative-words.txt') as f1:
                if j in f.read():
                    pol.append('positive')
                elif j in f1.read():
                    pol.append('negative')
                else:
                    pol.append('-missing-')
    polarity.append(pol)



df = pd.DataFrame()
df['Sentence'] = sentence
df['Target'] = target
df['Opinion'] = opinion
df['Polarity'] = polarity
print(df)

df.to_csv('C:/Users/Marco/PycharmProjects/StanfordParser/Final.csv')











'''
with open('input.txt', 'r') as infile, \
        open('input_processato.txt', 'w') as outfile:
  data = infile.read()
  data = data.replace(",", "")
  outfile.write(data)

nltk.download('punkt')
text = open("input_processato.txt").read()
sentences = sent_tokenize(text)


#sys.stdout = open("output.txt", "w")

for input in sentences:

    target = open('target.txt', 'a')
    opinion = open('opinion.txt', 'a')
    target.write('\n')
    target.write(input)
    opinion.write('\n')
    opinion.write(input)


    print("REGOLA 1")
    print('\n')
    targ = Rule.R1(local_corenlp_path, input)
    for element in targ:
        target.write(' ')
        target.write(element)

    #target.close()


    target = 'target.txt'
    #for input in sentences:
    print("REGOLA 2")
    print('\n')
    opin = Rule.R2(local_corenlp_path, input, target)
    for element in opin:
        opinion.write(' ')
        opinion.write(element)

    #opinion.close()

    #sys.stdout.close()

    target = open('target.txt', 'a')
    targe = 'target.txt'
        #for input in sentences:
    print("REGOLA 3")
    print('\n')
    targ = Rule.R3(local_corenlp_path, input, targe)
    for element in targ:
        target.write(' ')
        target.write(element)

        #target.close()

    opinion = open('opinion.txt', 'a')
    opin = 'opinion.txt'
        #for input in sentences:
    print("REGOLA 4")
    print('\n')
    op = Rule.R4(local_corenlp_path, input, opin)
    for element in op:
        target.write(' ')
        opinion.write(element)



     #opinion.close()
    target.close()
    opinion.close()

'''


'''

with open('target.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(".") for line in stripped if line)
    with open('Targ.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Sentence', 'Target'))
        writer.writerows(lines)

'''


'''
with open('opinion.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(".") for line in stripped if line)
    with open('Opi.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Sentence', 'Opinion'))
        writer.writerows(lines)
'''




#dfT['Opinion'] = opinion
#print(dfT)




#dfT.to_csv('C:/Users/Marco/PycharmProjects/StanfordParser/prova.csv')

