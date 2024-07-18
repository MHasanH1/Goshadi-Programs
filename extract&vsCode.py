import os
import zipfile
import patoolib

projectFolder = "hasan"

os.chdir("C:\\Users\\acer\\Downloads\\Compressed")
os.mkdir(projectFolder)

filePath = "C:\\Users\\acer\\Downloads\\Compressed\\exercies_file_vue3_part_12.rar"
outputPath = "C:\\Users\\acer\\Downloads\\Compressed\\" + projectFolder

try:
    patoolib.extract_archive(filePath, outdir = outputPath)
except:
    with zipfile.ZipFile(filePath, 'r') as zip_ref:
        zip_ref.extractall(outputPath)

os.chdir(projectFolder)
os.system("code .")
