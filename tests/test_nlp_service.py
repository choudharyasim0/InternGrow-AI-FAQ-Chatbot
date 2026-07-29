import unittest

from services.nlp_service import NLPService


class NLPServiceTest(unittest.TestCase):
    def test_clean_returns_expected_text(self):
        service = NLPService()
        cleaned = service.clean("Hello, world! This is a test.")
        self.assertEqual(cleaned, "hello world this is a test")


if __name__ == "__main__":
    unittest.main()
