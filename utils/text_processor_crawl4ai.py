import re
import json


def clean_content(content: str) -> str:
    # Remove reference numbers and links
    content = re.sub(r'\[\d+\]', '', content)

    # Format whitespace
    content = re.sub(r'\s+', ' ', content)

    # Remove backslash
    content = re.sub(r'\\', '', content)

    # Remove html tags
    content = re.sub(r'<[^>]*>', '', content)

    # Remove newlines
    content = re.sub(r'\n', '', content)

    # Remove whitespace at the beginning and end of the string
    content = content.strip()
    return content


def extract_markdown_content(markdown_text):
    pattern = r'^(#{1,4})\s+(.+?)\n((?:(?!^#{1,4}\s+).|\n)*)'
    matches = re.finditer(pattern, markdown_text, re.MULTILINE)  # prevent overstacking

    extracted_content = {}

    for match in matches:
        title = match.group(2).strip()
        content = match.group(3).strip()

        if title and content:
            extracted_content[clean_content(title)] = clean_content(content)

    return extracted_content


def extract_abstract_discussion_conclusion(markdown_text: str) -> dict:
    """
    Extract abstract, discussion, and conclusion from the extracted content
    """

    extracted_content = extract_markdown_content(markdown_text)
    extracted_value_content = {
        "abstract": "",
        "discussion": "",
        "conclusion": ""
    }

    # iterate through extracted_content
    for key, value in extracted_content.items():

        # if key contains abstract, pull out
        if any(word in key.lower() for word in ['abstract']):
            extracted_value_content['abstract'] = f"{value}"

        # if key contains discussion, pull out
        if any(word in key.lower() for word in ['discussion']):
            extracted_value_content['discussion'] = f"{value}"

        # if key contains conclusion, pull out
        if any(word in key.lower() for word in ['conclusion']):
            extracted_value_content['conclusion'] = f"{value}"

    return extracted_value_content
