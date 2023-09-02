import math
from bitarray import bitarray

class BloomFilter(object):
    def __init__(self, size, expected_elements=100_000):
        self.size = size
        self.expected_elements = expected_elements

        self.bloom_filter = bitarray(self.size)
        self.bloom_filter.setall(0)

        self.hash_fn_number = round((self.size / self.expected_elements) * math.log(2))

    def add_to_filter(self, item):
        for i in range(self.hash_fn_number):
            self.bloom_filter[self._get_hash(item, i)] = 1

    def check_in_not_in_filter(self, item):
        for i in range(self.hash_fn_number):
            if self.bloom_filter[self._get_hash(item, i)] == 0:
                return True
        return False

    def _get_hash(self, item, K):
        return self._get_fnv1a_hash(str(K) + item)
    # def _get_djb2_hash(self, s):
    #     h = 5381
    #     for x in s:
    #         h = ((h << 5) + h) + ord(x)
    #     return h % self.size
    def _get_fnv1a_hash(self, s):
        h = 0x811c9dc5
        for x in s:
            h = ((ord(x) ^ h) * 0x01000193) & self.size
        return h


bf = BloomFilter(1_000_000, 100_000)

base_ip = '192.168.1.'
bf.add_to_filter(base_ip + str(1))

for i in range(1, 100_000):
    if not bf.check_in_not_in_filter(base_ip + str(i)):
        print(base_ip + str(i))