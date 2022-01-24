file = open('input.txt', 'r')
read = file.readlines()
file.close()

new_version = []

for line in read:
    for word in line.split(" "):
        new_version.append(word[::-1])


new_version = " ".join(new_version)

file = open('input.txt', 'w')
file.write(new_version)
file.close()
