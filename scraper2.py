from googlesearch import search

query = "studytonight"

for i in search(query, num=10, stop=10, pause=2):
    print(i)