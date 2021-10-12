from copy import deepcopy
from matplotlib import pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import numpy as np


def get_centroids(K, data):
    # X coordinates of random centroids
    x = np.random.randint(0, np.max(data) - 20, size=K)
    # Y coordinates of random centroids
    y = np.random.randint(0, np.max(data) - 20, size=K)
    return np.array(list(zip(x, y)), dtype=np.float64)


def assign_clusters(K, centroids, distances):
    for i in range(K):
        distances[:, i] = np.linalg.norm(data - centroids[i], axis=1)
    return np.argmin(distances, axis=1)


def reposition_centroid(K, centroids, clusters):
    for i in range(K):
        # avoid dividing by error when a cluster isn't assigned any points due to poor instantiation of centroids
        if len(data[clusters == i]) == 0:
            return False
        centroids[i] = np.mean(data[clusters == i], axis=0)
    return centroids

# create k means clustering without instantiation error
def k_mean_attempt(K, data):
    # Number of training data
    num = len(data)
    # Number of clusters
    centroids = get_centroids(K, data)

    # to store old centroids
    centers_old = np.zeros(centroids.shape)  # to store old centroids
    distances = np.zeros((num, K))
    error = np.linalg.norm(centroids - centers_old)

    # When, after an update, the estimate of that center stays the same, exit loop
    while error != 0:
        # Assign data to closest centroid
        clusters = assign_clusters(K, centroids, distances)
        centers_old = deepcopy(centroids)
        # Get mean for each cluster and find new centroid
        centroids = reposition_centroid(K, centroids, clusters)
        if centroids is False:
            return False
        error = np.linalg.norm(centroids - centers_old)
    return centroids


def k_means(k, data):
    result = False
    while result is False:
        result = k_mean_attempt(k, data)
    return result


if __name__ == "__main__":
    digits = load_digits()

    # fit data to 2 dimensions
    pca = PCA(n_components=2)
    data = pca.fit_transform(digits.data)
    # get k means centroids
    result = k_means(10, data)
    plt.scatter(data[:, 0], data[:, 1])
    plt.scatter(result[:, 0], result[:, 1], s=200, c='red')
    plt.xlabel('Generated component 2')
    plt.ylabel('Generated component 1')
    plt.title("Hand written digits (K-means cluster centroids)")
    plt.show()
