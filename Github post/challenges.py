# Let's assume the file 'challenges.json' exists and contains the user's data.
import json
# Function to read and parse the 'challenges.json' file
file_path = 'db/challenges.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Print the data in a readable format
# Let's write the parsed JSON data to a text file

output_file_path = 'challenges_output.txt'

with open(output_file_path, 'w') as output_file:
    for result in data["results"]:
        output_file.write(f"ID: {result['id']}\n")
        output_file.write(f"Name: {result['name']}\n")
        output_file.write(f"Description: {result['description']}\n")
        output_file.write(f"Max Attempts: {result['max_attempts']}\n")
        output_file.write(f"Value: {result['value']}\n")
        output_file.write(f"Category: {result['category']}\n")
        output_file.write(f"Type: {result['type']}\n")
        output_file.write(f"State: {result['state']}\n")
        output_file.write(f"Requirements: {result['requirements']}\n")
        output_file.write(f"Connection Info: {result['connection_info']}\n")
        output_file.write(f"Next ID: {result['next_id']}\n")
        output_file.write(f"Attribution: {result['attribution']}\n\n")

output_file_path
