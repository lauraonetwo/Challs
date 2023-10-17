import re

def extract_numerical_values(ip):
    numerical_values = re.findall(r'\d+', ip)
    return '.'.join(numerical_values)

with open('ips.txt', 'r') as file:
    ip_lines = file.readlines()

ip_list = [line.strip() for line in ip_lines]

numerical_ips = [extract_numerical_values(ip) for ip in ip_list]

unique_numerical_ips = list(set(numerical_ips))

print(unique_numerical_ips)
