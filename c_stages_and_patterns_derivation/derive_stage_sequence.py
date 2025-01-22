import sys
from c_sample_issues import read_issues, count_issues
import csv
import json
import pandas as pd
from collections import Counter
from collections import defaultdict
import copy

# All 356 coded issues
annotated_issues_id_list = [538721, 551837, 552914, 554061, 558970, 561168, 576837, 577462, 590389, 596726, 597389,
                            601912, 601999, 626855, 627984, 634654, 642412, 659018, 670853, 674446, 674609, 675961,
                            676248, 677173, 687929, 691184, 695213, 696748, 698552, 700508, 714547, 717147, 722137,
                            724586, 730907, 731836, 738440, 738759, 752781, 758103, 768901, 779500, 783505, 790547,
                            794507, 797889, 801993, 811773, 812431, 817341, 817531, 822952, 823917, 833964, 835157,
                            837955, 838565, 840284, 851828, 857034, 861246, 866470, 866474, 888630, 894646, 894931,
                            897027, 904571, 906912, 912496, 919434, 924397, 927544, 937475, 939475, 947523, 957093,
                            966240, 978610, 983489, 985257, 989204, 991812, 1003694, 1023280, 1025075, 1029919, 1033283,
                            1033887, 1047560, 1048721, 1055843, 1057903, 1066726, 1071367, 1074012, 1076026, 1080574,
                            1104875, 1105771, 1111046, 1116867, 1118597, 1118599, 1121826, 1130065, 1130253, 1132780,
                            1148078, 1173001, 1176028, 1184282, 1184945, 1187056, 1189924, 1190676, 1191113, 1203871,
                            1207931, 1209952, 1217192, 1217663, 1247539, 1252039, 1253516, 1253884, 1261576, 1262069,
                            1263083, 1268252, 1287522, 1297315, 1300206, 1306719, 1314193, 1315285, 1316964, 1319370,
                            1324053, 1324183, 1325297, 1325731, 1328511, 1329110, 1332070, 1339619, 1343787, 1344721,
                            1354406, 1357065, 1357386, 1359490, 1362590, 1373154, 1373249, 1382702, 1384677, 1385699,
                            1386502, 1390087, 1396319, 1401299, 1403319, 1405027, 1407955, 1410565, 1421170, 1430012,
                            1435264, 1435456, 1441779, 1454126, 1456911, 1467403, 1479989, 1482681, 1486218, 1487135,
                            1493860, 1494092, 1506200, 1509994, 1510786, 1514429, 1515665, 1521066, 1529006, 1537936,
                            1560574, 1569123, 1570673, 1571487, 1574259, 1581315, 1593658, 1598488, 1600320, 1614706,
                            1623400, 1624268, 1625850, 1629902, 1637897, 1640135, 1651332, 1651593, 1654383, 1662097,
                            1666607, 1677183, 1683093, 1686219, 1686238, 1688325, 1705253, 1705768, 1706916, 1716655,
                            1718748, 1732739, 1733898, 1742664, 1742770, 1748376, 1748902, 1751268, 1751721, 1751919,
                            1761435, 1761826, 1761994, 1762088, 1764716, 1769254, 1769748, 1774026, 1778644, 1790543,
                            1792203, 1794237, 1818468, 597071, 658675, 667586, 682449, 687754, 735312, 794101, 916390,
                            948882, 1073339, 1079905, 1092808, 1097236, 1132964, 1183934, 1203253, 1249818, 1254694,
                            1265066, 1271750, 1353954, 1355481, 1357049, 1401249, 1407435, 1421905, 1442559, 1455735,
                            1458856, 1462624, 1465254, 1469362, 1479309, 1485422, 1513854, 1519164, 1526439, 1565273,
                            1571472, 1576600, 1576778, 1579004, 1584273, 1615767, 1618477, 1630806, 1634650, 1644719,
                            1661727, 1689742, 1703558, 1705327, 1715838, 1717682, 1718031, 1762292, 1768744, 1769085,
                            1811466, 1815706, 819493, 1439571, 1096093, 593387, 552359, 1298588, 1179123, 1823751,
                            1340967, 1514062, 1093374, 855335, 1142350, 585832, 1728953, 1187966, 1809080, 1622369,
                            1753765, 1647930, 869069, 852135, 1347860, 686900, 1670911, 1486074, 1685379, 713597,
                            1516605, 1571124, 1821213, 660762, 1248726, 759033, 1645527, 1395751, 587434, 623742,
                            1820814, 1704164, 1024256, 1626111, 1794406, 1600017, 900384, 1363344, 874258, 712870,
                            1221593, 734506, 600489, 1528712, 1540794, 1079321, 1424993]
print(f"Total number of annotated issues: {len(annotated_issues_id_list)}")

code_abbreviation_dict = {
    "REPRODUCTION_REQUEST": "REP_REQ",
    "REPRODUCTION_ATTEMPT": "REP_ATT",
    "PROBLEM_LOCALIZATION": "PRB_LOC",
    "PROBLEM_REVIEW_REQUEST": "PRB_REV_REQ",
    "PROBLEM_REVIEW": "PRB_REV",
    "PROBLEM_CAUSE_IDENTIFICATION": "PRB_CUS_IDN",
    "POTENTIAL_SOLUTION_DESIGN": "POT_SOL_DES",
    "SOLUTION_REVIEW_REQUEST": "SOL_REV_REQ",
    "SOLUTION_REVIEW": "SOL_REV",
    "CODE_IMPLEMENTATION": "COD_IMP",
    "CODE_REVIEW_REQUEST": "COD_REV_REQ",
    "CODE_REVIEW": "COD_REV",
    "CODE_UPDATE_REQUEST": "COD_UP_REQ",
    "VERIFICATION_REQUEST": "VER_REQ",
    "SOLUTION_VERIFICATION": "SOL_VER",
    "UPLIFT_APPROVAL": "UPLFT_APRV",
    "IMPLEMENTATION_REVERSION": "IMP_REVRSN",
    "COLLATERAL_PROBLEM_ANALYSIS": "CO_PRB_CUS",
    "COLLATERAL_POTENTIAL_SOLUTION": "CO_POT_SOL",
    "SOLVED_BY_OTHER_ISSUE": "SLVD_BY_ISUE",
    "ISSUE_IMPACT": "ISUE_IMPCT",
    "NEW_ISSUE_FILING": "FLD_NW_ISUE"
}

code_stage_dict = {
    "ISU_REP": ["REP_REQ", "REP_ATT"],
    "ISU_ANLYS": ["PRB_LOC", "PRB_REV_REQ", "PRB_REV", "PRB_CUS_IDN"],
    "SOL_DES": ["POT_SOL_DES", "SOL_REV_REQ", "SOL_REV"],
    "IMPL": ["COD_IMP"],
    "CR": ["COD_REV_REQ", "COD_REV", "COD_UP_REQ"],
    "VER": ["VER_REQ", "SOL_VER", "UPLFT_APRV", "IMP_REVRSN", "CO_PRB_CUS", "CO_POT_SOL"]
}

# This list contains non-actionable and cross-cutting codes
non_actionable_codes = ["REP_REQ", "PRB_REV_REQ", "SOL_REV_REQ", "COD_REV_REQ", "COD_UP_REQ", "VER_REQ", "SLVD_BY_ISUE",
                        "ISUE_IMPCT", "FLD_NW_ISUE"]


def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def get_all_info_of_annotated_issues(all_issues_path, annotated_issues_path):
    all_issues = read_issues(all_issues_path)
    print(f"Total number of issues: {count_issues(all_issues)}")
    print(f"Total number of annotated issues: {len(annotated_issues_id_list)}")

    annotated_issues = []
    for issue in all_issues:
        if issue['id'] in annotated_issues_id_list:
            annotated_issues.append(issue)

    with open(annotated_issues_path, 'w') as json_file:
        json.dump(annotated_issues, json_file, indent=4)


def create_stage_sequence(code_sequence):
    # Create the stage sequence by replacing the annotation code with the stage
    stage_sequence = []
    for text in code_sequence.split(','):
        stage = None
        for key, value_list in code_stage_dict.items():
            if text in value_list:
                stage = key
                break
        if stage:
            stage_sequence.append(stage)

    # Keep only one stage if there are multiple consecutive same steps
    if len(stage_sequence) > 0:
        stage_sequence = [stage_sequence[0]] + [text for i, text in enumerate(stage_sequence[1:]) if
                                                text != stage_sequence[i]]
    # print(step_sequence)
    stage_sequence = ','.join(stage_sequence)

    return stage_sequence


def remove_consecutive_repeating_elements(sequence):
    # Keep only one element if there are multiple consecutive same elements
    sequence_list = sequence.split(',')
    sequence_list = [sequence_list[0]] + [text for i, text in enumerate(sequence_list[1:]) if text != sequence_list[i]]
    sequence = ','.join(sequence_list)

    return sequence


def derive_stage_sequence(annotation_data_path, pattern_file_path):
    with open(annotation_data_path) as f:
        annotation_data = json.load(f)

    # Open the CSV file in write mode
    with open(pattern_file_path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)

        # Write the header row
        writer.writerow(
            ['issue_id', 'url', 'code_seq_with_all_codes', 'code_seq_abbreviated', 'code_seq_with_selected_codes',
             'stage_seq_with_selected_codes', 'n_code_seq_all_codes', 'n_code_seq_selected_codes',
             'n_stage_seq_selected_codes']
        )

        # Iterate over the JSON annotation_data
        for issue in annotation_data:
            issue_id = issue['issue_id']
            if issue_id not in annotated_issues_id_list:
                continue
            url = issue['url']

            # Create code sequence with all codes
            annotation_codes = [annotation['code'] for annotation in issue['annotations']]
            code_seq_with_all_codes = ','.join(annotation_codes)

            # Create code sequence (abbreviated) using the abbreviation dictionary with all codes
            code_seq_abbreviated = [code_abbreviation_dict.get(text, text) for text in
                                    code_seq_with_all_codes.split(',')]
            code_seq_abbreviated = ','.join(code_seq_abbreviated)
            # print(code_seq_abbreviated)

            # Create code sequence with selected codes by excluding non-actionable and cross-cutting codes
            code_seq_with_selected_codes = [text for text in code_seq_abbreviated.split(',') if
                                            text not in non_actionable_codes]
            code_seq_with_selected_codes = ','.join(code_seq_with_selected_codes)

            # Create stage sequence with selected codes
            stage_seq_with_selected_codes = create_stage_sequence(code_seq_with_selected_codes)
            # stage_seq_with_selected_codes = remove_consecutive_repeating_elements(stage_seq_with_selected_codes)

            # Compute the number of codes and stages
            n_code_seq_all_codes = len(code_seq_with_all_codes.split(','))
            n_code_seq_selected_codes = len(code_seq_with_all_codes.split(','))
            n_stage_seq_selected_codes = len(stage_seq_with_selected_codes.split(','))

            # For the stage sequence with no stages
            if stage_seq_with_selected_codes == "":
                stage_sequence = ["NO_STAGE"]
                stage_seq_with_selected_codes = ','.join(stage_sequence)

            # Write a row for each record
            writer.writerow(
                [issue_id, url, code_seq_with_all_codes, code_seq_abbreviated, code_seq_with_selected_codes,
                 stage_seq_with_selected_codes, n_code_seq_all_codes, n_code_seq_selected_codes,
                 n_stage_seq_selected_codes]
            )

    print(f"CSV file '{pattern_file_path}' has been created successfully.")


def get_code_stats(input_csv_file, output_csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv_file, delimiter=';')

    # Extract the 'annotation_sequence' column
    annotation_sequence = df['code_seq_with_all_codes']

    # Create a dictionary to store the unique annotations and their counts
    code_counts = Counter()

    # Iterate over the rows and update the dictionary
    for i in range(len(df)):
        unique_codes = annotation_sequence[i].split(',')
        code_counts.update(unique_codes)

    # Create lists to store the unique annotations, counts, and number of issues
    unique_codes = []
    total_codes = []
    total_issues = []

    # Iterate over the dictionary and populate the lists
    for code, count in code_counts.items():
        unique_codes.append(code)
        total_codes.append(count)
        total_issues.append(len(df[df['code_seq_with_all_codes'].str.contains(code)]))

    # Create a DataFrame with the unique annotations, counts, and number of issues
    unique_codes_df = pd.DataFrame({'Codes': unique_codes,
                                    'Total # of codes': total_codes,
                                    'Total # of issues': total_issues})

    # Sort the DataFrame by the unique annotations
    unique_codes_df = unique_codes_df.sort_values('Codes')

    # Write the DataFrame to a new CSV file
    unique_codes_df.to_csv(output_csv_file, index=False, sep=';')

    print(f"CSV file '{output_csv_file}' with unique annotations has been created successfully.")


if __name__ == '__main__':
    annotation_data_path = '../data/annotation_data.json'
    stage_seq_file_path = './stages.csv'
    # annotation_stats_file_path = '../dataset/annotation_data/annotation_codes_stat.csv'

    derive_stage_sequence(annotation_data_path, stage_seq_file_path)
    # get_annotation_codes_stats(patterns_file_path, annotation_stats_file_path)
