import os
from flask import Flask, jsonify
import requests
from google.cloud import secretmanager_v1

app = Flask(__name__)

# Create Secert Name
secret_name = "my_awesome_secret_from_secret_manager"

# Create CLient
secret_manager_client = secretmanager_v1.SecretManagerServiceClient()


def get_numeric_project_id():
    METADATA_URL = 'http://metadata.google.internal/computeMetadata/v1/'
    METADATA_HEADERS = {'Metadata-Flavor': 'Google'}

    try:
        url = METADATA_URL + 'project/numeric-project-id'
        resp = requests.get(
            url,
            headers=METADATA_HEADERS)
        print("Project id is {}".format(resp.text))
        return resp.text
    except requests.exceptions.ConnectionError:
        return "XXX"


@app.route("/", methods=["GET"])
def read_secrets():

    my_secret = secret_manager_client.access_secret_version(
        name=f"projects/{get_numeric_project_id()}/secrets/{secret_name}/versions/latest"
    )

    my_secret_str = my_secret.payload.data.decode('UTF-8')

    return jsonify(my_awesome_secret_from_secret_manager=f"{my_secret_str}"), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
