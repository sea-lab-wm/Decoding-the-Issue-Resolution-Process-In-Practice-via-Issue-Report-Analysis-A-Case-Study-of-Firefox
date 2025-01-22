This is an anonymous replication package for the paper "Decoding the Issue Resolution Process In Practice via Issue Report Analysis: A Case Study of Firefox"

This package contains the following files/folders:
1. `README.md`: this file
2. `a_issue_annotation`: a folder containing the necessary guidelines and spreadsheet for issue annotation
    * `issue_discussion_annotation_details`: the details of the issue discussion annotation task. This file includes the methodology of the annotation procedure, disambiguation techniques, strategies adopted for mitigating potential biases, and inter-coder reliability assessment details.
    * `issue_annotation_guidelines.pdf`: the procedure and guidelines for issue annotation. These guidelines were used by all the annotators for the issue annotation task.
    * `issue_annotation.xlsx`: the spreadsheet used for issue annotation. This spreadsheet contains three sheets:
      * `issues`: contains the list of issues that were annotated. This sheet was used to keep track of the issues during the annotation process.
      * `annotation_codes`: this sheet is the annotation code catalog. It is used to record the annotation codes with their definition, rules, and examples during the annotation process.
      * `problem_categories`: this sheet is the problem category catalog. It is used to record the problem categories with their definition and examples during the annotation process.
3. `b_annotation_data`: a folder containing the annotated data of all issues with the necessary statistics
    * `annotation_data.json`: this file contains the annotated data for all 356 issues in JSON format. Here, `quote` is the annotated text snippet from the issue report and `code` is the assigned code.
    * `annotation_code_and_stage_stats.xlsx`: this spreadsheet contains the necessary sheets for demonstrating the annotation code & stage statistics, and issue comment statistics.
4. `c_stage_and_pattern_derivation`: a folder containing the necessary scripts and spreadsheet to derive stages and patterns for all issues
    * `stage_derivation.xlsx`: this spreadsheet contains the derived six stages with the respective codes.
    * `pattern_derivation.xlsx`: this spreadsheet contains the required sheets for deriving patterns from the stage sequences for all issues.
      * `derive_pattern`: this sheet shows the steps to derive patterns from the stage sequences.
      * `complexity`: this sheet shows the complexity of the patterns.
      * `final_patterns`: this sheet contains the derived patterns for all issues.
    * `derive_stage_sequence.py`: this script is used to derive stage sequences from the annotation data for all issues.
    * `analyze_stage_sequences.py`: this script is used to analyze the stage sequences to draw conclusions for the RQs.
5. `d_result_analysis`: a folder containing the necessary scripts and spreadsheets to analyze the stages and patterns
   * `RQ_1_stage_analysis.xlsx`: this spreadsheet contains the necessary sheets for analyzing the derived six stages to answer RQ1.
   * `RQ_2_3_issue_resolution_process.xlsx`: this spreadsheet contains the necessary sheets for analyzing the bi-grams and tri-grams of the stage sequences to derive the issue resolution process of Mozilla Firefox to answer RQ2 and RQ3.
   * `RQ_4_pattern_analysis.xlsx`: this spreadsheet contains the necessary sheets for analyzing the derived patterns to answer RQ4.
   * `overall_process.pdf`: this file contains the overall issue resolution process of Mozilla Firefox derived from the stage sequences.
   * `get_statistics.py`: this script is used to get statistics and figures to answer the RQs.
   * `mannwhitneyu_test.py`: this script is used to perform the Mann-Whitney U test to answer RQs.
6. `e_interview`: this folder contains all the necessary materials to conduct the user-study, i,e., online interviews. This folder includes interview methodology, protocol, and the slides used for conducting the interviews. It also contains a sub-folder, i.e., `interview_transcripts` that includes the anonymized interview transcripts and the responses to the questions for each participant.
7. `generalizability_study`: this folder contains necessary materials for the generalizability study. It includes the methodology of the generalizability study and the coded issues with derived patterns for Chromium and GnuCash projects.
8. `additional_discussion.pdf`: this file contains the additional discussion and implications of the findings that we presented in the paper.


   

