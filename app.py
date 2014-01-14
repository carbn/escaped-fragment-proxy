#!/usr/bin/env python
import cgi
import sys
import envoy
import urllib

from bottle import route, run, request, HTTPError, Bottle

app = Bottle()
        
@app.route('/')
def serve():
    parts = request.urlparts
    new_url = parts.scheme + '://' + parts.netloc + parts.path
    
    query  = cgi.parse_qs(parts.query)
    fragment = query.pop('_escaped_fragment_', None)
    if query:
        new_url += '?' + urllib.urlencode((key, value[0])
                                           for key, value
                                          in query.items())
    if fragment:
        new_url += '#!' + fragment[0]

    command = 'node_modules/.bin/phantomjs --load-images=false driver.js "' + new_url + '"'
    result = envoy.run(command, timeout=5)

    if result.status_code == 0:
       return result.std_out
            
    return HTTPError(500, 'Bad answer from PhantomJS')


#run(host='localhost', port=8080, debug=True)
