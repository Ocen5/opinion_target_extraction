import Rule
import nltk
from nltk.tokenize import sent_tokenize



def propagation(input, local_corenlp_path):

    with open(input, 'r') as infile, \
            open('input_processato.txt', 'w') as outfile:
      data = infile.read()
      data = data.replace(",", "")
      outfile.write(data)

    nltk.download('punkt')
    text = open("input_processato.txt").read()
    sentences = sent_tokenize(text)


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



        target = 'target.txt'
        print("REGOLA 2")
        print('\n')
        opin = Rule.R2(local_corenlp_path, input, target)
        for element in opin:
            opinion.write(' ')
            opinion.write(element)



        target = open('target.txt', 'a')
        targe = 'target.txt'
        print("REGOLA 3")
        print('\n')
        targ = Rule.R3(local_corenlp_path, input, targe)
        for element in targ:
            target.write(' ')
            target.write(element)


        opinion = open('opinion.txt', 'a')
        opin = 'opinion.txt'
        print("REGOLA 4")
        print('\n')
        op = Rule.R4(local_corenlp_path, input, opin)
        for element in op:
            target.write(' ')
            opinion.write(element)



        target.close()
        opinion.close()

