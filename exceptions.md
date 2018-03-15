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


#glob2
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


#imagemagick
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


#inifile
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


#inotify-tools
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


#lancet
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


#nbserverproxy
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


#nipy
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


#pandas-plink
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


#paver
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


#pdfminer3k
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


#prettytable
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


#pyferret
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


#pyosf
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


#pytest-benchmark
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


#drmaa
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 147, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#python-gflags
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


#python-leveldb
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


#python-patch
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


#python-primesieve
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


#spake2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 280, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 147, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#pytoml
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


#quantlab
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


#r-ade4
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


#r-afex
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


#r-anomalydetection
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


#r-argparse
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


#r-assertthat
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


#dask-ec2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 282, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 147, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#drmaa
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 282, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 147, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#spake2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 282, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 147, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#dask-ec2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 282, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#drmaa
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 282, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#spake2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 282, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 282, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 186, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 284, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#drmaa
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 284, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#spake2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 284, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 284, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 188, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 284, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#drmaa
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 284, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#spake2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 284, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 284, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 188, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 291, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#drmaa
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 291, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#spake2
##'NoneType' object has no attribute 'create_fork'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 291, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 146, in run
    repo.create_fork()
AttributeError: 'NoneType' object has no attribute 'create_fork'


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 291, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 195, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##name 'rm' is not defined
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm - rf @ (feedstock_dir)
NameError: name 'rm' is not defined


#drmaa
##name 'rm' is not defined
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm - rf @ (feedstock_dir)
NameError: name 'rm' is not defined


#spake2
##name 'rm' is not defined
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm - rf @ (feedstock_dir)
NameError: name 'rm' is not defined


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##name 'rm' is not defined
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @ (feedstock_dir)
NameError: name 'rm' is not defined


#drmaa
##name 'rm' is not defined
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @ (feedstock_dir)
NameError: name 'rm' is not defined


#spake2
##name 'rm' is not defined
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @ (feedstock_dir)
NameError: name 'rm' is not defined


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##name 'rm' is not defined
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @ (feedstock_dir)
NameError: name 'rm' is not defined


#drmaa
##name 'rm' is not defined
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @ (feedstock_dir)
NameError: name 'rm' is not defined


#spake2
##name 'rm' is not defined
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @ (feedstock_dir)
NameError: name 'rm' is not defined


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#drmaa
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#spake2
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#drmaa
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#spake2
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#drmaa
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#spake2
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#dask-ec2
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#drmaa
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#spake2
##local variable 'feedstock_dir' referenced before assignment
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 143, in run
    rm -rf @(feedstock_dir)
UnboundLocalError: local variable 'feedstock_dir' referenced before assignment


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 297, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 298, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 298, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 298, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


#r-corpcor
##'list' object has no attribute 'partition'
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 298, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 201, in run
    source_url = eval_version(source_url)
  File "/home/travis/mc/lib/python3.6/site-packages/rever/tools.xsh", line 26, in eval_version
    rtn = expand_path(v)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 3573, in expand_path
    pre, char, post = s.partition('=')
AttributeError: 'list' object has no attribute 'partition'


