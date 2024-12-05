# resume-classifier
Resume Classifier - Automatic Resume Classification with Enhanced Text Processing
This Python script leverages spaCy's natural language processing capabilities to automatically classify key information from resumes. It extracts text relevant to specific categories such as education, experience, skills, projects, achievements, certifications, publications, and volunteering.


## Installation:

### Install Required Libraries:

Download spaCy and pandas modules using the following command:

``pip install spacy pandas``

Download a pre-trained spaCy model, such as en_core_web_sm, from the official website. You can download it using the following command:

``python -m spacy download en_core_web_sm``

### Usage:

**Prepare Input CSV:** Create a CSV file with a column named "Resume_str" containing the text of each resume.

**Modify File Paths:** Update the input_csv_path and output_csv_path variables in the main script to point to your input and desired output file paths.

**Run the Script:** Execute the Python script.


## How it Works:

**Loads spaCy Model:** Loads a pre-trained spaCy model to process text.

**Defines Categories:** Defines a dictionary of categories with corresponding keywords.

**Extracts Text by Category:** For each category, extracts text using a combination of spaCy's NER and regular expressions.

**NER-based Extraction:** Identifies named entities like organizations, locations, and dates.

**Regex-based Extraction:** Matches specific keywords and patterns.

**Enhanced Project and Experience Extraction:** Uses refined regular expressions to capture more detailed information.

**Classifies Resumes:** Iterates through each resume in the input CSV, classifies it into categories, and stores the results.

**Writes Output:** Writes the classified data to a new CSV file.


## Customization:

**Categories:** Modify the CATEGORIES dictionary to add or remove categories and adjust keywords.

**Text Extraction:** Customize the regular expressions in the extract_text_by_category function to refine the extraction process.

**Output Format:** Adjust the output CSV format to suit your specific needs.


### Note:

- The accuracy of the classification depends on the quality of the resumes and the effectiveness of the keyword-based approach.
- For more complex scenarios, consider exploring advanced techniques like machine learning-based text classification.
- For better performance on large datasets, consider optimizing the script by using parallel processing or more efficient text processing techniques.
- By following these steps and customizing the script as needed, you can effectively automate the classification of resumes and extract valuable insights from large volumes of text data.
