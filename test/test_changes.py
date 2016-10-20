import unittest

import changes


class TestChanges(unittest.TestCase):
    def test_should_parse_reflog(self):
        reflog = """
            e7c1dc5 HEAD@{0}: pull: Fast-forward
            344d9ea HEAD@{1}: clone: from git@github.com:tigrupodimed/fidelidade-service.git
        """
        reflog_list = changes.parse_reflog(reflog)

        self.assertEqual([('e7c1dc5', '0', 'pull'), ('344d9ea', '1', 'clone')], reflog_list)

    def test_should_build_hash_range(self):
        expected_hash_range = '344d9ea..e7c1dc5'
        hash_ranges = [('e7c1dc5', 'pull'), ('344d9ea', 'clone')]

        builded_hash_range = changes.build_hash_range(hash_ranges)

        self.assertEqual(expected_hash_range, builded_hash_range)

    def test_should_build_hash_range_with_more_than_two_hashes(self):
        expected_hash_range = '344d9ea..e7c1dc5'
        hash_ranges = [('e7c1dc5', '0', 'pull'), ('344d9ea', '1', 'clone'), ('344d4ea', '2', 'clone')]

        builded_hash_range = changes.build_hash_range(hash_ranges)

        self.assertEqual(expected_hash_range, builded_hash_range)
