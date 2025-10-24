ip = input("Enter IP address (e.g. 10.0.1.1): ")
octets = ip.split('.')

if ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    first_octet = int(octets[0])
    if 1 <= first_octet <= 223:
        print("unicast")
    elif 224 <= first_octet <= 239:
        print("multicast")
    else:
        print("unused")
