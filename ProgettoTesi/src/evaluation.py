from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt



def percentuale_targetEstratti_correct(n_correct, n_total):
    percent = ((n_correct/n_total)*100)
    return percent


def confusionMatrix(gold, prediction, classes_name, name):
    # Plot non-normalized confusion matrix
    matrix = metrics.confusion_matrix(gold, prediction)
    plt.figure(figsize=(6, 4))
    sns.heatmap(matrix,
                cmap='coolwarm',
                linecolor='white',
                linewidths=1,
                xticklabels=classes_name,
                yticklabels=classes_name,
                annot=True,
                fmt='d')
    plt.title(name)
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()



