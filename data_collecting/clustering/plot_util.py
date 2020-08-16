import matplotlib.pyplot as plt


def show_plot(data, x_name, y_name, labels):
    plt.figure(figsize=(10, 7))
    plt.axis([0, data[x_name].max() * 1.1,
              0, data[y_name].max() * 1.1])
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.scatter(data[x_name], data[y_name], c=labels)
    plt.show()
