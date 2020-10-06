from stanfordcorenlp import StanfordCoreNLP
import logging
import sys



def provaf(local_corenlp_path, input):
  nlp = StanfordCoreNLP(local_corenlp_path, quiet=False, logging_level=logging.DEBUG)

  sys.stdout = open("output.txt", "w")

  print('Tokenize:', nlp.word_tokenize(input))
  print('\n')
  print('Part of Speech:', nlp.pos_tag(input))
  print('\n')
  print('Named Entities:', nlp.ner(input))
  print('\n')
  print('Constituency Parsing:', nlp.parse(input))
  print('\n')
  print('Dependency Parsing:', nlp.dependency_parse(input))
  print('\n')

  nlp.close()
  sys.stdout.close()