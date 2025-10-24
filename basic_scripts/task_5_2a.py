from ipaddress import ip_network

network_input = input('Enter IP address with mask (e.g., 10.0.1.1/24): ')
net = ip_network(network_input, strict=False)

ip_octets = str(net.network_address).split('.')
ip_bin = ['{0:08b}'.format(int(octet)) for octet in ip_octets]

mask_int = net.prefixlen
mask_bin = '1' * mask_int + '0' * (32 - mask_int)
mask_octets = [str(int(mask_bin[i:i+8], 2)) for i in range(0, 32, 8)]
mask_bin_split = [mask_bin[i:i+8] for i in range(0, 32, 8)]

print('Network:')
print(' '.join(ip_octets))
print(' '.join(ip_bin))
print('Mask:')
print('/' + str(mask_int))
print(' '.join(mask_octets))
print(' '.join(mask_bin_split))
