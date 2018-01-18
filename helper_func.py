import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

CLASS_MARKERS = ['x', 'o', '+', 'D', '^']


def fix_pred_labels(prediction, class_info):
    """
    Tries to fix prediction labels to conform to original class labels of data when original class labels are available.
    """

    if max(prediction) != max(class_info) or len(prediction) != len(class_info):
        return prediction

    mapping_list = []
    for i in range(max(prediction)+1):
        mapping_list.append([])
        mapping_list[i] = [0 for j in range(max(prediction)+1)]

    for true, pred in zip(prediction, class_info):
        mapping_list[true][pred] += 1

    class_mapping = {}
    for i in range(max(prediction)+1):
        class_mapping[str(i)] = mapping_list[i].index(max(mapping_list[i]))

    if len(set(class_mapping.values())) == max(prediction)+1:
        fixed_pred = [class_mapping[str(i)] for i in prediction]
        return fixed_pred
    else:
        # Fixing prediction labels wasn't successful. Return original prediction labels.
        print(class_mapping, 'Luokkamerkintöjen korjaus ei onnistunut')
        return prediction


def draw_clusters(data, class_info, xlabel, ylabel, class_markers=None):
    """
    Function for drawing 2 dimensional graphs of data points and their clusters.
    """
    if class_markers is None:
        class_markers = CLASS_MARKERS

    classified_data = []
    for i in range(max(class_info) + 1):
        classified_data.append([])

    for point, cluster in zip(data, class_info):
        classified_data[cluster].append(point)

    plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for cluster, mark in zip(classified_data, class_markers):
        x_axis, y_axis = np.asarray(cluster).T
        plt.scatter(x=x_axis, y=y_axis, c='black', marker=mark)


def draw_clusters_3d(data, class_info, xlabel, ylabel, zlabel, class_markers=None):
    """
    Function for drawing 3 dimensional graphs of data points and their clusters.
    """
    if class_markers is None:
        class_markers = CLASS_MARKERS

    classified_data = []
    for i in range(max(class_info) + 1):
        classified_data.append([])

    for point, cluster in zip(data, class_info):
        classified_data[cluster].append(point)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    for cluster, mark in zip(classified_data, class_markers):
        ax.scatter(np.asarray(cluster)[:, 0], np.asarray(cluster)[:, 1], zs=np.asarray(cluster)[:, 2], c='black',
                   marker=mark)
