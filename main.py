#!/env/python3
import ipaddress


def toString(f: int):
    return intToBin(f) + ' : ' + str(ipaddress.ip_address(f))


def intToBin(s: int):
    return "{0:08b}".format(s)


def ipToBinString(ip):
    return ".".join(map(str,[intToBin(int(x)) for x in ip.__str__().split(".")]))


def toBitArray(n: int):
    return [n >> i & 1 for i in range(32 - 1,-1,-1)]

def bitArrayToInt(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

def getNet(ip_adresses_str_array):
    # преобразуем в объекты IPv4Address для простоты использования
    ips = [ipaddress.ip_address(x).__int__() for x in ip_adresses_str_array]
    return getNetwork(min(ips), max(ips))

def getNetwork(min: int, max: int):
    min_bit_array = toBitArray(min)
    max_bit_array = toBitArray(max)

    mask_bit_array = []
    last_true = True
    # производим побитовое сравнение слва направо
    for i in range(0, 32):
        if min_bit_array[i] == max_bit_array[i]:
            if last_true:
                mask_bit_array.append(1)
            else:
                mask_bit_array.append(0)
        else:
            last_true = False
            mask_bit_array.append(0)

    # вычисляем маску подсети
    mask = bitArrayToInt(mask_bit_array)
    # print(toString(mask))
    mask_bits = mask_bit_array.count(1)
    first_ip = min & mask
    net = str(ipaddress.ip_address(first_ip)) + '/' + str(mask_bits)

    return ipaddress.ip_network(net)
