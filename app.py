import os
from flask import Flask
from redis import Redis

# Initialize Flask app
app = Flask(__name__)

# Read Redis host and port from environment variables
redis_host = os.getenv('REDIS_HOST', 'localhost')  # Default to 'localhost' if not set
redis_port = int(os.getenv('REDIS_PORT', 6379))  # Default to 6379 if not set

# Connect to Redis
redisDB = Redis(host=redis_host, port=redis_port)

@app.route("/")
def main():
    redisDB.incr('visitorCount')  # Increment the visitor count in Redis
    visitCount = str(redisDB.get('visitorCount'), 'utf-8')  # Get the visitor count
    return f"Welcome! Visitor Count: {visitCount}"

if __name__ == "__main__":
    # Running the Flask development server (not for production)
    app.run(host="0.0.0.0", port=5000, debug=True)