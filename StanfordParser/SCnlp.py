from stanfordcorenlp import StanfordCoreNLP
import logging
import sys
import numpy as np



def SC(local_corenlp_path, input):
  nlp = StanfordCoreNLP(local_corenlp_path, quiet=False, logging_level=logging.DEBUG)


  Tokenize = nlp.word_tokenize(input)
  POS = nlp.pos_tag(input)
  Dependency = nlp.dependency_parse(input)
  '''
  print("Tokeninze: ", Tokenize)
  print('\n')
  print("Part Of Speech: ", POS)
  print('\n')
  print("Dependency Parse: ", Dependency)
  print('\n')
  '''
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
  val = 'JJ'

  for item in pos:
    if item[1] == val:
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
              o = tok[opinion-1]
              t = tok[target-1]
              list_target.append(t)

  return set(list_target)

def R2(local_corenlp_path, input):

  list_target = R1(local_corenlp_path, input)

  list_opinion = []
  toke, pos, depe = SC(local_corenlp_path, input)



  tok = np.array(toke)
  val = 'NN'

  for item in pos:
    if item[1] == val:
      sost = item[0]

      if sost in list_target:
        MR = ['amod', 'advmod', 'rcmod']
        for items in depe:
          if items[0] in MR:
            opinion = items[2]
            target = items[1]
            o = tok[opinion-1]
            t = tok[target-1]
            list_opinion.append(o)

  return set(list_opinion)





