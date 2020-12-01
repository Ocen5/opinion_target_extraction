from stanfordcorenlp import StanfordCoreNLP
import logging
import numpy as np


def SC(local_corenlp_path, input):
  nlp = StanfordCoreNLP(local_corenlp_path, quiet=False, logging_level=logging.DEBUG)


  Tokenize = nlp.word_tokenize(input)
  POS = nlp.pos_tag(input)
  Dependency = nlp.dependency_parse(input)
  nlp.close()
  return Tokenize, POS, Dependency


def R1(local_corenlp_path, input):



  toke, pos, depe = SC(local_corenlp_path, input)


  print("Tokeninze: ", toke)
  print('\n')
  print("Part Of Speech: ", pos)
  print('\n')
  print("Dependency Parse: ", depe)
  print('\n')

  tok = np.array(toke)
  list_target = []

  Op = 'opinion-lexicon-English/positive-words.txt'
  On = 'opinion-lexicon-English/negative-words.txt'
  val = ['JJ', 'JJS', 'JJR']

  for item in pos:
    if item[1] in val:
      agg = item[0]
      with open(Op) as myfile:
        if agg in myfile.read():
          label = 'positive'
      with open(On) as myfile:
        if agg in myfile.read():
          label = 'negative'
        MR = ['amod', 'advmod', 'rcmod']
        for items in depe:
          if items[0] in MR:
            opinion = items[2]
            target = items[1]
            if pos[target-1].__contains__('NN') or pos[target-1].__contains__('NNS'):
              o = tok[opinion-1]
              t = tok[target-1]
              list_target.append(t)
                #O-->O-dep-->T

              for items in depe:
                if items[0] == 'nsubj':
                  if items[1] == target:
                    target = items[2]
                    if pos[target-1].__contains__('NN') or pos[target-1].__contains__('NNS'):
                      t = tok[target-1]
                      list_target.append(t)
                      #O-->O-dep-->H<--T-dep<--T



  return set(list_target)


def R2(local_corenlp_path, input, file_target):

  #list_target = R1(local_corenlp_path, input)

  list_opinion = []
  toke, pos, depe = SC(local_corenlp_path, input)

  print("Tokeninze: ", toke)
  print('\n')
  print("Part Of Speech: ", pos)
  print('\n')
  print("Dependency Parse: ", depe)
  print('\n')

  tok = np.array(toke)
  val = ['NN', 'NNS']
  Op = 'opinion-lexicon-English/positive-words.txt'
  On = 'opinion-lexicon-English/negative-words.txt'

  for item in pos:
    if item[1] in val:
      sost = item[0]

      with open(file_target) as myfile:
        if sost in myfile.read():
          MR = ['amod', 'advmod', 'rcmod']
          for items in depe:
            if items[0] in MR:
              opinion = items[2]
              target = items[1]
              if pos[opinion - 1].__contains__('JJ') or pos[opinion - 1].__contains__('JJS') \
                      or pos[opinion - 1].__contains__('JJR'):
                o = tok[opinion-1]
                t = tok[target-1]
                list_opinion.append(o)
                # O-->O-dep-->T

              for items in depe:
                if items[0] == 'nsubj':
                  if items[1] == target:
                    if pos[opinion-1].__contains__('JJ') or pos[opinion-1].__contains__('JJS') \
                            or pos[opinion-1].__contains__('JJR'):
                      o = tok[opinion - 1]
                      list_opinion.append(o)
                      # O-->O-dep-->H<--T-dep<--T

  return set(list_opinion)


def R3(local_corenlp_path, input, file_target):

  toke, pos, depe = SC(local_corenlp_path, input)
  list_target = []

  print("Tokeninze: ", toke)
  print('\n')
  print("Part Of Speech: ", pos)
  print('\n')
  print("Dependency Parse: ", depe)
  print('\n')

  tok = np.array(toke)
  for item in depe:
    if item[0] == 'conj':
      n = tok[item[1]-1]
      with open(file_target) as myfile:
        if n in myfile.read():
          t = item[2]
          for item in pos:
            if item[1].__contains__('NN') or item[1].__contains__('NNS') :
              target = tok[t-1]
              list_target.append(target)


  return set(list_target)

def R4(local_corenlp_path, input, file_opinion):

  toke, pos, depe = SC(local_corenlp_path, input)
  list_opinion = []

  print("Tokeninze: ", toke)
  print('\n')
  print("Part Of Speech: ", pos)
  print('\n')
  print("Dependency Parse: ", depe)
  print('\n')

  tok = np.array(toke)
  for item in depe:
    if item[0] == 'conj':
      a = tok[item[1]-1]
      with open(file_opinion) as myfile:
        if a in myfile.read():
          o = item[2]
          for item in pos:
            if item[1].__contains__('JJ') or item[1].__contains__('JJS') \
                    or item[1].__contains__('JJR'):
              opinion = tok[o-1]
              list_opinion.append(opinion)

  return set(list_opinion)

