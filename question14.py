import numpy as np


def generate_random_x(dimension):
    current_x = []

    for i in range(dimension):
        g = round(np.random.random() * 10)
        current_x.append(g)

    return current_x


def main():
    print("question 14")
    dimension = int(input("Enter the dimension of your data"))
    print("Enter mean")
    mean = np.array([float(input()) for i in range(dimension)])
    print("Enter values of variance matrix.", dimension*dimension, "values:")
    inputs = np.array([float(input()) for i in range(dimension*dimension)])
    variance = inputs.reshape(dimension, dimension)
    num_of_rand_numbers = int(input("Enter the number of random numbers you want"))
    final_result = []
    for i in range(num_of_rand_numbers):
        x = np.array(generate_random_x(dimension))
        print(x)
        x_m = x - mean
        first = (1.0 / ((np.sqrt(2*np.pi))**dimension) * np.linalg.det(variance))
        second = np.dot(np.dot(x_m.transpose(), np.linalg.inv(variance)), x_m)
        result = first * np.exp(-(second/2))
        final_result.append(result)
        print(result)
    print(final_result)


if __name__ == "__main__":
    main()
