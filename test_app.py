import unittest
import uuid

from app import app, gpt_response


class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app.session_id = str(uuid.uuid4())
        # self.context = [{'role': 'system', 'content': 'Give response using the context given'},
        #                 {'role': 'assistant', 'content': 'What is your question or prompt?'}]

    def tearDown(self):
        self.context = None
        self.app.session_id = None

    def test_index(self):
        with app.test_request_context():  # testing for index page
            response = self.app.get('/')
            self.assertEqual(response.status_code, 200)

    def test_result(self):  # test for result page
        with self.app as client:
            response = client.post(
                '/result', data={'message': 'test message'})
            self.assertEqual(response.status_code, 200)

    def test_gpt_response(self):  # test for gpt api integration
        with app.test_request_context():
            response = gpt_response('Hello', self.app.session_id)
            self.assertIsNotNone(response)

    def test_valid_prompt(self):  # test for valid response for prompts
        with self.app as client:
            response = client.post(
                '/result', data={'message': 'What is the meaning of life?'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'What is the meaning of life?', response.data)
            self.assertNotIn(b'Failed to Generate response!', response.data)
