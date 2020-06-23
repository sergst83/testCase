import ipaddress
import unittest
import main

# задаем список адресов для созания серти
ip_strings = [
    '192.168.0.3',
    '192.168.0.1',
    '192.168.0.2',
    '192.168.0.63',
    '192.168.0.64'
]
net = '192.168.0.0/25'

class MyTestCase(unittest.TestCase):

    def test_calc_network(self):
        network = main.getNet(ip_strings)
        self.assertEqual(str(network), net, "wrong network calculated")

    def test_all_ip_in_network(self):
        network = main.getNet(ip_strings)
        result = [int(ipaddress.ip_address(x) in network.hosts()) for x in ip_strings]
        self.assertEqual(5, result.count(1))
        self.assertTrue(ipaddress.ip_address('192.168.0.126') in network.hosts())

    def test_ip_not_in_network(self):
        network = main.getNet(ip_strings)
        self.assertFalse(ipaddress.ip_address('192.168.0.129') in network.hosts())
        self.assertFalse(ipaddress.ip_address('8.8.8.8') in network.hosts())

if __name__ == '__main__':
    unittest.main()
