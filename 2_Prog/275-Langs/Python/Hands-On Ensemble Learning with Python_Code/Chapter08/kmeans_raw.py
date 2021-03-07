import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from sklearn.datasets import load_breast_cancer
from sklearn.manifold import TSNE


np.random.seed(123456)

bc = load_breast_cancer()
data = bc.data


#plt.figure()
#plt.title('2, 4, and 6 clusters.')
for clusters in [2, 4, 6]:
    km = KMeans(n_clusters=clusters)
    preds = km.fit_predict(data)
#    plt.subplot(1,3,clusters/2)
#    plt.scatter(*zip(*data), c=preds)

    classified = {x: {'m': 0, 'b': 0} for x in range(clusters)}

    for i in range(len(data)):
        cluster = preds[i]
        label = bc.target[i]
        label = 'm' if label == 0 else 'b'
        classified[cluster][label] = classified[cluster][label]+1

    print('-'*40)
    for c in classified:
        print('Cluster %d. Malignant percentage: ' % c, end=' ')
        print(classified[c], end=' ')
        print('%.3f' % (classified[c]['m'] /
                        (classified[c]['m'] + classified[c]['b'])))

    print(metrics.homogeneity_score(bc.target, preds))
    print(metrics.silhouette_score(data, preds))
