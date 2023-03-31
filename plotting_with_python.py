from matplotlib import pyplot as plt
import numpy as np
import math as m


def main():
    input = np.array(range(1, 6))
    output1 = input**2
    output2 = input ** 3
    output3 = input**4
    output4 = []
    output5 = []
    output6 = []
    for i in input:
        output4.append(m.factorial(i))
        output5.append(m.sqrt(i))
        output6.append(m.gamma(i))
    print(input)
    print(output1)
    print(output2)
    print(output3)
    print(output4)
    print(output5)
    print(output6)
    markers = ["s", "*", ".", "+", "D", "o"]
    my_plot = plt.plot(input, output1, input, output2, input, output3, input, output4, input, output5, input, output6, marker=".", mec="k", mfc="r", ms=15)
    # markers="*", mec="k", mfc="r", ms=3
    plt.legend(["Squire", "Cube", "Quad", "Factorial", "Sqrt", "Gama"])
    plt.title("Squire, cube, quad, factorial, sqrt and gama")
    plt.xlabel("Input values")
    plt.ylabel("Output values")
    plt.grid("major", axis="both")
    min_x = np.min(input)
    min_y = np.min([output1, output2, output3, output4, output5, output6])
    max_x = np.max(input)
    max_y = np.max([output1, output2, output3, output4, output5, output6])
    plt.xlim([min_x, max_x])
    plt.ylim([min_y, max_y])
    plt.show()


if __name__ == "__main__":
    main()
