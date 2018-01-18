# EXExampleMaker

Graphical UI for clustering data with EM-algorithm. Results are printed to a file spesified by the user and drawing graphs of the results is possible for 2- and 3-dimensional data.
Implementation of EM-algorithm is from scikit-learn library and drawing is done with matplotlib.

[Screenshot of UI](https://www.dropbox.com/s/34rduuljkowfmev/ui_example.png?dl=0)


## Getting Started

Run file controller.py with Python to start the software. Graphical user interface should be fairly standard. Refer to scikit-learn [documentation](http://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture) for function of each option.

### Prerequisites

* Python 3.5 or higher
* numpy
* scikit-learn

### Installing

Extract project files in a folder of your choosing. Run file controller.py with Python.

Project comes with helper file data_generation.py for generating data points from gaussian mixtures and example data set of 300 points with real class labels.


## Built With

* Python 3.5 or higher
* Graphical User interface is made with Tkinter
* EM-algorithm implementation from scikit-learn
* Numpy for handling data
* matplotlib for drawing graphs of resulting clustering.


## Authors

* **Hannes Vilmi** - *Initial work* - [hvilmi](https://github.com/hvilmi)

## License

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
