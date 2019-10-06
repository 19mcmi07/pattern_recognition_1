import numpy as np


def main():
    print("Question 16")
    mean1, mean2, variance1, variance2 = 0, 5, 1, 1
    x1, x2 = [], []
    num = int(input("Enter number of sample"))
    for i in range(num):
        x = np.random.uniform()
        t1 = (1. / np.sqrt(2*np.pi)) * (np.exp(-((x-mean1)**2) * 0.5))
        t2 = (1. / np.sqrt(2*np.pi)) * (np.exp(-((x-mean2)**2) * 0.5))
        x1.append(t1)
        x2.append(t2)
    
    print(np.mean(x1))
    print(np.var(x1))
    print(np.mean(x2))
    print(np.var(x2))


if __name__ == "__main__":
    main()
