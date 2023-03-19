from .httpcore import HTTPClient
from ._return import _httpreq

def get(url, headers={}):
    headers, json, response, status_code = HTTPClient().send_request('GET',url,headers)
    return _httpreq(
        headers=headers, json=json, response=response, status_code=status_code)

def head(url, headers={}):
    headers, json, response, status_code = HTTPClient().send_request('HEAD',url,headers)
    return _httpreq(
        headers=headers, json=json, response=response, status_code=status_code)

def post(url, headers={}, json={}):
    headers, json, response, status_code = HTTPClient().send_request('POST',url,headers, json)
    return _httpreq(
        headers=headers, json=json, response=response, status_code=status_code)

def put(url, headers={}, json={}):
    headers, json, response, status_code = HTTPClient().send_request('PUT',url,headers, json)
    return _httpreq(
        headers=headers, json=json, response=response, status_code=status_code)

def delete(url, headers={}):
    headers, json, response, status_code = HTTPClient().send_request('DELETE',url,headers)
    return _httpreq(
        headers=headers, json=json, response=response, status_code=status_code)

def options(url, headers={}):
    headers, json, response, status_code = HTTPClient().send_request('OPTIONS',url,headers)
    return _httpreq(
        headers=headers, json=json, response=response, status_code=status_code)

def trace(url, headers={}):
    headers, json, response, status_code = HTTPClient().send_request('TRACE',url,headers)
    return _httpreq(
        headers=headers, json=json, response=response, status_code=status_code)

def patch(url, headers={}):
    headers, json, response, status_code = HTTPClient().send_request('PATCH',url,headers)
    return _httpreq(
        headers=headers, json=json, response=response, status_code=status_code)
