import json
import random
from datetime import datetime, timedelta
import time

# Load the metadata.json file
metadata_file_path = '/data/metadata.json'
with open(metadata_file_path, 'r') as file:
    metadata = json.load(file)

# Extract the PIDs from the metadata
pids = []
for plugin in metadata['plugins']:
    pids.extend(plugin['pids'])

# Function to generate random wattage
def generate_random_wattage():
    return round(random.uniform(0.0, 10.0), 1)

# Generate timestamps for the entries - every 1 second for 1 minute
start_time = datetime.strptime(metadata['start_time'], "%m/%d/%Y %I:%M:%S %p")

# Create the data structure incrementally
data = []
output_file_path = '/data/cpu.json'  # Use the volume path
for i in range(5):  # Generate 60 timestamps, 1 second apart
    timestamp = start_time + timedelta(seconds=i)
    timestamp_str = timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
    entries = [[generate_random_wattage(), str(pid)] for pid in pids]

    # Print the generated data
    print("Writing:", entries)

    data.append({timestamp_str: entries})

    # Save the data to cpu.json incrementally
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

    time.sleep(1)  # Wait for 1 second before generating the next entry
