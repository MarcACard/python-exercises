from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def setUp(self):
        """Code to run before all tests"""
        app.testing = True
        self.client = app.test_client()

    def test_homepage(self):
        with self.client as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            # Response Status
            self.assertEqual(resp.status_code, 200)

            # Check for session data
            self.assertIn("board", session)
            self.assertIn("stats", session)

            # Check for specific HTML Elements
            self.assertIn('id="board"', html)
            self.assertIn('id="alert"', html)
            self.assertIn('id="timer"', html)
            self.assertIn('id="score"', html)
            self.assertIn('id="games-played"', html)
            self.assertIn('id="highscore"', html)
            self.assertIn('id="user-input"', html)
            self.assertIn('id="user-form"', html)

    def test_valid_word(self):
        """Test a valid word that is on the board."""

        with self.client as client:
            with client.session_transaction() as mock_session:
                mock_session["board"] = [
                    ["R", "U", "N", "Z", "Z"],
                    ["R", "U", "N", "Z", "Z"],
                    ["R", "U", "N", "Z", "Z"],
                    ["R", "U", "N", "Z", "Z"],
                    ["R", "U", "N", "Z", "Z"],
                ]

            resp = client.post("/validate-guess", json={"guess": "run"})
            data = resp.get_json()

            self.assertEqual(data["result"], "ok")

    def test_not_on_board(self):
        """Test if a word not on the board return not-on-board"""

        with self.client as client:
            with client.session_transaction() as mock_session:
                mock_session["board"] = [
                    ["R", "U", "N", "Z", "Z"],
                    ["R", "U", "N", "Z", "Z"],
                    ["R", "U", "N", "Z", "Z"],
                    ["R", "U", "N", "Z", "Z"],
                    ["R", "U", "N", "Z", "Z"],
                ]

        resp = client.post("/validate-guess", json={"guess": "book"})
        data = resp.get_json()

        self.assertEqual(data["result"], "not-on-board")

    def test_not_word(self):
        """Test if a non-word return not-word"""

        with self.client as client:
            client.get("/")
            resp = client.post("/validate-guess", json={"guess": "aweinpivawen"})
            data = resp.get_json()

            self.assertEqual(data["result"], "not-word")

    def test_score_game(self):
        """Test that response and session return expected values."""
        with self.client as client:
            client.get("/")
            resp = client.post("/score-game", json={"score": 1})
            data = resp.get_json()

            # Test JSON Response
            self.assertTrue(data["new_highscore"])
            self.assertEqual(data["stats"]["games_played"], 1)
            self.assertEqual(data["stats"]["highscore"], 1)

            # Test User Session
            self.assertEqual(session["stats"]["games_played"], 1)
            self.assertEqual(session["stats"]["highscore"], 1)
