import numpy as np
import matplotlib.pylab as plt


def main():
    print("Question 19")
    a = int(input("Enter 'a' value for uniform distribution"))
    b = int(input("Enter 'b' value for uniform distribution"))
    n = int(input("Enter number of random numbers needed"))
    # Run the program two times with n being 10^5 and 10^6
    s = np.random.uniform(a, b, n)
    plt.hist(s)
    print("Mean", np.mean(s))
    print("Standard deviation", np.std(s))
    plt.show()
    # We observe that the histogram becomes a straight line as the number of samples increase.


if __name__ == "__main__":
    main()
