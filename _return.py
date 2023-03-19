class _httpreq:
    def __init__(self, headers, json, response, status_code):
        self._status_code = status_code
        self._headers = headers
        self._json = json
        self._response = response

    @property
    def headers(self):
        return self._headers
    
    @property
    def json(self):
        return self._json
    
    @property
    def response(self):
        return self._response
    
    @property
    def status_code(self):
        return self._status_code
    
    def __repr__(self):
        return ("httpreq (headers={0}, json={1}, response={2}, status_code={3})".format
                (self._headers, self._json, self._response, self._status_code))  