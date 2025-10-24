network_input = input('Enter IP network (e.g., 10.1.1.0/24): ')
ip, mask = network_input.split('/')
ip_octets = ip.split('.')
ip_bin = ['{0:08b}'.format(int(octet)) for octet in ip_octets]

mask_int = int(mask)
mask_bin = '1' * mask_int + '0' * (32 - mask_int)
mask_octets = [str(int(mask_bin[i:i+8], 2)) for i in range(0, 32, 8)]
mask_bin_split = [mask_bin[i:i+8] for i in range(0, 32, 8)]

print('Network:')
print(' '.join(ip_octets))
print(' '.join(ip_bin))
print('Mask:')
print('/' + mask)
print(' '.join(mask_octets))
print(' '.join(mask_bin_split))
