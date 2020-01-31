import unittest
import copy


def all_ips(string):
    all_found_ips = []
    all_ips_inner(string, "", [], all_found_ips)
    return all_found_ips


def all_ips_inner(string, prefix, prev_numbers, all_found_ips):
    if len(prev_numbers) == 4:
        if len(prefix) == 0 and len(string) == 0:
            all_found_ips.append(".".join(prev_numbers))
        return
    
    if len(string) > 0:
        new_string = string[1::]
        new_prefix = prefix + string[0]
        if int(new_prefix) < 256:
            all_ips_inner(new_string, new_prefix, prev_numbers, all_found_ips)

    if len(prefix) > 0:
        prev_numbers_copy = copy.copy(prev_numbers)
        prev_numbers_copy.append(prefix)
        all_ips_inner(string, "", prev_numbers_copy, all_found_ips)


class TestAllIps(unittest.TestCase):
    def test_all_ips(self):
        self.assertEqual(
            sorted(all_ips("25525511135")),
            sorted(["255.255.11.135", "255.255.111.35"])
        )


if __name__ == '__main__':
    unittest.main()
