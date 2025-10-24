with open('ospf.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines

        # Remove unwanted characters and split
        fields = line.replace(',', '').replace('[', '').replace(']', '').split()

        # Defensive check: only process lines with at least 6 fields
        if len(fields) >= 6:
            print(f"Prefix              {fields[0]}")
            print(f"AD/Metric           {fields[1]}")
            print(f"Next-Hop            {fields[3]}")
            print(f"Last update         {fields[4]}")
            print(f"Outbound Interface  {fields[5]}")
            print()
        else:
            print(f"⚠️ Skipped malformed line: {line}")
