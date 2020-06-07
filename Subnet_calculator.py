import sys, ipaddress
import math

if __name__== "__main__":
    ipi = ipaddress.ip_interface(sys.argv[1])
    print("Given Block/IP", ipi.ip)
    print("Given Mask", ipi.netmask)
    print("CIDR", str(ipi.network).split('/')[1])
    print("Network", str(ipi.network).split('/')[0])
    #print("Broadcast", ipi.network.broadcast_address)
    cidr = int(str(ipi.network).split('/')[1])

    while(True):
        choice = input('Enter (H) for Host based Subnetting, (S) for subnet based Subnetting, (D) for Network details of given IP ?').lower()
        if choice == 's' or choice == 'h' or choice == 'd':
            break
        else:
            continue

    if choice == 's':
        no_of_subnets = int(input('Enter number of subnets required in power of 2: '))
        no_of_bits = int(math.log(no_of_subnets,2))

        print('Number of bits borrowed into netid: ',no_of_bits)

        if cidr >= 24 :
            host_bits = 32 - cidr - no_of_bits
            #subnets = 2 ** subnet_bits
            Hosts_per_subnet = int(2 ** host_bits)
            print('Hosts_per_subnet:', Hosts_per_subnet)

        if 16 <= cidr < 24:
            host_bits = 32 - cidr
            #subnets = 2 ** subnet_bits
            Hosts_per_subnet = 2 ** host_bits

            print('Hosts_per_subnet:', Hosts_per_subnet)

        print(f'New mask: /{cidr + no_of_bits}: ')
        n = 0
        for i in range(no_of_subnets):
            print(f'Subnet {i}: ')
            print('     First address:', ipi.ip + (n))
            print('     last address:', ipi.ip + + (n) + (Hosts_per_subnet - 1))
            n += Hosts_per_subnet


    elif choice == 'h':
        no_of_hosts = int(input('Enter number of hosts required per subnet: '))

        for i in range(no_of_hosts):
            if i <= no_of_hosts <= (2**(i+2) - 2):
                host_bits = i+2
                print('Host bits', host_bits)
                break
            else:
                continue


        if cidr >= 24:
            subnet_bits = 32 - host_bits - cidr
            subnets = 2 ** subnet_bits
            Hosts_per_subnet = 2 ** host_bits
            print('Hosts_per_subnet:', Hosts_per_subnet)

        if 16 <= cidr < 24:
            subnet_bits = 32 - host_bits - 16
            subnets = 2 ** subnet_bits
            Hosts_per_subnet = 2 ** host_bits

            print('subnets:', subnets)
            print('Hosts_per_subnet:', Hosts_per_subnet)

        print(f'New mask: /{cidr + subnet_bits}: ')
        n = 0
        for i in range(subnets):
            print(f'Subnet {i}: ')
            print('     First address:', ipi.ip + (n))
            print('     last address:', ipi.ip + + (n) + (Hosts_per_subnet - 1))
            n += Hosts_per_subnet

    elif choice == 'd' :
        if cidr >= 24:
            subnet_bits = cidr - 24
            subnets = 2 ** subnet_bits
            host_bits = 32 - cidr
            Hosts_per_subnet = 2 ** host_bits

            print('Total subnets:', subnets)
            print('Hosts_per_subnet:', Hosts_per_subnet)

        if 16 <= cidr < 24:
            subnet_bits = cidr - 16
            subnets = 2 ** subnet_bits
            host_bits = 32 - cidr
            Hosts_per_subnet = 2 ** host_bits

            print('subnets:', subnets)
            print('Hosts_per_subnet:', Hosts_per_subnet)

        n = 0
        network = str(ipi.network).split('/')[0]
        start_ip = ipaddress.IPv4Address(network)

        for i in range(subnets):
            print(f'Subnet {i}: ')
            print('     First address:', start_ip + (n))
            print('     last address:', start_ip + + (n) + (Hosts_per_subnet - 1))
            n += Hosts_per_subnet















