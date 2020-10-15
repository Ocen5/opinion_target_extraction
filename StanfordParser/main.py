import SCnlp
import sys

local_corenlp_path = 'stanford-corenlp-4.0.0/stanford-corenlp-4.0.0'

with open('input.txt', 'r') as infile, \
        open('input_processato.txt', 'w') as outfile:
  data = infile.read()
  data = data.replace(".", "")
  data = data.replace(",", "")
  outfile.write(data)


text = open('input_processato.txt', 'r')
lines = text.readlines()
input = ''
for i in lines:
  input = input + i


Tokenize, POS, Dependency = SCnlp.SC(local_corenlp_path, input)

sys.stdout = open("output.txt", "w")

print("REGOLA 1")
print('\n')
target = SCnlp.R1(local_corenlp_path, input)
print("lista dei potenziali target: ", target)
print('\n')

print("REGOLA 2")
print('\n')
opinion = SCnlp.R2(local_corenlp_path, input)
print("lista delle potenziali opinion words: ", opinion)

sys.stdout.close()