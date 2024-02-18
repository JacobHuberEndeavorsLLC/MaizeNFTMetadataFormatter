import json
import os

# Define the directory containing the JSON files
json_dir = '/Users/cobmin/downloads/80/alienanimaljson'  # Update this path based on your pwd output
output_dir = '/Users/cobmin/downloads/80/reformatted_json'  # New directory for reformatted files

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

# Loop through all files in the directory
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        
        # Read the original JSON data
        with open(file_path, 'r') as file:
            original_data = json.load(file)
        
        # Reformat the data
        reformatted_data = reformat_json_data(original_data)
        
        # Write the reformatted data to the new file in output directory
        output_file_path = os.path.join(output_dir, filename)
        with open(output_file_path, 'w') as file:
            json.dump(reformatted_data, file, indent=4)

print("JSON files have been reformatted and saved to", output_dir)
