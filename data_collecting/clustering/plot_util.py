import matplotlib.pyplot as plt


def show_plot(data, x_name, y_name, labels):
    plt.figure(figsize=(10, 7))
    plt.scatter(data[x_name], data[y_name], c=labels)
    plt.show()
