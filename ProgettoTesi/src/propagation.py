from src import rule
import nltk
from nltk.tokenize import sent_tokenize



#nel caso di un testo, viene suddiviso lo stesso in una lista di frasi
'''
def sentence_tokenize(input):
    nltk.download('punkt')
    text = open("../input.txt").read()
    sentences = sent_tokenize(text)
    return sentences
'''
def propagation(sentences, local_corenlp_path):

    #sentences = sentence_tokenize(input)

    for input in sentences:


        target = open('../target.txt', 'a')
        opinion = open('../opinion.txt', 'a')


        target.write('\n')
        target.write(input +'#')
        opinion.write('\n')
        opinion.write(input + '#')


        print("REGOLA 1")
        print('\n')
        targ = rule.R1(local_corenlp_path, input)
        for element in targ:
            target.write(' ')
            target.write(element)
            target.write(' ')




        target = '../lessico_target_opinion/Lessico-Target.txt'
        print("REGOLA 2")
        print('\n')
        opin = rule.R2(local_corenlp_path, input, target)
        for element in opin:
            opinion.write(' ')
            opinion.write(element)
            opinion.write(' ')




        target = open('../target.txt', 'a')
        targe = '../lessico_target_opinion/Lessico-Target.txt'
        print("REGOLA 3")
        print('\n')
        targ = rule.R3(local_corenlp_path, input, targe)
        for element in targ:
            target.write(' ')
            target.write(element)
            target.write(' ')



        opinion = open('../opinion.txt', 'a')
        opin = '../lessico_target_opinion/Lessico-Opinion.txt'
        print("REGOLA 4")
        print('\n')
        op = rule.R4(local_corenlp_path, input, opin)
        for element in op:
            target.write(' ')
            opinion.write(element)
            opinion.write(' ')




        target.close()
        opinion.close()

