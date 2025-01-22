import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from c_sample_issues import read_issues


def draw_boxplot(numbers_list):
    color = {
        "boxes": "DarkGreen",
        "whiskers": "DarkOrange",
        "medians": "Red",
        "caps": "Gray",
    }

    # Set the figure size.
    plt.rcParams["figure.figsize"] = [10, 7]
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["boxplot.meanline"] = True
    plt.rcParams["boxplot.showmeans"] = True

    # Pandas dataframe.
    # n_query_data = pd.DataFrame({f"{file_name}": n_query_list})
    df = pd.DataFrame({'# of Comments': numbers_list})

    # Plot the dataframe.
    df[['# of Comments']].plot(kind='box', color=color, legend=True)

    # Display the plot.
    plt.show()

    # Calculate Q1, Q3 and IQR
    q1 = df['# of Comments'].quantile(0.25)
    q3 = df['# of Comments'].quantile(0.75)
    iqr = q3 - q1

    # Determine the outliers
    outliers = df[((df['# of Comments'] < (q1 - 1.5 * iqr)) | (df['# of Comments'] > (q3 + 1.5 * iqr)))][
        '# of Comments']

    print(f'Q1: {q1}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    # Print the number of outliers
    print(f'Total number of outliers: {len(outliers)}')


def no_outliers(data):
    # Calculate interquartile range.
    q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
    iqr = q75 - q25

    # Calculate the outlier cutoff.
    cut_off = iqr * 1.5
    lower, upper = q25 - cut_off, q75 + cut_off
    print(f'Lower: {lower}')
    print(f'Upper: {upper}')

    # True if x is NOT an outlier, false otherwise.
    return list(map(lambda x: x < upper, data))


def draw_histogram(numbers_list, x_label):
    """# Creating histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(n_comment_list, bins = [0, 20, 40, 60, 80, 100])"""

    n_bins = 40
    # Creating histogram
    fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)
    axs.hist(numbers_list, bins=n_bins)

    # Setting labels for x and y axes
    plt.xlabel(x_label)
    plt.ylabel('Frequency')

    # Show plot
    plt.show()


def draw_multiple_boxplot(data, labels):
    """
    Draw a boxplot for each set of data in the list.
    :param data: List of lists containing the data to be plotted
    :param labels: List of labels for the data
    :return: None
    """
    # Calculate and print the median and mean for each set of data
    for i, label in enumerate(labels):
        print(f"For {label}:")
        print(f"  Max: {np.max(data[i])}")
        print(f"  Min: {np.min(data[i])}")
        print(f"  Median: {np.median(data[i])}")
        print(f"  Mean: {np.mean(data[i])}")

    # Create a new figure with specified size
    plt.figure(figsize=(10, 3))

    # Determine new positions for the boxplots to reduce the gap between them
    new_positions = np.arange(1, len(data) + 1) * 0.2

    # Create the boxplot with the new positions
    bplot = plt.boxplot(data, vert=False,
                        medianprops={'color':'red'},
                        meanprops={'marker':'o', 'markerfacecolor':'green'},
                        showmeans=True,
                        positions=new_positions)

    # Set the limits of the y-axis to reduce empty space at the top and bottom
    plt.ylim(new_positions[0] - 0.15, new_positions[-1] + 0.15)

    plt.yticks(new_positions, labels)
    # Set the range of the x-axis to [0, 80]
    plt.xlim(0, 300)
    # plt.xlabel("Sequence Length")
    # plt.title('Boxplots of Sequence Lengths')
    plt.grid(axis='x', linestyle='--')
    plt.show()


def draw_violin_plot(number_list, x_label):
    # Create a violin plot
    sns.violinplot(x=number_list)

    # Customizing the plot
    plt.title('Violin Plot')
    plt.xlabel(x_label)

    # Show the plot
    plt.show()


if __name__ == '__main__':
    # Draw boxplots for the data
    # Time to resolve in days for 356 coded issues
    resolution_time_all = [0, 53, 59, 26, 3, 6, 26, 188, 5, 41, 32, 275, 16, 1, 5, 4, 2, 704, 36, 10, 1, 24, 265, 816, 26, 30, 3, 336, 268, 13, 15, 3, 587, 24, 5, 5, 19, 79, 5, 2, 38, 31, 61, 5, 10, 11, 3, 2, 2, 63, 95, 3, 2, 13, 11, 17, 208, 1, 106, 52, 4, 17, 1, 126, 2, 1, 14, 263, 4, 4, 125, 1, 13, 86, 2, 1, 2, 2394, 11, 39, 17, 1, 2, 18, 1559, 196, 8, 3, 8, 1, 119, 516, 205, 11, 1, 4, 72, 10, 2, 21, 4, 32, 1651, 1, 1233, 16, 62, 5, 6, 13, 1, 2, 4, 1, 12, 4, 0, 5, 230, 14, 21, 5, 0, 82, 0, 15, 2, 12, 722, 3, 1, 166, 1, 7, 26, 4, 21, 20, 1, 3, 13, 11, 3, 363, 573, 1, 3, 4, 3, 2, 2, 5, 9, 3, 5, 27, 3, 20, 292, 4, 1287, 2, 43, 5, 6, 2, 139, 1, 12, 1, 3, 101, 3, 83, 5, 15, 94, 2, 7, 131, 1, 1, 2, 42, 6, 77, 4, 2, 3, 12, 142, 5, 9, 12, 1, 1, 1, 8, 70, 214, 7, 59, 1, 44, 20, 7, 2, 4, 27, 12, 1, 5, 9, 2, 1, 208, 0, 1, 2, 0, 2, 1952, 4, 7, 5, 0, 104, 46, 6, 221, 2, 3, 9, 6, 48, 1, 0, 1, 4, 1, 9, 107, 2, 9, 1, 89, 1, 559, 1, 20, 3, 10, 141, 337, 353, 35, 7, 1, 1, 1, 1, 9, 1, 1, 61, 22, 370, 6, 7, 15, 61, 328, 35, 226, 20, 9, 1, 1, 1, 0, 1, 2, 11, 19, 15, 28, 26, 31, 3, 101, 1, 12, 2, 13, 316, 5, 21, 15, 1, 30, 14, 8, 135, 190, 643, 1, 20, 8, 11, 4, 2, 0, 5, 2, 5, 11, 4, 11, 85, 86, 13, 2, 46, 147, 4, 1, 1, 3, 14, 1, 24, 4, 28, 3, 4, 3, 2, 3, 0, 16, 28, 95, 1, 0, 6, 0, 33, 18, 3, 4, 3, 14, 1, 8, 3, 4]
    resolution_time_defects = [0, 53, 59, 26, 3, 6, 26, 188, 5, 41, 32, 275, 16, 1, 5, 4, 2, 36, 10, 1, 24, 265, 816, 26, 30, 3, 336, 268, 13, 15, 3, 587, 24, 5, 5, 19, 79, 5, 2, 38, 61, 5, 10, 11, 3, 2, 2, 63, 95, 3, 2, 11, 17, 208, 1, 106, 52, 4, 17, 126, 2, 1, 14, 263, 4, 4, 125, 1, 13, 86, 2, 1, 2, 2394, 11, 39, 17, 1, 2, 18, 1559, 196, 8, 3, 8, 1, 119, 516, 205, 11, 1, 4, 72, 10, 2, 21, 4, 32, 1651, 1, 1233, 16, 62, 5, 6, 13, 1, 2, 4, 1, 12, 4, 0, 5, 230, 14, 21, 5, 0, 82, 0, 15, 2, 12, 722, 3, 1, 166, 1, 26, 4, 21, 20, 1, 3, 13, 11, 3, 363, 573, 1, 3, 4, 3, 2, 2, 5, 9, 3, 5, 27, 3, 20, 292, 4, 1287, 2, 43, 5, 6, 2, 139, 1, 12, 1, 3, 101, 3, 83, 5, 15, 94, 2, 7, 131, 1, 1, 2, 42, 6, 77, 4, 2, 3, 12, 142, 5, 9, 12, 1, 1, 8, 7, 7, 12, 5, 9, 2, 1, 208, 0, 1, 2, 1952, 4, 5, 104, 46, 6, 3, 9, 6, 48, 1, 0, 1, 2, 1, 89, 10, 337, 35, 1, 1, 22, 6, 15, 328, 226, 1, 0, 1, 2, 11, 19, 15, 28, 31, 1, 135, 190, 20, 11, 4, 0, 5, 11, 85, 13, 2, 1, 1, 14, 1, 4, 3, 0, 28, 95, 1, 6, 0, 33, 18, 4, 3, 1, 8, 3, 4]
    resolution_time_enhancements = [704, 31, 13, 7, 1, 70, 214, 59, 1, 44, 20, 2, 4, 27, 1, 2, 0, 7, 0, 221, 2, 4, 9, 107, 9, 1, 559, 1, 20, 3, 141, 353, 7, 1, 1, 9, 1, 1, 61, 370, 61, 35, 20, 1, 101, 12, 13, 316, 5, 15, 30, 14, 643, 8, 11, 86, 147, 3, 3, 3]
    resolution_time_tasks = [1, 1, 7, 9, 1, 26, 3, 1, 2, 21, 8, 1, 2, 2, 5, 4, 46, 4, 24, 28, 4, 2, 16, 0, 3, 14]

    time_to_resolve_simple = [0, 53, 5, 41, 32, 275, 1, 5, 4, 2, 10, 1, 24, 30, 3, 15, 3, 587, 5, 5, 79, 5, 2, 38, 31, 5, 10, 11, 3, 2, 2, 63, 3, 13, 11, 17, 1, 106, 4, 1, 126, 2, 1, 14, 263, 4, 1, 13, 86, 2, 1, 2, 11, 39, 1, 2, 18, 1559, 196, 8, 3, 516, 205, 4, 72, 10, 2, 21, 1, 1233, 6, 1, 2, 4, 1, 4, 0, 5, 230, 21, 0, 0, 15, 2, 12, 722, 3, 1, 4, 1, 3, 13, 11, 3, 363, 573, 1, 4, 2, 2, 5, 3, 5, 3, 4, 2, 43, 5, 6, 2, 1, 12, 1, 5, 15, 94, 2, 7, 1, 1, 2, 42, 6, 4, 2, 3, 12, 142, 5, 9, 12, 1, 1, 8, 70, 214, 7, 1, 44, 7, 2, 4, 27, 12, 1, 5, 2, 1, 208, 0, 1, 2, 0, 2, 1952, 4, 7, 5, 0, 104, 46, 6, 221, 6, 48, 0, 1, 4, 1, 9, 107, 2, 9, 1, 89, 1, 559, 1, 20, 7, 1, 1, 1, 1, 1, 61, 7, 328, 226, 20, 1, 1, 1, 0, 1, 2, 19, 15, 31, 3, 101, 1, 12, 2, 21, 1, 30, 14, 8, 135, 190, 643, 20, 11, 4, 2, 0, 5, 2, 11, 4, 11, 85, 13, 2, 46, 147, 4, 1, 1, 3, 14, 1, 24, 4, 28, 3, 4, 3, 3, 0, 16, 28, 1, 0, 6, 0, 3, 3, 1, 8, 3]
    time_to_resolve_complex = [59, 26, 3, 6, 26, 188, 16, 704, 36, 265, 816, 26, 336, 268, 13, 24, 19, 61, 95, 2, 208, 52, 17, 4, 125, 2394, 17, 8, 1, 119, 11, 1, 4, 32, 1651, 16, 62, 5, 13, 12, 14, 5, 82, 1, 166, 7, 26, 21, 20, 3, 3, 9, 27, 20, 292, 1287, 139, 3, 101, 3, 83, 131, 77, 1, 59, 20, 9, 2, 3, 9, 1, 3, 10, 141, 337, 353, 35, 9, 1, 22, 370, 6, 15, 61, 35, 9, 11, 28, 26, 13, 316, 5, 15, 1, 8, 5, 86, 2, 95, 33, 18, 4, 14, 4]

    # data = [time_to_resolve, time_to_resolve_simple, time_to_resolve_complex]
    # labels = ['All', 'Simple', 'Complex']
    # draw_multiple_boxplot(data, labels)

    data = [resolution_time_all, resolution_time_defects, resolution_time_enhancements, resolution_time_tasks]
    labels = ['All', 'Defect', 'Enhancement', 'Task']
    draw_multiple_boxplot(data, labels)
    # draw_boxplot(resolution_time_all)
    # draw_boxplot(resolution_time_defects)
    # draw_boxplot(resolution_time_enhancements)
    # draw_boxplot(resolution_time_tasks)

    """data = [time_to_resolve]
    labels = ['Sampled Issues']
    # draw_boxplot(time_to_resolve)
    draw_multiple_boxplot(data, labels)"""

    # Pattern length of different types of issues
    pattern_length_defects = [3, 6, 14, 6, 8, 8, 12, 9, 2, 4, 2, 1, 15, 1, 5, 5, 1, 6, 2, 2, 6, 11, 6, 6, 3, 2, 15, 8, 4, 3, 2, 4, 10, 2, 3, 16, 6, 2, 1, 4, 5, 1, 3, 5, 4, 1, 3, 4, 20, 1, 11, 2, 3, 9, 3, 5, 40, 6, 12, 4, 3, 1, 2, 2, 2, 7, 16, 2, 3, 8, 2, 2, 2, 5, 5, 3, 5, 2, 2, 1, 1, 3, 1, 1, 9, 9, 11, 1, 5, 7, 4, 6, 3, 1, 2, 2, 5, 29, 20, 3, 5, 8, 24, 7, 3, 9, 4, 2, 1, 2, 10, 3, 4, 4, 3, 12, 5, 12, 4, 11, 1, 2, 1, 1, 0, 4, 8, 16, 4, 7, 1, 16, 10, 3, 4, 4, 1, 5, 2, 3, 2, 4, 1, 6, 3, 4, 3, 18, 5, 2, 4, 3, 12, 7, 6, 11, 2, 1, 1, 5, 2, 6, 2, 6, 2, 7, 10, 10, 12, 3, 1, 1, 2, 2, 11, 3, 3, 1, 3, 2, 6, 2, 4, 2, 2, 0, 4, 1, 6, 6, 6, 3, 5, 5, 5, 5, 7, 3, 2, 3, 4, 2, 3, 4, 4, 6, 2, 1, 4, 12, 10, 3, 6, 5, 2, 2, 3, 3, 1, 8, 9, 14, 6, 4, 19, 11, 13, 3, 3, 3, 3, 3, 3, 8, 5, 4, 13, 2, 3, 5, 2, 1, 5, 5, 2, 3, 2, 3, 2, 4, 0, 3, 2, 2, 4, 2, 3, 4, 12, 3, 4, 3, 8, 8, 6, 4, 2, 3, 4, 7]
    pattern_length_enhancements = [9, 3, 3, 6, 3, 3, 0, 11, 2, 7, 8, 2, 5, 2, 2, 3, 1, 2, 3, 4, 4, 2, 6, 4, 3, 4, 2, 5, 3, 9, 9, 13, 2, 3, 4, 7, 9, 2, 8, 6, 15, 6, 5, 3, 2, 4, 11, 12, 4, 12, 6, 4, 5, 6, 3, 4, 2, 2, 3, 6]
    pattern_length_tasks = [2, 2, 3, 8, 5, 11, 2, 3, 2, 3, 2, 6, 2, 2, 7, 2, 2, 2, 2, 4, 2, 5, 2, 4, 2, 6]

    data = [pattern_length_defects, pattern_length_enhancements, pattern_length_tasks]
    labels = ['Defects', 'Enhancements', 'Tasks']
    # draw_boxplot(pattern_length_defects)
    # draw_multiple_boxplot(data, labels)

    # frequency_of_patterns = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 10, 12, 12, 13, 14, 17, 21, 22, 40, 49]
    # draw_boxplot(frequency_of_patterns)

    avg_patten_length = [6.67, 13.50, 10.00, 6.00, 14.67, 7.00, 18.00, 17.25, 9.00, 7.00, 12.58, 8.00, 1.00, 5.00, 6.50, 5.00, 2.33, 7.00, 4.25, 3.57, 2.75, 5.00, 7.00, 3.33, 2.57, 1.00, 10.00, 7.00, 6.00, 13.00, 2.17, 2.00, 3.62, 5.00, 5.00, 3.29, 12.50, 3.67, 7.50, 4.45, 5.50, 1.00, 11.00, 7.00, 3.00, 10.50, 9.00, 6.00, 2.60, 7.00, 3.50, 10.00, 0.00, 1.00, 9.25, 2.00, 2.00, 3.90, 5.33, 3.38, 9.00, 1.00]
    # draw_boxplot(avg_patten_length)
    median_pattern_length = [6, 13.5, 10, 6, 13, 7, 18, 14, 9, 7, 10.5, 8, 1, 5, 6.5, 5, 2, 7, 4, 3, 2.5, 5, 7, 3, 2, 1, 11, 7, 6, 13, 2, 2, 3, 5, 5, 3, 12.5, 4, 6.5, 4, 5.5, 1, 11, 7, 3, 10, 9, 6, 3, 7, 3.5, 10, 0, 1, 7, 2, 2, 4, 5, 3, 9, 1]
    # draw_boxplot(median_pattern_length)
    # data = [avg_patten_length, median_pattern_length]
    # labels = ['Average', 'Median']
    # draw_multiple_boxplot(data, labels)

    # draw_histogram(avg_patten_length, 'Average')
    # draw_histogram(median_pattern_length, 'Median')

    # draw_violin_plot(avg_patten_length, 'Average')
    # draw_violin_plot(median_pattern_length, 'Median')
