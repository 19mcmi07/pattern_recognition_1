import numpy as np
import matplotlib as plt


def classified_as(mean1, mean2, x):
    total = ((1. / np.sqrt(2 * np.pi)) * (np.exp(-((x - mean1) ** 2) * 0.5)) * 0.5) + \
            ((1. / np.sqrt(2 * np.pi)) * (np.exp(-((x - mean2) ** 2) * 0.5)) * 0.5)
    posterior1 = ((1. / np.sqrt(2 * np.pi)) * (np.exp(-((x - mean1) ** 2) * 0.5)) * 0.5) / total
    posterior2 = ((1. / np.sqrt(2 * np.pi)) * (np.exp(-((x - mean2) ** 2) * 0.5)) * 0.5) / total
    print(posterior1, posterior2)
    if posterior1 > posterior2:
        return 1
    else:
        return 2


# def calculate_posterior(mean, x):
#     total = (needs to be calculated)
#     likelihood = (1. / np.sqrt(2 * np.pi)) * (np.exp(-((x - mean) ** 2) * 0.5))
#     posterior = (likelihood * 0.5) / total
#     return posterior


def main():
    print("question 17")
    mean1, mean2 = 0, 5
    # Variances and priors need not be used as the remain constant
    # variance1, variance2 = 1, 1
    # prior1, prior2 = 0.5, 0.5
    for x in range(20):
        print(classified_as(mean1, mean2, x))


if __name__ == "__main__":
    main()
