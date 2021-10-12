import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def elbow_method(X):
    Sum_of_squared_distances = []
    K = range(1, 12)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(X)
        Sum_of_squared_distances.append(km.inertia_)

    plt.plot(K, Sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum of squared distances')
    plt.title('Elbow Method Graph')
    plt.show()


def k_mean_plot(data, k, x_label, y_label):
    kmeans = KMeans(n_clusters=k, max_iter=300)
    pred_y = kmeans.fit_predict(data)
    plt.scatter(data[:, 0], data[:, 1], c=pred_y, cmap="rainbow", s=20)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title("Pokemon " + y_label + " vs " + x_label + " , K-means clustering")
    plt.show()


def pokemon_type_plot(data, x_label, y_label):
    colours = ['black', 'blue', 'purple', 'yellow', 'brown', 'red', 'lime', 'cyan', 'orange', 'gray', 'salmon', 'cyan',
               'olive', '#9ffeb0', '#ff6cb5', '#a50055', '#a484ac', '#feb308']
    types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground',
             'ice', 'normal', 'Poison', 'psychic', 'rock', 'steel', 'water']
    for i in range(len(types)):
        x = data[:, 0][dataset.type1 == types[i]]
        y = data[:, 1][dataset.type1 == types[i]]
        plt.scatter(x, y, c=colours[i], s=20)
    # plt.legend(digits.target_names, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title("Pokemon " + y_label + " vs " + x_label + " , Types")
    plt.show()


if __name__ == "__main__":
    dataset = pd.read_csv('pokemon.csv')
    dataset = dataset[dataset.weight_kg > 0]
    dataset = dataset[dataset.height_m > 0]
    dataset = dataset[dataset.height_m < 10]

    # speed vs attack
    X = dataset.iloc[:, [35, 19]].values  # attack vs speed
    elbow_method(X)
    k_mean_plot(X, 6, "speed", "attack")
    pokemon_type_plot(X, "speed", "attack")

    # weight vs height
    X = dataset.iloc[:, [38, 27]].values
    elbow_method(X)
    k_mean_plot(X, 4, "weight/kg", "height/m")
    pokemon_type_plot(X, "weight/kg", "height/m")

    # weight vs defence
    X = dataset.iloc[:, [38,25]].values
    elbow_method(X)
    k_mean_plot(X, 4, "weight/kg", "defence")
    pokemon_type_plot(X, "weight/kg", "defence")

    # weight vs defence
    X = dataset.iloc[:, [38, 35]].values
    elbow_method(X)
    k_mean_plot(X, 6, "weight/kg", "speed")
    pokemon_type_plot(X, "weight/kg", "speed")

    # against_grass vs defense
    X = dataset.iloc[:, [10,25]].values
    elbow_method(X)
    k_mean_plot(X, 5, "total", "defence")
    pokemon_type_plot(X, "total", "defence")
