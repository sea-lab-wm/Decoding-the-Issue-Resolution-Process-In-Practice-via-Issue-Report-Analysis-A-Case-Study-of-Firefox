import pandas as pd
from collections import defaultdict


def one_step_leads_to_another(pattern_list, first_step, second_step):
    """
    Count the issues where first_step leads to the second_step.
    """
    # Initialize counters
    n_issues_with_first_step = 0
    n_issues_with_second_step = 0
    n_issues_first_leads_to_second = 0

    # Iterate through each pattern
    for sequence in pattern_list:
        # print(sequence)
        steps = sequence.split(',')  # Split the sequence into individual steps
        if first_step in steps:
            n_issues_with_first_step += 1
        if second_step in steps:
            n_issues_with_second_step += 1
        if first_step in steps and second_step in steps[steps.index(first_step)+1:]:
            n_issues_first_leads_to_second += 1

    # Print out the results
    print(f"# of issues with {first_step}: {n_issues_with_first_step}")
    print(f"# of issues with {second_step}: {n_issues_with_second_step}")
    print(f"# of issues where there {first_step} leads to {second_step}: {n_issues_first_leads_to_second}")
    print(f"% of (# issues where {first_step} leads to {second_step} / # issues with {first_step}): {round((n_issues_first_leads_to_second/n_issues_with_first_step)*100,2)}%")


def one_step_surrounded_by_other(pattern_list, first_step, second_step):
    """
    Count the issues where first_step has an immediate (before or after) second_step.
    """
    # Initialize counter for issues where first_step is immediately before or after second_step
    n_issues_with_first_step = 0
    n_issues_with_second_step = 0
    n_issues_first_next_to_second = 0

    # Iterate through each pattern
    for sequence in pattern_list:
        steps = sequence.split(',')  # Split the sequence into individual steps
        if first_step in steps:
            n_issues_with_first_step += 1
        if second_step in steps:
            n_issues_with_second_step += 1

        # Find all indices of first_step
        indices_of_first_step = [index for index, step in enumerate(steps) if step == first_step]
        for index in indices_of_first_step:
            # Check if the second_step immediately follows or precedes the first_step
            if (index + 1 < len(steps) and steps[index + 1] == second_step) or \
                    (index - 1 >= 0 and steps[index - 1] == second_step):
                n_issues_first_next_to_second += 1
                break  # Only count each sequence once

    # Print out the result
    print(f"# of issues with {first_step}: {n_issues_with_first_step}")
    print(f"# of issues with {second_step}: {n_issues_with_second_step}")
    print(f"# of issues where {first_step} has an immediate (before or after) {second_step}: {n_issues_first_next_to_second}")
    print(f"% of (# issues where {first_step} surrounded by {second_step} / # issues with {first_step}): {round((n_issues_first_next_to_second/n_issues_with_first_step)*100,2)}%")


def one_step_surrounded_by_multiple(pattern_list, first_step, second_step):
    """
    Count the issues where first_step has an immediate (before or after) second_step.
    """
    # Initialize counter for issues where first_step is immediately before or after second_step
    n_issues_with_first_step = 0
    n_issues_with_first_step_at_first_position = 0
    n_issues_with_first_step_at_other_position = 0
    n_issues_with_second_step = 0
    n_issues_first_next_to_second = 0

    # Iterate through each pattern
    for sequence in pattern_list:
        steps = sequence.split(',')  # Split the sequence into individual steps
        if first_step == steps[0]:
            n_issues_with_first_step_at_first_position += 1
        if first_step in steps:
            n_issues_with_first_step += 1

        # Find all indices of first_step
        indices_of_first_step = [index for index, step in enumerate(steps) if step == first_step]

        for index in indices_of_first_step:
            if index == 0:
                continue
            n_issues_with_first_step_at_other_position += 1
            # Check if the second_step immediately follows or precedes the first_step
            if (index + 1 < len(steps) and steps[index + 1] in second_step) or \
                    (index - 1 >= 0 and steps[index - 1] in second_step):
                n_issues_first_next_to_second += 1
                break  # Only count each sequence once

    # Print out the result
    print(f"# of issues with {first_step}: {n_issues_with_first_step}")
    print(f"# of issues with {first_step} at the first position: {n_issues_with_first_step_at_first_position}")
    print(f"# of issues with {first_step} at the other positions: {n_issues_with_first_step_at_other_position}")
    print(f"% of issues where {first_step} appears at other positions: {round((n_issues_with_first_step_at_other_position/n_issues_with_first_step)*100,2)}%")
    print(f"# of issues where non-first {first_step} has an immediate (before or after) {second_step}: {n_issues_first_next_to_second}")
    print(f"% of (# issues where non-first {first_step} surrounded by {second_step} / # issues with non-first {first_step}): {round((n_issues_first_next_to_second/n_issues_with_first_step_at_other_position)*100,2)}%")


def first_step_with_no_or_before_second_step(pattern_list, first_step, second_step):
    """
    Count the issues where first_step appears with no second_step or before the second_step.
    """
    # Initialize counter for issues where first_step is without second_step or before second_step
    n_issues_first_without_or_before_second = 0
    n_issues_with_first_step = 0
    n_issues_with_second_step = 0

    # Iterate through each pattern
    for sequence in pattern_list:
        steps = sequence.split(',')  # Split the sequence into individual steps
        if first_step in steps:
            n_issues_with_first_step += 1
        if second_step in steps:
            n_issues_with_second_step += 1
        if first_step in steps:
            # Check if second_step is not in the steps or if first_step comes before second_step
            if second_step not in steps or steps.index(first_step) < steps.index(second_step):
                # print(sequence)
                n_issues_first_without_or_before_second += 1

    # Print out the result
    print(f"# of issues with {first_step}: {n_issues_with_first_step}")
    print(f"# of issues with {second_step}: {n_issues_with_second_step}")
    print(f"# of issues where {first_step} appears with no/before {second_step}: {n_issues_first_without_or_before_second}")
    print(f"% of (# issues where {first_step} appears with no/before {second_step} / # issues with {first_step}): {round((n_issues_first_without_or_before_second/n_issues_with_first_step)*100,2)}%")


def create_matrix(data_frame, matrix_file_path, matrix_of):
    if matrix_of == 'Steps':
        column_name = 'step_seq_with_selected_codes'
    elif matrix_of == 'Codes':
        column_name = 'code_seq_abbreviated'

    # Extract unique steps
    unique_elements = sorted(set(step for sequence in data_frame[column_name] for step in sequence.split(',')))

    # Initialize the matrix with zeros
    matrix = pd.DataFrame(0, index=unique_elements, columns=unique_elements)

    # Populate the matrix
    for sequence in data_frame[column_name]:
        elements_in_sequence = sequence.split(',')
        unique_elements_in_sequence = set(elements_in_sequence)
        for element in unique_elements_in_sequence:
            for other_element in unique_elements_in_sequence:
                matrix.loc[element, other_element] += 1

    # Rename the index label to 'Steps/Codes'
    if matrix_of == 'Steps':
        matrix.index.name = 'Steps'
    elif matrix_of == 'Codes':
        matrix.index.name = 'Codes'

    # Saving the matrix to a CSV file
    matrix.to_csv(matrix_file_path)


def create_matrix_first_and_second_steps(data_frame, matrix_file_path, matrix_of):
    if matrix_of == 'Steps':
        column_name = 'step_seq_with_selected_codes'
    elif matrix_of == 'Codes':
        column_name = 'code_seq_abbreviated'

    # Extract unique elements from the first and second elements of each sequence
    unique_first_elements = sorted(set(
        sequence.split(',')[0]
        for sequence in data_frame[column_name]
        if len(sequence.split(',')) > 1
    ))

    unique_second_elements = sorted(set(
        sequence.split(',')[1]
        for sequence in data_frame[column_name]
        if len(sequence.split(',')) > 1
    ))

    # Initialize the matrix with zeros
    matrix = pd.DataFrame(0, index=unique_first_elements, columns=unique_second_elements)

    # Populate the matrix
    for sequence in data_frame[column_name]:
        elements_in_sequence = sequence.split(',')
        if len(elements_in_sequence) < 2:
            continue  # Skip sequences that don't have at least two elements
        first_element = elements_in_sequence[0]
        second_element = elements_in_sequence[1]
        matrix.loc[first_element, second_element] += 1

    # Rename the index label to 'Steps/Codes'
    if matrix_of == 'Steps':
        matrix.index.name = 'First Steps'
        matrix.columns.name = 'Second Steps'
    elif matrix_of == 'Codes':
        matrix.index.name = 'First Codes'
        matrix.columns.name = 'Second Codes'

    # Saving the matrix to a CSV file
    matrix.to_csv(matrix_file_path)


def multiple_occurrences_of_step(pattern_list, step):
    """
    Count the number of issues where the specified step appears more than once.

    Parameters:
    - step: The step to check for multiple occurrences.
    - sequences: A list of step sequences (str) from issues.

    Returns:
    - The count of issues where the step appears more than once.
    """
    n_issues_with_step = 0
    n_issues_with_multiple_step = 0
    for pattern in pattern_list:
        steps = pattern.split(',')
        if step in steps:
            n_issues_with_step += 1
        if steps.count(step) > 1:
            n_issues_with_multiple_step += 1

    # Print out the result
    print(f"# of issues with {step}: {n_issues_with_step}")
    print(f"# of issues with multiple {step}: {n_issues_with_multiple_step}")
    print(f"% of (# issues with multiple {step} / # issues with {step}): {round((n_issues_with_multiple_step/n_issues_with_step)*100,2)}%")


def count_issues_first_after_second(pattern_list, first_step, second_step):
    """
    Count the number of issues where first_step occurs after second_step.

    Parameters:
    - first_step: The step that needs to occur after.
    - second_step: The step that needs to occur before.
    - pattern_list: A list of patterns (str) of issues.
    """
    n_issues_with_first_step = 0
    n_issues_with_second_step = 0
    n_issues_with_first_step_after_second = 0
    for pattern in pattern_list:
        steps = pattern.split(',')
        if first_step in steps:
            n_issues_with_first_step += 1
        if second_step in steps:
            n_issues_with_second_step += 1
        if second_step in steps and first_step in steps:
            if steps.index(first_step) > steps.index(second_step):
                n_issues_with_first_step_after_second += 1

    # Print out the result
    print(f"# of issues with {first_step}: {n_issues_with_first_step}")
    print(f"# of issues with {second_step}: {n_issues_with_second_step}")
    print(f"# of issues where {first_step} appears after {second_step}: {n_issues_with_first_step_after_second}")
    print(f"% of (# issues where {first_step} appears after {second_step} / # issues with {first_step}): {round((n_issues_with_first_step_after_second/n_issues_with_first_step)*100,2)}%")


def get_first_step_stats(pattern_list):
    # Initialize data structures
    unique_steps = set()
    first_step_counts = {}

    # Populate unique steps and count last step occurrences
    for sequence in pattern_list:
        steps = sequence.split(',')
        unique_steps.update(steps)
        first_step = steps[0]
        if first_step not in first_step_counts:
            first_step_counts[first_step] = 1
        else:
            first_step_counts[first_step] += 1

    # Calculate percentages
    total_issues = len(pattern_list)
    last_step_percentages = {step: (count / total_issues) * 100 for step, count in first_step_counts.items()}

    # Print header
    print("\n\n First step stats")
    print("===================")
    print("Step;# of Issues with last step;% of Issues in all Issues")
    for step in unique_steps:
        # Get the number of issues where the step is the last step
        num_issues_first_step = first_step_counts.get(step, 0)
        # Calculate the percentage
        percentage = (num_issues_first_step / total_issues) * 100 if total_issues > 0 else 0
        # Print the formatted information
        print(f"{step};{num_issues_first_step};{percentage:.2f}%")


def get_last_step_stats(pattern_list):
    """
    Analyze the given pattern list to find:
    1. The list of unique steps.
    2. The number of issues where each step is the last step.
    3. The percentage of item 2 in all issues.

    Parameters:
    - pattern_list: A list of step sequences (str) from issues.

    Returns:
    - A summary of the analysis including the list of unique steps, the count, and percentage of issues
      where each step is the last step.
    """
    # Initialize data structures
    unique_steps = set()
    last_step_counts = {}

    # Populate unique steps and count last step occurrences
    for sequence in pattern_list:
        steps = sequence.split(',')
        unique_steps.update(steps)
        last_step = steps[-1]
        if last_step not in last_step_counts:
            last_step_counts[last_step] = 1
        else:
            last_step_counts[last_step] += 1

    # Calculate percentages
    total_issues = len(pattern_list)
    last_step_percentages = {step: (count / total_issues) * 100 for step, count in last_step_counts.items()}

    # Print header
    print("\n\n Last step stats")
    print("===================")
    print("Step;# of Issues with last step;% of Issues in all Issues")
    for step in unique_steps:
        # Get the number of issues where the step is the last step
        num_issues_last_step = last_step_counts.get(step, 0)
        # Calculate the percentage
        percentage = (num_issues_last_step / total_issues) * 100 if total_issues > 0 else 0
        # Print the formatted information
        print(f"{step};{num_issues_last_step};{percentage:.2f}%")


def get_following_steps_stats(pattern_list, given_step):
    # Track occurrences of steps immediately following the given step, without overcounting within the same issue
    following_step_counts = {}
    total_issues = len(pattern_list)

    for sequence in pattern_list:
        steps = sequence.split(',')
        found_following_steps = set()  # Track found following steps in this issue to avoid overcounting
        for i, step in enumerate(steps[:-1]):  # Ignore the last step as it cannot be "followed" by another step
            if step == given_step and steps[i + 1] not in found_following_steps:
                next_step = steps[i + 1]
                following_step_counts[next_step] = following_step_counts.get(next_step, 0) + 1
                found_following_steps.add(next_step)
                break  # Only count each sequence once

    # Calculate percentages for each step that follows the given step
    following_steps_percentages = {step: (count / total_issues) * 100 for step, count in following_step_counts.items()}

    # Print header
    print("\n\n Following step stats")
    print("===================")
    # Print the findings
    print("Step,# of Issues with step immediately after the given step,% of Issues in all Issues")
    for step, count in following_step_counts.items():
        print(f"{step},{count},{following_steps_percentages[step]:.2f}")


def get_preceding_steps_stats(pattern_list, given_step):
    """
    Count the number of issues where each step immediately precedes the given step,
    ensuring that repeated occurrences within the same issue are not overcounted.

    Parameters:
    - pattern_list: A list of step sequences from issues.
    - given_step: The step to analyze for what immediately precedes it.

    Returns:
    - A summary of steps that immediately precede the given step, along with the count and percentage.
    """
    # Track occurrences of steps immediately preceding the given step, without overcounting within the same issue
    preceding_step_counts = {}
    total_issues = len(pattern_list)

    for sequence in pattern_list:
        steps = sequence.split(',')
        found_preceding_steps = set()  # Track found preceding steps in this issue to avoid overcounting
        for i in range(1, len(steps)):  # Start from the second step
            if steps[i] == given_step and steps[i-1] not in found_preceding_steps:
                preceding_step = steps[i-1]
                preceding_step_counts[preceding_step] = preceding_step_counts.get(preceding_step, 0) + 1
                found_preceding_steps.add(preceding_step)
                break  # Only count each sequence once

    # Calculate percentages for each step that precedes the given step
    preceding_steps_percentages = {step: (count / total_issues) * 100 for step, count in preceding_step_counts.items()}

    # Print header
    print("\n\n Preceding step stats")
    print("===================")
    # Print the findings
    print("Step,# of Issues with step immediately before the given step,% of Issues in all Issues")
    for step, count in preceding_step_counts.items():
        print(f"{step},{count},{preceding_steps_percentages[step]:.2f}")


def count_ngrams(pattern_list, n):
    """
    Count the number of issues where each unique n-gram (bi-gram or tri-gram) is found,
    skipping non-string and empty patterns.

    Parameters:
    - pattern_list: A list of step sequences from issues, expected to be strings.
    - n: The size of the n-gram (2 for bi-gram, 3 for tri-gram).

    Returns:
    - A dictionary of n-grams and their occurrence counts across issues.
    """
    ngram_counts = {}
    for sequence in pattern_list:
        # Skip non-string and empty patterns
        if not isinstance(sequence, str) or not sequence.strip():
            continue
        steps = sequence.split(',')
        # Skip patterns with fewer steps than the size of the n-gram
        if len(steps) < n:
            continue
        found_ngrams = set()
        for i in range(len(steps) - n + 1):
            ngram = tuple(steps[i:i+n])
            if ngram not in found_ngrams:  # Avoid counting the same n-gram multiple times within an issue
                ngram_counts[ngram] = ngram_counts.get(ngram, 0) + 1
                found_ngrams.add(ngram)

    for bi_gram, count in ngram_counts.items():
        print(f"{','.join(bi_gram)}: {count}")


def get_bi_grams(pattern_list):
    # Initialize counters
    bi_gram_issue_counts = defaultdict(int)
    first_step_issue_counts = defaultdict(int)
    second_step_issue_counts = defaultdict(int)
    both_steps_issue_counts = defaultdict(int)

    # Identify and count bi-grams, and count individual steps
    for issue in pattern_list:
        if issue:  # Ensure the issue is not empty
            if not isinstance(issue, str) or not issue.strip():
                continue
            steps = issue.split(',')
            seen_bi_grams = set()  # Track bi-grams seen in this issue to avoid double counting
            for i in range(len(steps) - 1):
                bi_gram = (steps[i], steps[i + 1])
                seen_bi_grams.add(bi_gram)

            # Update bi-gram counts
            for bi_gram in seen_bi_grams:
                bi_gram_issue_counts[bi_gram] += 1

    for issue in pattern_list:
        if issue:  # Ensure the issue is not empty
            if not isinstance(issue, str) or not issue.strip():
                continue
            steps = issue.split(',')

            # Count issues containing the steps of each bi-gram
            for bi_gram in bi_gram_issue_counts.keys():
                if bi_gram[0] in steps:
                    first_step_issue_counts[bi_gram] += 1
                if bi_gram[1] in steps:
                    second_step_issue_counts[bi_gram] += 1
                if bi_gram[0] in steps and bi_gram[1] in steps:
                    both_steps_issue_counts[bi_gram] += 1

    # Prepare results
    results = []
    for bi_gram, count in bi_gram_issue_counts.items():
        results.append({
            "Bi-gram": f"{bi_gram[0]},{bi_gram[1]}",
            "# of issues containing bi-gram": count,
            "# of issues containing 1st step": first_step_issue_counts[bi_gram],
            "# of issues containing 2nd step": second_step_issue_counts[bi_gram],
            "# of issues containing both steps": both_steps_issue_counts[bi_gram]
        })
    df = pd.DataFrame(results)
    df.to_csv('bi_gram_counts.csv')


def get_tri_grams(pattern_list):
    # Initialize counters
    tri_gram_issue_counts = defaultdict(int)
    first_step_issue_counts = defaultdict(int)
    second_step_issue_counts = defaultdict(int)
    third_step_issue_counts = defaultdict(int)
    all_three_steps_issue_counts = defaultdict(int)
    tri_gram_total_occurrences = defaultdict(int)

    # Identify and count tri-grams
    for issue in pattern_list:
        if not issue:  # Ensure the issue is not empty
            continue
        if not isinstance(issue, str) or not issue.strip():
            continue
        steps = issue.split(',')
        seen_tri_grams = set()  # Track tri-grams seen in this issue to avoid double counting
        for i in range(len(steps) - 2):
            tri_gram = (steps[i], steps[i + 1], steps[i + 2])
            seen_tri_grams.add(tri_gram)
            tri_gram_total_occurrences[tri_gram] += 1

        # Update tri-gram counts
        for tri_gram in seen_tri_grams:
            tri_gram_issue_counts[tri_gram] += 1

    # Count issues containing the steps of each tri-gram
    for issue in pattern_list:
        if not issue:  # Ensure the issue is not empty
            continue
        if not isinstance(issue, str) or not issue.strip():
            continue
        steps = issue.split(',')

        for tri_gram in tri_gram_issue_counts.keys():
            if tri_gram[0] in steps:
                first_step_issue_counts[tri_gram] += 1
            if tri_gram[1] in steps:
                second_step_issue_counts[tri_gram] += 1
            if tri_gram[2] in steps:
                third_step_issue_counts[tri_gram] += 1
            if tri_gram[0] in steps and tri_gram[1] in steps and tri_gram[2] in steps:
                all_three_steps_issue_counts[tri_gram] += 1

    # Prepare results
    results = []
    for tri_gram, count in tri_gram_issue_counts.items():
        results.append({
            "Tri-gram": f"{tri_gram[0]},{tri_gram[1]},{tri_gram[2]}",
            "# of issues containing tri-gram": count,
            "# of issues containing 1st step": first_step_issue_counts[tri_gram],
            "# of issues containing 2nd step": second_step_issue_counts[tri_gram],
            "# of issues containing 3rd step": third_step_issue_counts[tri_gram],
            "# of issues containing all three steps": all_three_steps_issue_counts[tri_gram],
            "Total occurrences of tri-gram": tri_gram_total_occurrences[tri_gram]
        })

    df = pd.DataFrame(results)
    df.to_csv('./files/tri_gram_counts.csv')


def create_consecutive_matrix(data_frame, matrix_file_path):
    column_name = 'step_seq_with_selected_codes'

    # Define the order of unique steps explicitly, including NO_STAGE, NO_SOURCE, and NO_TARGET
    unique_elements = ['NO_STAGE', 'NO_SOURCE', 'ISU_REP', 'ISU_ANLYS', 'SOL_DES', 'IMPL', 'CR', 'VER', 'NO_TARGET']

    # Initialize the matrix with zeros
    matrix = pd.DataFrame(0, index=unique_elements, columns=unique_elements)

    # # Populate the matrix with the count of sequences where each bigram appears at least once
    # for sequence in data_frame[column_name]:
    #     if sequence == 'NO_STAGE':
    #         # Handle sequences with NO_STAGE
    #         matrix.loc['NO_STAGE', 'NO_STAGE'] += 1
    #     else:
    #         elements_in_sequence = sequence.split(',')
    #         if len(elements_in_sequence) == 1:
    #             # Handle sequences with only one step
    #             step = elements_in_sequence[0]
    #             matrix.loc['NO_SOURCE', step] += 1
    #             matrix.loc[step, 'NO_TARGET'] += 1
    #         else:
    #             bigrams_in_sequence = set((elements_in_sequence[i], elements_in_sequence[i + 1]) for i in range(len(elements_in_sequence) - 1))
    #             for source, target in bigrams_in_sequence:
    #                 if source in unique_elements and target in unique_elements:
    #                     matrix.loc[source, target] += 1

    # # Populate the matrix with the count of bigram occurrences
    # for sequence in data_frame[column_name]:
    #     if sequence == 'NO_STAGE':
    #         # Handle sequences with NO_STAGE
    #         matrix.loc['NO_STAGE', 'NO_STAGE'] += 1
    #     else:
    #         elements_in_sequence = sequence.split(',')
    #         if len(elements_in_sequence) == 1:
    #             # Handle sequences with only one step
    #             step = elements_in_sequence[0]
    #             matrix.loc['NO_SOURCE', step] += 1
    #             matrix.loc[step, 'NO_TARGET'] += 1
    #         else:
    #             for i in range(len(elements_in_sequence) - 1):
    #                 source = elements_in_sequence[i]
    #                 target = elements_in_sequence[i + 1]
    #                 if source in unique_elements and target in unique_elements:
    #                     matrix.loc[source, target] += 1

    # Populate the matrix with the count of issues where either (source,target) or (target,source) appears
    for sequence in data_frame[column_name]:
        if sequence == 'NO_STAGE':
            # Handle sequences with NO_STAGE
            matrix.loc['NO_STAGE', 'NO_STAGE'] += 1
        else:
            elements_in_sequence = sequence.split(',')
            if len(elements_in_sequence) == 1:
                # Handle sequences with only one step
                step = elements_in_sequence[0]
                matrix.loc['NO_SOURCE', step] += 1
                matrix.loc[step, 'NO_TARGET'] += 1
            else:
                seen_bigrams = set()
                for i in range(len(elements_in_sequence) - 1):
                    source = elements_in_sequence[i]
                    target = elements_in_sequence[i + 1]
                    if (source, target) not in seen_bigrams and (target, source) not in seen_bigrams:
                        if source in unique_elements and target in unique_elements:
                            matrix.loc[source, target] += 1
                            matrix.loc[target, source] += 1
                            seen_bigrams.add((source, target))
                            seen_bigrams.add((target, source))

    matrix.index.name = 'Steps'
    matrix.columns.name = 'Target Steps'

    # Saving the matrix to a CSV file
    matrix.to_csv(matrix_file_path)


if __name__ == '__main__':
    pattern_file_path = './files/patterns.csv'
    steps_matrix_file_path = './files/step_matrix.csv'
    codes_matrix_file_path = './files/code_matrix.csv'
    consequtive_steps_matrix = './files/consequtive_steps_matrix.csv'
    first_and_second_steps_matrix = './files/first_and_second_steps_matrix.csv'

    # Load the CSV data into a pandas DataFrame
    df = pd.read_csv(pattern_file_path, sep=';')
    pattern_list = df['step_seq_with_selected_codes']
    # create_consecutive_matrix(df, consequtive_steps_matrix)
    # print(pattern_list)
    get_tri_grams(pattern_list)

    # create_matrix_first_and_second_steps(df, first_and_second_steps_matrix, 'Steps')

    # get_following_steps_stats(pattern_list, "ISU_REP")
    # get_following_steps_stats(pattern_list, "ISU_ANLYS")
    # get_following_steps_stats(pattern_list, "SOL_DES")
    # get_following_steps_stats(pattern_list, "IMPL")
    # get_following_steps_stats(pattern_list, "CR")
    # get_following_steps_stats(pattern_list, "VER")
    # get_following_steps_stats(pattern_list, "SOL_DES")
    # get_preceding_steps_stats(pattern_list, "ISU_REP")
    # get_preceding_steps_stats(pattern_list, "ISU_ANLYS")
    # get_preceding_steps_stats(pattern_list, "SOL_DES")
    # get_preceding_steps_stats(pattern_list, "IMPL")
    # get_preceding_steps_stats(pattern_list, "CR")
    # get_preceding_steps_stats(pattern_list, "VER")

    # get_bi_grams(pattern_list)
    # get_tri_grams(pattern_list)

    # create_matrix(df, steps_matrix_file_path, 'Steps')
    # create_matrix(df, codes_matrix_file_path, 'Codes')

    """# 1. In how many issues does code review lead to further implementation?
    print(f"\n1. In how many issues does code review lead to further implementation?")
    first_step = "CR"
    second_step = "IMPL"
    one_step_leads_to_another(pattern_list, first_step, second_step)

    # 2. In how many issues does verification lead to further implementation?
    print(f"\n2. In how many issues does verification lead to further implementation?")
    first_step = "VER"
    second_step = "IMPL"
    one_step_leads_to_another(pattern_list, first_step, second_step)

    # 3. In how many issues does implementation have an immediate (before or after) solution design?
    print(f"\n3. In how many issues does implementation have an immediate (before or after) solution design?")
    first_step = "IMPL"
    second_step = "SOL_DES"
    one_step_surrounded_by_other(pattern_list, first_step, second_step)

    # 4. In how many issues does solution design have an immediate (before or after) issue analysis?
    print(f"\n4. In how many issues does solution design have an immediate (before or after) issue analysis?")
    first_step = "SOL_DES"
    second_step = "ISU_ANLYS"
    one_step_surrounded_by_other(pattern_list, first_step, second_step)

    # 5. In how many issues does issue analysis have an immediate (before or after) solution design?
    print(f"\n5. In how many issues does issue analysis have an immediate (before or after) solution design?")
    first_step = "ISU_ANLYS"
    second_step = "SOL_DES"
    one_step_surrounded_by_other(pattern_list, first_step, second_step)

    # 10. In how many issues does issue reproduction have an immediate (before or after) issue analysis?
    print(f"\n10. In how many issues does issue reproduction have an immediate (before or after) issue analysis?")
    first_step = "ISU_REP"
    second_step = "ISU_ANLYS"
    one_step_surrounded_by_other(pattern_list, first_step, second_step)

    # 11. In how many issues does issue analysis have an immediate (before or after) issue reproduction?
    print(f"\n11. In how many issues does issue analysis have an immediate (before or after) issue reproduction?")
    first_step = "ISU_ANLYS"
    second_step = "ISU_REP"
    one_step_surrounded_by_other(pattern_list, first_step, second_step)

    # 12. In how many issues does verification appear with no implementation or before the implementation?
    print(f"\n12. In how many issues does verification appear with no implementation or before the implementation?")
    first_step = "VER"
    second_step = "IMPL"
    first_step_with_no_or_before_second_step(pattern_list, first_step, second_step)

    # 13. In how many issues does solution design have an immediate (before or after) implementation?
    print(f"\n13. In how many issues does solution design have an immediate (before or after) implementation?")
    first_step = "SOL_DES"
    second_step = "IMPL"
    one_step_surrounded_by_other(pattern_list, first_step, second_step)

    # 14. In how many issues does ISU_REP occur multiple times?
    print(f"\n14. In how many issues does ISU_REP occur multiple times?")
    pattern_list = df['step_seq_with_selected_codes']
    step = "ISU_REP"
    multiple_occurrences_of_step(pattern_list, step)

    # 15. In how many issues does ISU_REP occur after IMPL?
    print(f"\n15. In how many issues does ISU_REP occur after IMPL?")
    pattern_list = df['step_seq_with_selected_codes']
    first_step = "ISU_REP"
    second_step = "IMPL"
    count_issues_first_after_second(pattern_list, first_step, second_step)

    # 16. In how many issues does code review lead to verification?
    print(f"\n16. In how many issues does code review lead to verification?")
    first_step = "CR"
    second_step = "VER"
    one_step_leads_to_another(pattern_list, first_step, second_step)

    # 17. In how many issues does verification lead to code review?
    print(f"\n17. In how many issues does verification lead to code review?")
    first_step = "VER"
    second_step = "CR"
    one_step_leads_to_another(pattern_list, first_step, second_step)"""

    # get_last_step_stats(pattern_list)

    # get_following_steps_stats(pattern_list, "VER")
    # get_following_steps_stats(pattern_list, "IMPL")
    # get_following_steps_stats(pattern_list, "CR")
    # get_preceding_steps_stats(pattern_list, "IMPL")

    # get_following_steps_stats(pattern_list, "ISU_REP")
    # get_preceding_steps_stats(pattern_list, "ISU_REP")

    # get_first_step_stats(pattern_list)

    """
    # These questions are not needed anymore.
    # 6. In how many issues does non-first issue description have an immediate (before or after) issue analysis?
    print(f"\n6. In how many issues does issue non-first description have an immediate (before or after) solution design?")
    first_step = "ISU_DES"
    second_step = ["ISU_ANLYS"]
    one_step_surrounded_by_multiple(pattern_list, first_step, second_step)

    # 7. In how many issues does non-first issue description have an immediate (before or after) issue reproduction?
    print(f"\n6. In how many issues does issue non-first description have an immediate (before or after) solution design?")
    first_step = "ISU_DES"
    second_step = ["ISU_REP"]
    one_step_surrounded_by_multiple(pattern_list, first_step, second_step)

    # 8. In how many issues does non-first issue description have an immediate (before or after) solution design?
    print(f"\n8. In how many issues does non-first issue description have an immediate (before or after) solution design?")
    first_step = "ISU_DES"
    second_step = ["SOL_DES"]
    one_step_surrounded_by_multiple(pattern_list, first_step, second_step)

    # 9. In how many issues does non-first issue description have an immediate (before or after) solution design?
    print(f"\n9. In how many issues does non-first issue description have an immediate (before or after) issue reproduction/issue analysis/solution design?")
    first_step = "ISU_DES"
    second_step = ["ISU_REP", "ISU_ANLYS", "SOL_DES"]
    one_step_surrounded_by_multiple(pattern_list, first_step, second_step)"""


