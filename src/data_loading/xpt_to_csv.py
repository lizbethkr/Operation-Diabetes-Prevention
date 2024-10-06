import pandas as pd
import os 
import xport

print("Current working directory:", os.getcwd())

xpt_dir = os.path.abspath('data/raw/xpt_files/')
csv_dir = os.path.abspath('data/raw/csv_files/')

if not os.path.exists(csv_dir):
    os.makedirs(csv_dir)


def convert_xpt_to_csv(xpt_file, output_directory):
    # Extract the file name without the extension
    file_name = os.path.splitext(os.path.basename(xpt_file))[0]
    
    with open(xpt_file, 'rb') as file:
        df = xport.to_dataframe(file)
    
    csv_file = os.path.join(output_directory, file_name + '.csv')
    df.to_csv(csv_file, index=False)
    print(f"Converted {xpt_file} to {csv_file}")

for file_name in os.listdir(xpt_dir):
    if file_name.endswith(".XPT") or file_name.endswith(".xpt"):
        # Full path to the .XPT file
        xpt_file_path = os.path.join(xpt_dir, file_name)
        print(f"Processing file: {xpt_file_path}")

        # Convert the .XPT file to .CSV
        try:
            convert_xpt_to_csv(xpt_file_path, csv_dir)
        except Exception as e:
            print(f"Error processing {xpt_file_path}: {e}")

print("Conversion completed!")