import urllib.request

file_name = "python_links.txt"
file = open(file_name)
in_file = file.read()
List = in_file.split("\n")

Video = 1
Zip = 1
for url in List:
    if "mp4" in url:
        urllib.request.urlretrieve(url, str(Video)+'.mp4')
        Video += 1
    elif "zip" in url:
        urllib.request.urlretrieve(url, str(Zip)+'.zip')
        Zip += 1
# Video = 140
# Zip = 1
# length = len(List)
# for url in range (Video+Zip-2, length+1):
#     if "mp4" in List[url]:
#         urllib.request.urlretrieve(List[url], str(Video)+'.mp4')
#         Video += 1
#     elif "zip" in List[url]:
#         urllib.request.urlretrieve(List[url], str(Zip)+'.zip')
#         Zip += 1
