import csv



def target_to_csv(target):
    with open(target, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(".") for line in stripped if line)
        with open('Targ.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Sentence', 'Target'))
            writer.writerows(lines)

def opinion_to_csv(opinion):
    with open(opinion, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(".") for line in stripped if line)
        with open('Opi.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Sentence', 'Opinion'))
            writer.writerows(lines)
