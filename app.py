import os
from flask import Flask, jsonify, request
import base64


app = Flask(__name__)


@app.route("/", methods=["POST"])
def receive_pubsub_messages():
    print("message received")

    envelope = request.get_json()

    if not envelope:
        msg = "no Pub/Sub message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(envelope, dict) or "message" not in envelope:
        msg = "invalid Pub/Sub message format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if "message" in envelope and "data" in envelope["message"]:
        pubsub_message = base64.b64decode(envelope["message"]["data"])
    else:
        pubsub_message = envelope["message"]

    print(pubsub_message)

    return jsonify(message=True), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
