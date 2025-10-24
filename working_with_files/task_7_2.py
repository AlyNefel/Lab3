from sys import argv

filename = argv[1]

with open(filename) as f:
    for line in f:
        line = line.strip()
        if not line.startswith('!') and line:
            print(line)
