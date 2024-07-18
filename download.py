import urllib.request

file_name = "inp.txt"
file = open(file_name)
in_file = file.read()
List = in_file.split("\n")

Video = 1
Zip = 1
length = len(List)
for url in List:
    if "mp4" in url:
        urllib.request.urlretrieve(url, str(Video)+'.mp4')
        Video += 1
    if "zip" in url:
        urllib.request.urlretrieve(url, str(Zip)+'.zip')
        Zip += 1
