import zipfile
import os

# List of files to include in the zip
files_to_zip = []
root = "C:\\Users\\acer\\Desktop\\booom"
entries = os.listdir(root)
for entry in entries:
  if (entry.endswith("pdf")):
      files_to_zip.append(root + '\\' + entry)

# Name of the output zip file
output_zip = 'final.zip'

# Create a zip file
with zipfile.ZipFile(output_zip, 'w') as zipf:
    for file in files_to_zip:
        if os.path.exists(file):
            zipf.write(file, os.path.basename(file))
        else:
            print(f"File {file} does not exist and will be skipped.")

print(f"Created {output_zip} successfully.")
