#!/env/python3
import ipaddress

MAX_MASK = int('0xffffffff', 16)

def toString(f: int):
    return intToBin(f) + ' : ' + str(ipaddress.ip_address(f))

def intToBin(s: int):
    return "{0:08b}".format(s)

def getNet(ip_adresses_str_array):
    # преобразуем в объекты IPv4Address для простоты использования
    ips = [ipaddress.ip_address(x).__int__() for x in ip_adresses_str_array]
    return getNetwork(min(ips), max(ips))

def getNetwork(min: int, max: int):
    print(toString(min))
    print(toString(max))

    mask_bits = 0
    # производим побитовое сравнение слва направо
    for i in range(31,-1,-1):
        if (min >> i == max >> i):
            mask_bits += 1
        else:
            break

    # вычисляем маску подсети в виде числа
    mask = MAX_MASK >> (32 - mask_bits) << (32 - mask_bits)
    print(toString(mask))
    # находим ip серти
    first_ip = min & mask
    print(toString(first_ip))
    # обозначение сети в виде xxx.xxx.xxx.xxx/xx
    net = str(ipaddress.ip_address(first_ip)) + '/' + str(mask_bits)
    print(net)
    return ipaddress.ip_network(net)
