import tkinter as tk
from tkinter import ttk
import tkinter.filedialog

CLUSTER_AMOUNT = 5

CLUSTERING_DONE = "Data fitted"
CLUSTERING_NOT_DONE = "Data not fitted"


class MainWindow(tk.Frame):

    def __init__(self, controller, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.controller = controller

        # Frame for data entry
        # ///////////////////////////////
        data_frame = tk.LabelFrame(self, text="Data")
        data_frame.grid(row=0, column=0, sticky=("N", "S", "E", "W"))

        tk.Button(data_frame, text="Load Data", command=self.load_data).grid(row=0, column=0)

        tk.Button(data_frame, text="Transpose data", command=self.controller.transpose_data).grid(row=0, column=1)

        self.data_shape_text = tk.StringVar()
        tk.Label(data_frame, textvariable=self.data_shape_text).grid(row=1, column=0)
        self.data_shape_text.set("No data loaded yet.")

        tk.Button(data_frame, text="Load Clustering info", command=self.load_clustering_data).grid(row=2, column=0)
        self.cluster_info_text = tk.StringVar()
        tk.Label(data_frame, textvariable=self.cluster_info_text).grid(row=2, column=1)
        self.cluster_info_text.set("No clustering info loaded.")

        tk.Label(data_frame, text="Number of Clusters").grid(row=3, column=0)
        self.cluster_num_var = tk.IntVar()
        ttk.OptionMenu(data_frame, self.cluster_num_var, 2, *[i + 2 for i in range(CLUSTER_AMOUNT - 1)]).grid(row=3,
                                                                                                              column=1)

        self.tol = tk.DoubleVar(value=0.001)
        tk.Label(data_frame, text="Convergence Threshold").grid(row=4, column=0)
        tk.Entry(data_frame, textvariable=self.tol).grid(row=4, column=1)

        # Frame for initialization options
        # ///////////////////////////////
        init_frame = tk.LabelFrame(self, text="Initialization")
        init_frame.grid(row=1, column=0, sticky=("N", "S", "E", "W"))

        self.init_var = tk.StringVar()
        self.init_var.set("kmeans")
        tk.Radiobutton(init_frame, text="k-means", variable=self.init_var, value="kmeans").grid(row=0, column=0)
        tk.Radiobutton(init_frame, text="Random", variable=self.init_var, value="random").grid(row=1, column=0)

        self.n_init_var = tk.IntVar()
        tk.Label(init_frame, text="# of initializations").grid(row=2, column=0)
        tk.Entry(init_frame, textvariable=self.n_init_var).grid(row=2, column=1)
        self.n_init_var.set(1)

        # Frame for covariance matrix options
        # ///////////////////////////////
        cov_frame = tk.LabelFrame(self, text="Covariance type")
        cov_frame.grid(row=0, column=1, sticky=("N", "S", "E", "W"))

        self.cov_var = tk.StringVar()
        self.cov_var.set("full")
        tk.Radiobutton(cov_frame, text="Full", variable=self.cov_var, value="full").grid(row=0, column=0)
        tk.Radiobutton(cov_frame, text="Tied", variable=self.cov_var, value="tied").grid(row=1, column=0)
        tk.Radiobutton(cov_frame, text="diagonal", variable=self.cov_var, value="diag").grid(row=2, column=0)
        tk.Radiobutton(cov_frame, text="spherical", variable=self.cov_var, value="spherical").grid(row=3, column=0)

        # Frame for graph settings
        # ///////////////////////////////
        graph_frame = tk.LabelFrame(self, text="Graphs")
        graph_frame.grid(row=1, column=1, sticky=("N", "S", "E", "W"))

        self.x_label = tk.StringVar()
        self.y_label = tk.StringVar()
        self.z_label = tk.StringVar()
        graph_list = [["x", self.x_label], ["y", self.y_label], ["z", self.z_label]]
        row_counter = 0
        for label, var in graph_list:
            tk.Label(graph_frame, text=label + ":").grid(row=row_counter, column=0)
            tk.Entry(graph_frame, textvariable=var).grid(row=row_counter, column=1)
            var.set(label)
            row_counter += 1

        self.graph_var = tk.IntVar()
        tk.Checkbutton(graph_frame, text="Draw Graphs", variable=self.graph_var).grid(row=3, column=0, columnspan=2)

        # Frame for output options
        # ///////////////////////////////
        output_frame = tk.LabelFrame(self, text="Output Options")
        output_frame.grid(row=2, column=0, columnspan=2, sticky=("N", "S", "E", "W"))

        tk.Button(output_frame, text="Fit Data", command=self.fit_data).grid(row=0, column=0)
        self.em_status = tk.StringVar(value="No data fitted")
        tk.Label(output_frame, textvariable=self.em_status).grid(row=0, column=1)

        tk.Button(output_frame, text="Output results to file", command=self.output_results).grid(row=1, column=0)

    def load_data(self):
        f_path = tk.filedialog.askopenfilename()
        if f_path:
            self.controller.read_data(f_path)

    def load_clustering_data(self):
        f_path = tk.filedialog.askopenfilename()
        if f_path:
            self.controller.read_clustering(f_path)

    def fit_data(self):
        options_dict = {"n_components": self.cluster_num_var.get(), "init_params": self.init_var.get(),
                        "covariance_type": self.cov_var.get(), "n_init": self.n_init_var.get(),
                        "tol": self.tol.get()}
        self.controller.fit_em(options_dict, self.graph_var.get(), [self.x_label.get(), self.y_label.get(),
                                                                    self.z_label.get()])

    def output_results(self):
        f_path = tk.filedialog.askopenfilename()
        if f_path:
            self.controller.print_to_file(f_path)

    def write_em_result(self, text):
        self.em_status.set(text)

    def write_clustering_loaded(self, n, loaded=True):
        if loaded:
            self.cluster_info_text.set("Loaded class info of " + str(n) + " data points.")
        else:
            self.cluster_info_text.set("No clustering info loaded.")

    def set_data_dimensions(self, n, d):
        self.data_shape_text.set("Loaded " + str(n) + " " + str(d) + "-dimensional data points.")
