import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from scipy.stats import mode
import k_means_function

if __name__  == "__main__":
    digits = load_digits()

    #fit data to 2 dimensions
    pca = PCA(n_components=2)
    X = pca.fit_transform(digits.data)

    # show clustered as groups of coloured points
    kmeans = KMeans(n_clusters=10, max_iter=300)
    pred_y = kmeans.fit_predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=pred_y, s=10, cmap="rainbow")
    plt.ylabel('Generated component 2')
    plt.xlabel('Generated component 1')
    plt.title("Hand written digits (K-means cluster groups)")
    plt.show()

    # show centroid of clusters
    plt.scatter(X[:, 0], X[:, 1])
    # plot centroids
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red')
    plt.xlabel('Generated component 2')
    plt.ylabel('Generated component 1')
    plt.title("Hand written digits (K-means cluster centroids)")
    plt.show()

    # Get centroids to show as images
    clusters = kmeans.fit_predict(digits.data)
    kmeans.cluster_centers_.shape
    fig, ax = plt.subplots(2, 5, figsize=(8, 3))
    centers = kmeans.cluster_centers_.reshape(10, 8, 8)
    for axi, center in zip(ax.flat, centers):
        axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
    plt.show()

    # get labels to get accuracy of k-mean clustering on data
    labels = np.zeros_like(clusters)
    for i in range(10):
        mask = (clusters == i)
        labels[mask] = mode(digits.target[mask])[0]

    from sklearn.metrics import accuracy_score
    print("Accuracy: " + str(accuracy_score(digits.target, labels)) +"%")