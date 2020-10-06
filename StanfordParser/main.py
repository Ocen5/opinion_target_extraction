import SCnlp

local_corenlp_path = 'stanford-corenlp-4.0.0/stanford-corenlp-4.0.0'


text = open('input.txt', 'r')
lines = text.readlines()
input = ''
for i in lines:
  input = input + i

SCnlp.provaf(local_corenlp_path, input)
