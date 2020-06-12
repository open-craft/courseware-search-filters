"""
Unit test for Exclude CAPA Search Filter Generator

Unit test in order to make sure that the exclude dictionary with
the ExcludeCapaSearchFilterGenerator contains `content_type` key
"""
import unittest

from opencraft_courseware_search_filters import ExcludeCapaSearchFilterGenerator

class TestExcludeCapaSearchFilterGenerator(unittest.TestCase):
    def test_exclude_dictionary_for_content_type_key(self):
        search_filter = ExcludeCapaSearchFilterGenerator()
        self.assertIn("content_type", search_filter.exclude_dictionary())

if __name__ == "__main__":
    unittest.main()
