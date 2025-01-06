import re

def extract_contacts_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            
        # Patterns for phone numbers and emails
        phone_pattern = r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b'
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # Find all matches
        phones = re.findall(phone_pattern, text)
        emails = re.findall(email_pattern, text)
        
        return phones, emails
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return [], []
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], []

def save_contacts_to_file(phones, emails, output_file):
    try:
        with open(output_file, 'w') as file:
            # Write header
            file.write(f"{'Phone Numbers':<20}{'Emails':<30}\n")
            file.write(f"{'-'*20:<20}{'-'*30:<30}\n")
            
            # Get the maximum number of rows
            max_length = max(len(phones), len(emails))
            
            # Write data in columns
            for i in range(max_length):
                phone = phones[i] if i < len(phones) else ''
                email = emails[i] if i < len(emails) else ''
                file.write(f"{phone:<20}{email:<30}\n")
        
        print(f"Contacts saved to '{output_file}' successfully!")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# File paths
input_file = 'contact.txt'  # Replace with your input file path
output_file = 'extracted_contact.txt'  # File where the output will be saved

# Extract contacts and save them
phones, emails = extract_contacts_from_file(input_file)
save_contacts_to_file(phones, emails, output_file)


'''
1. The first thing I did before starting to write the code for this project is I open up Chat GPT and ask in providing me a python scripts
on how to write a scripts to a scripts in extracting phone number and email.
2. Using the Chat GPT result, I copy and pasted code.
3. Also, I ask Chat GPT to create an out list columns for the phone numbers and emails. Lastly, I ask Chat GPT to save the result in a text file.
4. It was a successful request. I have created a project in less than 30 minutes.
'''


