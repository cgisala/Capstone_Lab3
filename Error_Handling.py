#This line errors if data.txt does not exist.
data = open('data.txt', 'r').readlines()

for line in data:
    print(line)