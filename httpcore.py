from flask import jsonify
import http.client
import urllib.parse
import json as js
import ssl

class HTTPClient:
    def __init__(self):
        '''
        ignore this
        '''

    def send_request(self, method, url, headers={}, json=None):
        parsed_url = urllib.parse.urlparse(url)

        if not parsed_url.path:
            path = '/'
        else:
            path = parsed_url.path

        if parsed_url.query:
            path += '?' + parsed_url.query

        # Create a default SSL context with hostname verification and certificate validation disabled
        context = ssl.create_default_context();context.check_hostname=False;context.verify_mode=ssl.CERT_NONE

        # Send the HTTP(S) request
        if json == None:
            self.conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=10, context=context)
            self.conn.request(method.upper(), path, headers=headers)
        else:
            self.conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=10, context=context)
            self.conn.request(method.upper(), path, body=js.dumps(json), headers=headers)

        response = self.conn.getresponse()
        headers = response.getheaders()
        status_code = response.getcode()

        try:
            json = jsonify(response.read().decode())
        except:
            json = None

        self.conn.close()

        return headers, json, response, status_code
    