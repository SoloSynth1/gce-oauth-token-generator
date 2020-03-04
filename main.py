import argparse

import urllib3


def main(receiving_service_url):

    # Set up metadata server request
    # See https://cloud.google.com/compute/docs/instances/verifying-instance-identity#request_signature
    metadata_server_token_url = 'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience='

    token_request_url = metadata_server_token_url + receiving_service_url
    token_request_headers = {'Metadata-Flavor': 'Google'}

    http = urllib3.PoolManager()
    token_response = http.request('GET', token_request_url, headers=token_request_headers)

    # Fetch the token
    if token_response.status == 200:
        jwt = token_response.data
        return jwt
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("audience")
    args = parser.parse_args()
    print(main(args.audience))
