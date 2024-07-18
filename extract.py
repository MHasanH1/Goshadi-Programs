import os

path = 'D:\Programming\Toturial\WordPress'
destination_path = 'D:\Programming\Toturial\WordPress'
folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

for folder in folders:
    folder = "\\" + folder
    # path += folder
    os.chdir(path + folder)
    mp4_files = [f for f in os.listdir(path + folder) if f.endswith('.mp4')]
    for mp4_file in mp4_files:
        mp4_file = "\\" + mp4_file
        source_path = path + folder + mp4_file
        os.system(f"move {source_path} {destination_path}")        
    # path = 'D:\Programming\Toturial\WordPress'

# def is_empty_folder(path):
#     return len(os.listdir(path)) == 0

# path = 'D:\Programming\Toturial\WordPress'
# folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

# for folder in folders:
#     folder = '\\' + folder
#     if is_empty_folder(path + folder):
#         print("The folder is empty")
#     else:
#         print("The folder is not empty")
