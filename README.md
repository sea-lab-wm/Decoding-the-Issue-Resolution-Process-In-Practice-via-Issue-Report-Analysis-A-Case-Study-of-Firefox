# Paper Title
**Decoding the Issue Resolution Process In Practice via Issue Report Analysis: A Case Study of Firefox**

Link to the paper: https://antu-saha.github.io/assets/pdf/papers/icse-2025.pdf

# Purpose
This artifact complements the research paper by offering a manually curated dataset of coded issue reports of Mozilla products, i.e., Core and Firefox. The dataset contains the manually assigned topics (a.k.a, codes) to the developers’ discussion in the issue reports. The topics are categorized into the issue resolution activities (i.e., stages) performed to resolve the issue which facilitates the derivation of the issue resolution process and patterns of the Mozilla project. This artifact enables the reproducibility and verifiability of our results and findings presented in the paper. Moreover, it promotes further research into understanding the issue resolution process of Mozilla as well as other software projects.

# Overview
In this study, we aim to understand the issue resolution process implemented in practice by analyzing the issue reports of Mozilla Firefox. We qualitatively and quantitatively analyzed the discussions found in 356 Firefox issue reports, identified the overall resolution process at Firefox, and derived a catalog of 47 patterns representing instances of the process. We carried out a user study involving Mozilla developers to understand the usefulness of the derived patterns. We conducted a small-scale study on issue reports of Chromium and GnuCash projects to understand the generalizability of the findings of the study.

This artifact includes all the essential materials required to replicate the study's findings and to facilitate similar research on other projects. The provided scripts and programs can be used to replicate the quantitative results and generate figures and plots. As the qualitative results require manual investigation, we provided all the detailed results in the artifact. In summary, this artifact contains:
1. Detailed procedure and guidelines for annotating issue reports
2. Annotation catalog including annotation codes and identified stages with their description, frequency, rules to apply them, and real examples
3. Annotated data of 356 Mozilla issue reports with all the necessary statistics
4. Derived stage sequences and patterns with necessary statistics
5. Details of the result analysis presented in the paper to answer RQs
6. Procedure and results of the user study, i.e., interview involving Mozilla developers
7. Procedure and results of the generalizability study including Chromium and GnuCash issue reports

# Provenance
The artifact is publicly available at: https://doi.org/10.5281/zenodo.14727541

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14727542.svg)](https://doi.org/10.5281/zenodo.14727542)

The paper’s preprint is publicly available at: https://antu-saha.github.io/assets/pdf/papers/icse-2025.pdf

# Directory Structure
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

# Data
In this study, we qualitatively analyzed the developers’ discussion in the issue reports and assigned the issue report comments specific codes (i.e., topics discussed in the comment). We provide the annotated issue report data in JSON format where “quote” represents the issue report comments and “code” represents the assigned code (i.e., topic) to that comment. The assigned annotation codes were used to identify the issue resolution stages. Finally, utilizing the stages, we identified the overall Mozilla issue resolution process and derived 47 issue resolution patterns.

The annotation data is available at: https://github.com/sea-lab-wm/Decoding-the-Issue-Resolution-Process-of-Mozilla/blob/main/b_annotation_data/annotation_data.json

# Setup
No special setup is required to use the artifact. Most of the materials are provided in PDF, XLSX, or JSON format which can be opened using respective software (i.e., PDF reader, Microsoft Excel, and JSON reader). 

Additionally, we provided simple Python scripts to derive results and automate result analysis. The scripts can be executed (not mandatory) on any machine (e.g., Windows, Linux, or Mac) with Python 3 or above.

# How to run the scripts?
1. Install required Python packages from `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```
2. Run the following scripts sequentially:
* ```c_stages_and_patterns_derivation/derive_stage_sequence.py```
* ```c_stages_and_patterns_derivation/analyze_stage_sequences.py```
* ```d_results_analysis/get_statistics.py```
* ```d_results_analysis/mannwhitneyu_test.py```

# Usage
This artifact can be used in two ways: (1) to replicate the results of this study, and (2) to conduct similar research on a different software project. To replicate the results of the study or reuse the artifact to identify the issue resolution patterns of other projects using this artifact, one has to perform the following steps:
1. **Issue Discussion Annotation:** The first step is to investigate and annotate the developers’ discussion in the issue reports. The detailed guidelines are found at a_issue_annotation/issue_discussion_annotation_details.pdf. This step comprises the following sub-steps:
   * *Project Selection:* Select the project to investigate the issue report discussion and identify the issue resolution patterns. In our study, we selected three projects, i.e., Mozilla (Core and Firefox), Chromium, and GnuCash.
   * *Issue Report Collection:* Collect a statistically significant sample of FIXED and RESOLVED issue reports to investigate the developers’ discussion.
   * *Issue Annotation:* Annotate the issue reports by following the guidelines (a_issue_annotation/issue_annotation_guidelines.pdf) and using the issue annotation catalog (a_issue_annotation/issue_annotation.xlsx/annotation_codes).
   * *Annotation Data Collection:* Collect the annotation data in some format (e.g., JSON or CSV). Our annotation data is found at b_annotation_data/annotation_data.json.
2. **Stage and Patterns Derivation:** Once the issue reports are annotated, the next step is to derive stages and patterns. This step includes the following sub-steps:
   * *Stage Sequence Derivation:* To derive stage sequence which represents the issue resolution activities sequentially, we need to map the annotation codes to the resolution stages using c_stages_and_patterns_derivation/stage_derivation.xlsx. To automatically perform this step, use the Python script: c_stages_and_patterns_derivation/derive_stage_sequence.py. The input to this script is the annotation data in JSON format and the output is the derived stages in CSV format. Stage sequences for our data is found at: c_stages_and_patterns_derivation/stages.csv.
   * *Pattern Derivation:* Using the stage sequences, derive the issue resolution patterns for each issue report using the methodology discussed in the paper (Section III.E). For our case, the pattern derivation is showed in c_stages_and_patterns_derivation/pattern_derivation.xlsx.
3. **Result Analysis:** The next step is to analyze the stages and patterns to draw conclusions about the issue resolution stages, process, and patterns. Use the Python scripts, i.e., d_results_analysis/get_statistics.py and d_results_analysis/mannwhitneyu_test.py to automate the result analysis process. Our result analysis are detailed in three XLSX files: d_results_analysis/RQ_1_stage_analysis.xlsx, d_results_analysis/RQ_2_3_issue_resolution_process.xlsx, and d_results_analysis/RQ_4_pattern_analysis.xlsx.
4. **User Study:** To conduct the user study (i.e., interview) involving developers to understand the usefulness of the identified patterns, use the methodology discussed in e_interview/interview_methodology_and_results.pdf.

# Contact Information
[**Antu Saha**](https://antu-saha.github.io/), PhD Candidate

William & Mary

Virginia, USA

asaha02@wm.edu
