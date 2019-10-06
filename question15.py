import numpy as np
import matplotlib.pylab as plt


def generate_random_x(dimension):
    current_x = []

    for i in range(dimension):
        g = round(np.random.random() * 10)
        current_x.append(g)

    return current_x


def main():
    print("Question 15")
    dimension = 2
    mean1 = np.array([0.0, 0.0])
    mean2 = np.array([1.0, 1.0])
    prior1 = 0.5
    prior2 = 0.5
    covariance1 = np.array([[2.0, 0.4], [0.4, 1.0]])
    covariance2 = np.array([[1.0, 0.6], [0.6, 2.0]])

    result1 = []
    result2 = []
    for i in range(1000):
        points = np.array(generate_random_x(dimension))
        
        inv_of_cov1 = np.linalg.inv(covariance1)
        x_mean1 = points - mean1
        g1 = -0.5 * np.sum(np.dot(x_mean1, inv_of_cov1) * x_mean1) - dimension * 0.5 * np.log(2 * np.pi) - 0.5 * \
            np.log(np.linalg.det(covariance1)) + np.log(prior1)
        
        result1.append(g1)
        
        inv_of_cov2 = np.linalg.inv(covariance2)
        x_mean2 = points - mean2
        g2 = -0.5 * np.sum(np.dot(x_mean2, inv_of_cov2) * x_mean2) - dimension * 0.5 * np.log(2 * np.pi) - 0.5 * \
            np.log(np.linalg.det(covariance2)) + prior2
        result2.append(g2)

    plt.plot(result1)
    plt.plot(result2)
    plt.show()


if __name__ == "__main__":
    main()
