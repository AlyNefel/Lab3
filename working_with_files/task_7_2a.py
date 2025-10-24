from sys import argv

ignore = ["duplex", "alias", "Current configuration"]
filename = argv[1]

with open(filename) as f:
    for line in f:
        line = line.strip()
        if not line.startswith('!') and line:
            if not any(word in line for word in ignore):
                print(line)
