import json
import os

# Define the directory relative to the script location
script_dir = os.path.dirname(os.path.realpath(__file__))  # Gets the directory where the script/executable is located
input_dir = os.path.join(script_dir, 'input')  # Input folder
output_dir = os.path.join(script_dir, 'output')  # Output folder

# Check if the output directory exists, if not, create it
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
    print("Input directory is empty. Please add some JSON files to process.")
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
                print(f"Error: '{filename}' is not a valid JSON file and was skipped.")
            except Exception as e:
                print(f"An error occurred with '{filename}': {e}")
    
    print("JSON files have been reformatted and saved to", output_dir)
