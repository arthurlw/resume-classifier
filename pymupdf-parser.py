import spacy
import pandas as pd
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define categories to extract
CATEGORIES = {
    "Education": ["degree", "university", "college", "school"],
    "Experience": ["experience", "work", "job", "company", "role", "position", "internship", "employment", "tenure", "career", "responsibilities", "contributions"],
    "Projects": ["projects", "case study", "portfolio", "implementation", "demonstrated", "initiative", "proof of concept", "prototype", "hackathon", "research", "developed", "built", "designed"],
    "Skills": ["skills", "technologies", "tools", "framework", "languages", "expertise", "proficiencies", "competencies", "aptitude", "specialization"],
    "Achievements": ["award", "achievement", "honor"],
    "Certifications": ["certification", "license", "qualification"],
    "Publications": ["publication", "article", "journal", "research", "thesis"],
    "Volunteering": ["volunteer", "charity", "nonprofit", "community", "fundraising", "social impact", "ngo", "service"],
}

# Helper functions
def extract_text_by_category(text, category_keywords):
    """
    Extracts text matching a category using spaCy's NER and regex patterns.
    This function is enhanced to extract detailed project descriptions.
    """
    doc = nlp(text)
    extracted = []
    
    # Check entities for matching keywords
    for ent in doc.ents:
        if any(keyword in ent.label_.lower() or keyword in ent.text.lower() for keyword in category_keywords):
            extracted.append(ent.text)
    
    # Add regex-based keyword matching for additional extraction
    regex = "|".join(category_keywords)
    matches = re.findall(rf"\b(?:{regex})\b", text, re.IGNORECASE)
    extracted.extend(matches)
    
    # For projects, extract entire paragraphs containing project-related keywords
    if "projects" in category_keywords:
        project_pattern = r"([^.]*\b(?:projects|case study|portfolio|implementation|initiative|prototype|hackathon|research|developed|built|designed)\b[^.]*\.)"
        project_matches = re.findall(project_pattern, text, re.IGNORECASE)
        extracted.extend(project_matches)
    
    if "experience" in category_keywords:
        experience_pattern = r"([^.]*\b(?:experience|role|responsibility|job|worked|managed|led)\b[^.]*\.)"
        experience_matches = re.findall(experience_pattern, text, re.IGNORECASE)
        extracted.extend(experience_matches)
    
    return "\n".join(set(extracted))

def classify_resume(resume_text):
    """
    Classifies a single resume text into categories.
    """
    classified_data = {}
    for category, keywords in CATEGORIES.items():
        classified_data[category] = extract_text_by_category(resume_text, keywords)
    return classified_data

# Process resumes from CSV
def process_resumes(input_csv, output_csv):
    """
    Reads resumes from a CSV file, classifies them, and writes the results to a new CSV.
    """
    # Load data
    df = pd.read_csv(input_csv)
    print(df.columns)
    if "Resume_str" not in df.columns:
        raise ValueError("Input CSV must contain a 'Resume_str' column.")

    # Classify each resume
    results = []
    total_resumes = len(df)
    for idx, row in df.iterrows():
        resume_text = row["Resume_str"]
        classified = classify_resume(resume_text)
        results.append(classified)
        
        # Print progress to terminal
        print(f"Processing resume {idx + 1}/{total_resumes}")

    # Create output DataFrame
    output_df = pd.DataFrame(results)
    output_df.to_csv(output_csv, index=False)
    print(f"Processed {total_resumes} resumes. Results saved to {output_csv}")

# Main script
if __name__ == "__main__":
    input_csv_path = "/Users/user/Documents/Coding/ResumAI/Resume copy - Resume copy.csv.csv"  # Replace with the input file path
    output_csv_path = "classified_resumes.csv"  # Replace with the output file path
    process_resumes(input_csv_path, output_csv_path)
