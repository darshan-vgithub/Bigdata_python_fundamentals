with open("file_content.txt", "w") as f:
    content = f.write("Hi I am Darshan I am studying in University of Strathclyde")
    f.close()


with open("file_content.txt", "r") as f:
    content = f.read()
    print(content)