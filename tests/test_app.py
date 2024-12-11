import unittest
from app import app, redisDB  # Import the Flask app and Redis instance

class FlaskAppTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Runs once before all tests, can be used for setup
        pass
    
    def setUp(self):
        # Runs before each test; ensures Redis is clean before each test
        redisDB.flushdb()  # Clear the Redis database for isolation between tests

    def test_visitor_count_increases(self):
        # Test that the visitor count increases on each visit
        with app.test_client() as client:
            # Initial visit (should be 1)
            response = client.get('/')
            self.assertEqual(response.data.decode(), "Welcome! Visitor Count: 1")
            
            # Second visit (should be 2)
            response = client.get('/')
            self.assertEqual(response.data.decode(), "Welcome! Visitor Count: 2")

    def test_visitor_count_with_no_redis(self):
        # Test the visitor count when Redis is not available
        # This tests if the application handles the case gracefully
        original_redis_db = redisDB
        redisDB = None  # Simulate Redis not being available
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 500)  # Internal server error if Redis is down
        redisDB = original_redis_db  # Restore the original Redis connection

if __name__ == '__main__':
    unittest.main()