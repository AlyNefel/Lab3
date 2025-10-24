from sys import argv

# Define the ignore list
ignore = ["duplex", "alias", "Current configuration"]

# Get source and destination filenames from command-line arguments
src_file = argv[1]
dest_file = argv[2]

# Open source for reading and destination for writing
with open(src_file) as src, open(dest_file, 'w') as dest:
    for line in src:
        line = line.strip()
        if not line or line.startswith('!'):
            continue
        if not any(word in line for word in ignore):
            dest.write(line + '\n')
