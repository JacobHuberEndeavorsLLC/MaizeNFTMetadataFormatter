import json
import os
import sys

# The application's directory when running the executable
if getattr(sys, 'frozen', False):
    application_dir = os.path.dirname(sys.executable)
else:
    # The directory of the script file if not running as an executable
    application_dir = os.path.dirname(os.path.abspath(__file__))

# Define the input and output directories
input_dir = os.path.join(application_dir, 'input')
output_dir = os.path.join(application_dir, 'output')

# Ensure input and output directories exist
if not os.path.exists(input_dir) or not os.listdir(input_dir):
    sys.exit("\n--\nInput directory is empty or does not exist. Please add some JSON files to process.\n--")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to reformat the JSON data
def reformat_json_data(original_data):
    reformatted_data = {
        "image": "ipfs://ANIMATION_PLACEHOLDER",
        "animation_url": "ipfs://ANIMATION_PLACEHOLDER",
        "name": original_data.get("name", ""),
        "royalty_percentage": 10,
        "description": original_data.get("description", ""),
        "collection_metadata": "https://nftinfos.loopring.io/COLLECTION_PLACEHOLDER",
        "mint_channel": "Maize",
        "properties": {item["trait_type"]: item["value"] for item in original_data.get("attributes", [])},
        "attributes": original_data.get("attributes", [])
    }
    return reformatted_data

# Check if the input directory is empty
if not os.listdir(input_dir):
    print("\n--\nInput directory is empty. Please add some JSON files to process.\n--")
else:
    # Process files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(input_dir, filename)
            try:
                with open(file_path, 'r') as file:
                    original_data = json.load(file)
                
                reformatted_data = reformat_json_data(original_data)
                
                output_file_path = os.path.join(output_dir, filename)
                with open(output_file_path, 'w') as file:
                    json.dump(reformatted_data, file, indent=4)
                    
            except json.JSONDecodeError:
                print(f"\n--\nError: '{filename}' is not a valid JSON file and was skipped.\n--")
            except Exception as e:
                print(f"\n--\nAn error occurred with '{filename}': {e}\n--")
    
    print(f"\n--\nJSON files have been reformatted and saved to", output_dir, "\n--")
