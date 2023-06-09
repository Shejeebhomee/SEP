import re
import spacy

# Load the small English language model
nlp = spacy.load("en_core_web_sm")

# Define a function to redact names from a text document
def redact_names_address_date(text):
    # Create a new doc object from the text
    doc = nlp(text)

    # Iterate over the entities in the doc object
    for ent in doc.ents:
        # If the entity is a person name, replace it with [REDACTED]
        if ent.label_ == "PERSON" or ent.label_ == "DATE" or  ent.label_ == "GPE":
            text = text.replace(ent.text, "[REDACTED]")

    return text

def redact_info(file_path):
    # Read file contents
    with open(file_path, 'r') as file:
        content = file.read()
        redacted_content=redact_names_address_date(content)

    # Write redacted content to a new file
    with open('redacted_' + file_path, 'w') as redacted_file:
        redacted_file.write(redacted_content)

    print('Redacted file saved as redacted_' + file_path)

# Example usage
redact_info('data.txt')
