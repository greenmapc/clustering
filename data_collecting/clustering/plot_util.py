import matplotlib.pyplot as plt


def show_plot(data, x_name, y_name, labels):
    plt.figure(figsize=(10, 7))

    if y_name == 'year':
        plt.axis([0, data[x_name].max() * 1.1,
                  1950, data[y_name].max() + 10])
    elif x_name == 'year':
        plt.axis([1950, data[x_name].max() + 10,
                  0, data[y_name].max() * 1.1])
    else:
        plt.axis([0, data[x_name].max() * 1.1,
                  0, data[y_name].max() * 1.1])

    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.scatter(data[x_name], data[y_name], c=labels)
    plt.show()
