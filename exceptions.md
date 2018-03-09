#azure-storage
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#betamax-matchers
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#brent_search
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#build_capi
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#cairosvg
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#ccdproc
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#convertdate
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#craftr
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#dask-ec2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 147, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#egal
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#email_validator
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#envisage
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


#flake8-quotes
##'name'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 189, in run
    hash = hash_url(source_url, hash_type)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 193, in hash_url
    for b in stream_url_progress(url, verb='Hashing'):
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 165, in stream_url_progress
    with urllib.request.urlopen(url) as f:
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 564, in error
    result = self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 756, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 532, in open
    response = meth(req, response)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 570, in error
    return self._call_chain(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/travis/mc/lib/python3.6/urllib/request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 192, in run
    f.write('{}: hash failed\n'.format(meta_yaml['name']))
KeyError: 'name'


