with open('input.txt', 'r') as file:
    read = file.readlines()

new_version = []

for line in read:
    for word in line.split(" "):
        new_version.append(word[::-1])


new_version = " ".join(new_version)

with open('input.txt', 'w') as file:
     file.write(new_version)
