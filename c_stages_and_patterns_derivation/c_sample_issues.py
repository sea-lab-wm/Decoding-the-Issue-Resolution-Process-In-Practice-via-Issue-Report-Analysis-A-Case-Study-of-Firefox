import json
import random
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


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


def draw_histogram(numbers_list):
    """# Creating histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(n_comment_list, bins = [0, 20, 40, 60, 80, 100])"""

    n_bins = 40
    # Creating histogram
    fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)
    axs.hist(numbers_list, bins=n_bins)

    # Setting labels for x and y axes
    plt.xlabel('# of Comments')
    plt.ylabel('Frequency')

    # Show plot
    plt.show()


def read_issues(file_path):
    with open(file_path) as f:
        issues = json.load(f)
    return issues


def count_issues(issue_list):
    return len(issue_list)


def get_issue_id_list(issue_list):
    issue_id_list = []

    for issue_dict in issue_list:
        issue_id = issue_dict['id']
        issue_id_list.append(issue_id)

    return issue_id_list


def get_n_comment_list(issue_list):
    n_comment_list = []

    for issue_dict in issue_list:
        n_comment = len(issue_dict['comments'])
        n_comment_list.append(n_comment)

    print(f'Total # of issues that have comments: {len(n_comment_list)}')
    print(f'Maximum # of comments: {np.max(n_comment_list)}')
    print(f'Minimum # of comments: {np.min(n_comment_list)}')
    print(f'Avg. # of comments: {np.mean(n_comment_list)}')
    print(f'Median of # of comments: {np.median(n_comment_list)}')

    return n_comment_list


def generate_a_random_number():
    # Generate a random integer between 1 and 10000
    random_number = random.randint(1, 10000)
    print(random_number)


def percentile_based_sampling(num_list):
    # Set a seed for reproducibility
    np.random.seed(4332)
    random.seed(4332)

    # num_list = list(np.random.randint(1, 1001, size=1000))  # a list of 1000 random integers from 1 to 1000

    # Generate percentiles at 10, 20, ..., 90, 100
    percentiles = [np.percentile(num_list, p) for p in range(10, 101, 10)]
    print(f"Percentiles: {percentiles}")

    # Now create 10 lists, each one with the numbers in num_list within each percentile range
    num_list_sorted = sorted(num_list)
    divisions = []
    start = 0

    for percentile in percentiles:
        division = [x for x in num_list_sorted if start <= x < percentile]
        divisions.append(division)
        start = percentile

    # Now we pick a random sample of 10 numbers from each division. If a division has no numbers or fewer than 10,
    # we handle those cases.
    random_samples = []
    for division in divisions:
        if len(division) == 0:
            random_samples.append([])  # Append an empty list if the division has no numbers
        else:
            # Pick 10 numbers or less if division has fewer than 10 numbers.
            random_samples.append(random.sample(division, min(10, len(division))))

    print("Percentile-based sampling:")
    print(random_samples)
    print(f"Total number of samples: {sum([len(x) for x in random_samples])}")


def stratified_sampling(num_list):
    # Set a seed for reproducibility
    np.random.seed(4332)
    random.seed(4332)

    # Define the number of bins
    num_bins = 10  # Adjust as needed

    # Create histogram and define the bin boundaries
    counts, bin_edges = np.histogram(num_list, bins=num_bins)

    # Create empty list to store the samples
    samples = []

    # Loop through each bin
    for bin_index in range(num_bins):
        # Get the start and end values for each bin
        bin_start = bin_edges[bin_index]
        bin_end = bin_edges[bin_index + 1]

        # Get the values that fall within the current bin
        bin_values = [val for val in num_list if bin_start <= val < bin_end]

        # If bin is not empty, take a sample
        if bin_values:
            # If bin has less than 10 values, take what's available
            if len(bin_values) < 10:
                samples.extend(bin_values)
            else:  # Otherwise take a sample of 10 values
                samples.extend(random.sample(bin_values, 10))

    # Print the samples
    print("Stratified sampling:")
    print(samples)
    print(f"Total samples: {len(samples)}")


def random_sampling(num_list, n_samples):
    # Set a seed for reproducibility
    np.random.seed(4332)
    random.seed(4332)

    # Randomly sample 384 numbers from the list
    random_samples = random.sample(num_list, n_samples)

    return random_samples


def save_sampled_issues(all_issues, sampled_issues, sampled_issues_path):
    sampled_issues_list = []
    for issue_dict in all_issues:
        if issue_dict['id'] in sampled_issues:
            sampled_issues_list.append(issue_dict)

    with open(sampled_issues_path, 'w') as f:
        json.dump(sampled_issues_list, f, indent=4)


if __name__ == "__main__":
    core_issues_path = 'dataset/all_core_issues.json'
    firefox_issues_path = 'dataset/all_firefox_issues.json'
    sampled_issues_path = 'dataset/sampled_issues.json'
    sampled_100_issues_path = 'dataset/sampled_100_issues.json'

    # generate_a_random_number()
    # sys.exit()

    """core_issues = read_issues(core_issues_path)
    firefox_issues = read_issues(firefox_issues_path)

    all_issues = core_issues + firefox_issues

    # print(f'Number of issues: {count_issues(firefox_issues)}')
    # n_comment_list = get_n_comment_list(firefox_issues)
    print(f'Number of total issues: {count_issues(all_issues)}')"""

    """n_comment_list = get_n_comment_list(all_issues)
    draw_boxplot(n_comment_list)
    draw_histogram(n_comment_list)
    percentile_based_sampling(n_comment_list)
    stratified_sampling(n_comment_list)"""

    """issue_id_list = get_issue_id_list(all_issues)
    # print(f"Total # of issues: {len(issue_id_list)}")
    randomly_sampled_issues_id = random_sampling(issue_id_list)
    print(f"# of random samples: {len(randomly_sampled_issues_id)}")
    print(f"Issue IDs of the random samples: {randomly_sampled_issues_id}")

    save_sampled_issues(all_issues, randomly_sampled_issues_id, sampled_core_issues_path)"""

    sampled_issues = read_issues(sampled_issues_path)
    issue_id_list = get_issue_id_list(sampled_issues)
    print("\n--------------------------------")
    print("Statistics of the sampled issues")
    print("--------------------------------")
    print(f'# of sampled issues: {count_issues(sampled_issues)}')

    n_comment_list = get_n_comment_list(sampled_issues)
    print(f'Number of sampled issues: {len(n_comment_list)}')
    print(f"List of # of comments: {n_comment_list}")

    """draw_boxplot(n_comment_list)
    draw_histogram(n_comment_list)
    percentile_based_sampling(n_comment_list)
    stratified_sampling(n_comment_list)"""

    sorted_n_comment_list = sorted(n_comment_list)

    print(f"Sorted list of # of comments: {sorted_n_comment_list}")

    # initializing N
    N = 10

    # using list slicing
    # Get last N elements from list
    largest_10_n_comment_list = sorted_n_comment_list[-N:]
    largest_10_issue_id_list = []

    print(f"List of largest {N} # of comments: {largest_10_n_comment_list}")

    for issue_dict in sampled_issues:
        if len(issue_dict['comments']) in largest_10_n_comment_list:
            largest_10_issue_id_list.append(issue_dict['id'])

    print(f"List of largest {N} issue IDs: {largest_10_issue_id_list}")

    issue_id_list_without_largest_10 = [issue_id for issue_id in issue_id_list if issue_id not in largest_10_issue_id_list]

    print(f"List of issue IDs without the largest {N} issue IDs: {issue_id_list_without_largest_10}")
    print(f"# of issue IDs without the largest {N} issue IDs: {len(issue_id_list_without_largest_10)}")

    randomly_sampled_90_issues_id = random_sampling(issue_id_list_without_largest_10, 90)
    print(f"# of random samples: {len(randomly_sampled_90_issues_id)}")
    print(f"Issue IDs of the random samples: {randomly_sampled_90_issues_id}")

    all_sampled_issues_id = randomly_sampled_90_issues_id + largest_10_issue_id_list

    print(f"# of all sampled issues: {len(all_sampled_issues_id)}")
    print(f"Issue IDs of all sampled issues: {all_sampled_issues_id}")

    save_sampled_issues(sampled_issues, all_sampled_issues_id, sampled_100_issues_path)
