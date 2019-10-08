import numpy as np


def main():
    print("question 18")
    dimension = int(input("Enter dimensionality of the dataset"))
    num_rows = int(input("Enter number of patterns for each class"))
    training_c1 = np.array([np.random.randint(100) for i in range(num_rows * dimension)]).reshape(num_rows, dimension)
    print("input 1", training_c1)
    training_c2 = np.array([np.random.randint(100) for i in range(num_rows * dimension)]).reshape(num_rows, dimension)
    print("input 2", training_c2)
    test_data = np.array([np.random.randint(100) for i in range(num_rows * dimension)]).reshape(num_rows, dimension)
    print("test data", test_data)
    mean1 = np.mean(training_c1, axis=0)
    print("mean1", mean1)
    mean2 = np.mean(training_c2, axis=0)
    print("mean2", mean2)
    variance1 = np.cov(training_c1.T)
    print("variance 1", variance1)
    variance2 = np.cov(training_c2.T)
    print("variance 2", variance2)
    for x in test_data:
        x_m1 = x - mean1
        x_m2 = x - mean2
        likelihood1 = (1.0 / ((np.sqrt(2 * np.pi)) ** dimension) * np.linalg.det(variance1)) * \
            np.exp(-(np.dot(np.dot(x_m1.transpose(), np.linalg.inv(variance1)), x_m1)) / 2)
        likelihood2 = (1.0 / ((np.sqrt(2 * np.pi)) ** dimension) * np.linalg.det(variance2)) * \
                      np.exp(-(np.dot(np.dot(x_m2.transpose(), np.linalg.inv(variance2)), x_m2)) / 2)
        print("likelihood 1:", likelihood1)
        print("likelihood 2", likelihood2)
        if likelihood1 > likelihood2:
            print("class 1")
        elif likelihood2 > likelihood1:
            print("class 2")
        else:
            print("tie")


if __name__ == "__main__":
    main()
