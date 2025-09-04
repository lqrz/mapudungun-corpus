import unittest
from data_cleaning.clean_transcriptions import clean_annotations, assert_paths


class TestCleanTranscriptions(unittest.TestCase):
    def test_clean_annotations(self):
        text = "<*spa>hello<uh>world<noise>"
        cleaned = clean_annotations(text)
        self.assertEqual(cleaned, "helloworld")

    def test_assert_paths_valid(self):
        # Should not raise
        try:
            assert_paths("input", "output")
        except AssertionError:
            self.fail("assert_paths raised AssertionError unexpectedly!")

    def test_assert_paths_invalid_input(self):
        with self.assertRaises(AssertionError):
            assert_paths("input/", "output")

    def test_assert_paths_invalid_output(self):
        with self.assertRaises(AssertionError):
            assert_paths("input", "output/")
