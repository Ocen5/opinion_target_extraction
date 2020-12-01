import pandas as pd
from src import processing_fileOriginale, evaluation, propagation, processing
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import classification_report, accuracy_score


pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 2000)
pd.set_option('display.width', 2000)



local_corenlp_path = '../stanford-corenlp-4.0.0/stanford-corenlp-4.0.0'
input = 'input.txt'
target = 'target.txt'
opinion = 'opinion.txt'
lexicon_positive = '../opinion-lexicon-English/positive-words.txt'
lexicon_negative = '../opinion-lexicon-English/negative-words.txt'
csv_target = '../csv/Targ.csv'
csv_opinion = '../csv/Opi.csv'


sentences, target_polarity = processing_fileOriginale.trasforma_csv_in_df_colonne_to_list("../csv/Gold.csv")

#propagation.propagation(sentences, local_corenlp_path)
#processing.target_to_csv(target)
#processing.opinion_to_csv(opinion)




sentence, lista_target_estratti = processing.column_from_dfT(csv_target)
lista_opinion_estratti = processing.column_from_dfO(csv_opinion)
lista_polarity_estratta = processing.polarity_lista(lista_opinion_estratti, lexicon_positive, lexicon_negative)


list_target_polarity = processing_fileOriginale.process_list_target_polarity(target_polarity)
lista_target_gold = processing_fileOriginale.listaTarget_from_listaTargetPolarity(list_target_polarity)
lista_polarity_gold = processing_fileOriginale.listaPolarity_from_listaTargetPolarity(list_target_polarity)
lista_polarity_gold_mod = processing_fileOriginale.process_list_polarity_gold(lista_polarity_gold)

#rendo le due liste ==> liste di liste con dimensioni uguali
#mi creo la lista di correct target
n, lista_target_estratti_P = processing.process_lista_target(lista_target_estratti)
lista_target_gold_P = processing.process_lista_target_gold(lista_target_gold, n)
lista_target_correct, numero_corretti, numero_totale = processing.lista_correct_target(lista_target_estratti_P, lista_target_gold_P)


#mi creo la lista di correct polarity
n, lista_polarity_estratta_P = processing.process_lista_polarity(lista_polarity_estratta)
lista_polarity_gold_P = processing.process_lista_target_gold(lista_polarity_gold_mod, n)
lista_polarity_correct = processing.lista_corect_polarity(lista_polarity_estratta_P, lista_polarity_gold_P)


#valutazione target estratti
percentuale_corretti = evaluation.percentuale_targetEstratti_correct(numero_corretti, numero_totale)
print('percentuale target corretti: ', round(percentuale_corretti,2), '%')


#valutazione polarità estratte
mlb = MultiLabelBinarizer()
lista_polarity_gold_mod_tr = mlb.fit_transform(lista_polarity_gold_mod)
lista_polarity_estratta_tr = mlb.fit_transform(lista_polarity_estratta)
classes = list(mlb.classes_)


print(classification_report(lista_polarity_gold_mod_tr,lista_polarity_estratta_tr, target_names=classes))

print('accuracy:', round(accuracy_score(lista_polarity_gold_mod_tr, lista_polarity_estratta_tr),2))

evaluation.confusionMatrix(lista_polarity_gold_mod_tr.argmax(axis=1), lista_polarity_estratta_tr.argmax(axis=1), classes, name='Confusion Matrix')



#creazione df finale per visualizzare l'output
df = pd.DataFrame()
df['Sentence'] = sentences
df['Target Estratti'] = lista_target_estratti
df['Target Gold'] = lista_target_gold
df['Correct Target'] = lista_target_correct
df['Opinion Estratti'] = lista_opinion_estratti
df['Polarity Estratta'] = lista_polarity_estratta
df['Polarity Gold'] = lista_polarity_gold_mod
df['Correct Polarity'] = lista_polarity_correct

df.to_csv('../csv/Final.csv')




