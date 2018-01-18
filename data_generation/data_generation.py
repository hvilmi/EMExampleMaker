import numpy as np


def main():
    means = [[1, 1], [3.5, 3.5], [5, 1]]
    covariances = [
        [[1, -0.3],
         [-0.3, 1]],
        [[1, 0.3],
         [0.3, 1]],
        [[1, -0.6],
         [-0.6, 1]]
    ]

    data = []
    for mean, covariance in zip(means, covariances):
        for data_point in np.random.multivariate_normal(mean, covariance, 100):
            data.append(data_point)

    with open('gaussian_data.txt', 'w') as f:
        for data_point in data:
            f.write(str(data_point[0]) + " " + str(data_point[1]) + "\n")

    with open('gaussian_class_info.txt', 'w') as f:
        for i in range(3):
            for j in range(100):
                f.write(str(i) + '\n')


if __name__ == '__main__':
    main()
