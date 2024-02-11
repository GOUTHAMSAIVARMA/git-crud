# pip install streamlit spacy
# import streamlit as st
# import spacy

# # Load English NLP model
# nlp = spacy.load("en_core_web_sm")

# def extract_fields(resume_text):
#     # Process the resume text using SpaCy
#     doc = nlp(resume_text)

#     # Define the required fields
#     required_fields = ["name", "email", "phone", "experience", "education", "skills"]

#     # Extract information based on the required fields
#     extracted_data = {field: [] for field in required_fields}

#     for ent in doc.ents:
#         for field in required_fields:
#             if field in ent.text.lower():
#                 extracted_data[field].append(ent.text)

#     return extracted_data

# def main():
#     st.title("Resume Field Extractor")

#     # Upload a resume file
#     uploaded_file = st.file_uploader("Upload a resume (PDF or text)", type=["pdf", "txt"])

#     if uploaded_file is not None:
#         resume_text = uploaded_file.read()

#         # Display the uploaded resume text
#         st.subheader("Uploaded Resume:")
#         st.text(resume_text)

#         # Extract fields
#         extracted_data = extract_fields(resume_text)

#         # Display the extracted fields
#         st.subheader("Extracted Fields:")
#         for field, values in extracted_data.items():
#             st.write(f"{field.capitalize()}: {', '.join(values)}" if values else f"{field.capitalize()}: Not found")

# if __name__ == "__main__":
#     main()
print("hello")
