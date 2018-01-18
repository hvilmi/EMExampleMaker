import em_gui
import tkinter as tk
import sklearn.mixture.gaussian_mixture
import sklearn.metrics
import numpy as np
import helper_func
import matplotlib.pyplot as plt


class EMController:
    def __init__(self):
        self.data = None
        self.class_info = None
        self.class_predict = None
        self.em = None
        self.output_file = None

        root = tk.Tk()
        self.gui = em_gui.MainWindow(self, root)
        self.gui.pack()
        root.mainloop()

    def fit_em(self, em_options, draw, labels):
        """

        :param em_options: dictionary containing options for EM clustering
        :param draw: Boolean value. Determines if graphs are drawn. Only for 2 and 3 dimensional data points.
        :param labels: Custom labels for graph axes.
        :return:
        """
        self.em = sklearn.mixture.gaussian_mixture.GaussianMixture(**em_options)
        self.em.fit(self.data)
        if self.class_info is not None:
            self.class_predict = helper_func.fix_pred_labels(self.em.predict(self.data), self.class_info)
        else:
            self.class_predict = self.em.predict(self.data)

        if draw:
            if self.data.shape[1] == 2:
                if self.class_info is not None:
                    helper_func.draw_clusters(self.data, self.class_info, labels[0], labels[1])
                helper_func.draw_clusters(self.data, self.class_predict, labels[0], labels[1])

            if self.data.shape[1] == 3:
                if self.class_info is not None:
                    helper_func.draw_clusters_3d(self.data, self.class_info, labels[0], labels[1], labels[2])
                helper_func.draw_clusters_3d(self.data, self.class_predict, labels[0], labels[1], labels[2])

            plt.show()
        self.gui.write_em_result(em_gui.CLUSTERING_DONE)

    def print_to_file(self, file_path):
        """
        This method prints result of clustering to the given file.
        """

        with open(file_path, 'w') as f:
            f.write("Results after " + str(self.em.n_iter_) + " iterations:\n")

            cluster_num = 0
            for mean, covariance, weight in zip(self.em.means_, self.em.covariances_, self.em.weights_):
                f.write("Cluster " + str(cluster_num))
                f.write("\nMean:\n")
                f.write(str(mean))
                f.write("\nCovariance:\n")
                f.write(str(covariance))
                f.write("\nWeight\n")
                f.write(str(weight))
                f.write("\n#########################\n")

                cluster_num = cluster_num + 1

            if self.class_info is not None:
                f.write(str(sklearn.metrics.confusion_matrix(self.class_info, self.class_predict))
                        + "\n#########################\n")

            f.write("Clustering for data:\n")
            for cluster in self.class_predict:
                f.write(str(cluster))
                f.write("\n")

    def set_output(self, file_path):
        self.output_file = file_path

    def read_data(self, file_path):
        data = []
        with open(file_path, 'r') as f:
            for line in f:
                data.append([float(value) for value in line.split(" ")])

        data = np.asarray(data)
        self.gui.set_data_dimensions(*data.shape)
        self.data = data
        self.gui.write_em_result(em_gui.CLUSTERING_NOT_DONE)

    def read_clustering(self, file_path):
        class_info = []
        with open(file_path, 'r') as f:
            for line in f:
                class_info.append(int(line))
        self.class_info = class_info
        self.gui.write_clustering_loaded(len(self.class_info))

    def transpose_data(self):
        if self.data is not None:
            self.data = self.data.T
            self.gui.set_data_dimensions(*self.data.shape)


if __name__ == '__main__':
    controller = EMController()
