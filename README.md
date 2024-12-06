# resume-classifier
Resume Classifier - Automatic Resume Classification with Enhanced Text Processing
This Python script automates resume classification by extracting text from PDFs and organizing it into categories like education, experience, skills, and projects. 

Key features include:
- Cleaning and de-duplication of text.
- Chronological date normalization for timelines.
- Context-aware section extraction using headers and keywords.
- Named Entity Recognition (NER) for dates, organizations, and locations.
- Regex-based pattern matching for structured data extraction.
- Fuzzy matching to map content back to its original PDF context.
The output is a clean, categorized CSV, ideal for analysis or recruitment workflows.


## Installation:

### Install Required Libraries:

Download all modules required for this program using the following command:

``pip install spacy pandas pymupdf rapidfuzz scikit-learn python-dateutil``

Download a pre-trained spaCy model, such as en_core_web_sm, from the official website. You can download it using the following command:

``python -m spacy download en_core_web_sm``

### Usage:

**Prepare Folder of Resumes:** Create a folder containing resumes in PDF format.

**Modify File Paths:** Update the folder_path and output_csv_path variables in the main script to point to your input and desired output file paths.

**Run the Script:** Execute the Python script.


## How it Works:

**Loads spaCy Model:** Loads a pre-trained spaCy model to process text.

**Defines Categories:** Defines a dictionary of categories with corresponding keywords.

**Cleans Input Text:** Removes noise such as symbols, redundant entries, and common resume filler words to ensure clean, structured input for processing.

**Date Parsing and Formatting:** Recognizes multiple date formats (e.g., "Jan 2023") and normalizes them using dateutil.parser for chronological consistency.

**Extracts Text by Category:** For each category, extracts text using a combination of spaCy's NER and regular expressions.

**NER-based Extraction:** Identifies named entities like organizations, locations, and dates.

**Regex-based Extraction:** Matches specific keywords and patterns.

**Uses Contextual Sections:** Matches section headers using predefined regex patterns to ensure extracted content corresponds to the intended category (e.g., "Work Experience").

**Enhanced Project and Experience Extraction:** Uses refined regular expressions to capture more detailed information.

**Fuzzy Matching to Original PDF Text:** A context window (start and end) is used to locate and retrieve the exact section from the original PDF for preservation of order and validation.

**Classifies Resumes:** Iterates through each resume in the input CSV, classifies it into categories, and stores the results.

**Writes Output:** Writes the classified data to a new CSV file.


## Customization:

**Categories:** Modify the CATEGORIES dictionary to add or remove categories and adjust keywords.

**Regex Adjustments:** Modify patterns in SECTION_HEADERS or FORMAT_PATTERNS for domain-specific needs.

**Threshold Tuning:** Adjust fuzzy matching thresholds in functions like fuzzy_keyword_match for stricter or looser matches.

**Output Format:** Adjust the output CSV format to suit your specific needs.


### Notes:

- The accuracy of the classification depends on the quality of the resumes and the effectiveness of the keyword-based approach.
- For more complex scenarios, consider exploring advanced techniques like machine learning-based text classification.
- For better performance on large datasets, consider optimizing the script by using parallel processing or more efficient text processing techniques.
