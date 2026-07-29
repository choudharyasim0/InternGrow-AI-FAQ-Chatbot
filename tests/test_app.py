import unittest

from app import app


class ChatEndpointTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_chat_accepts_question_payload(self):
        response = self.client.post(
            "/chat",
            json={"question": "What services do you provide?"},
        )

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("answer", data)
        self.assertNotEqual(data["answer"], "Please enter a question.")


if __name__ == "__main__":
    unittest.main()
