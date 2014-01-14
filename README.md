# Escaped Fragment Proxy

This proxy renders pages according to the [AJAX crawl specification](https://developers.google.com/webmasters/ajax-crawling/).

## Installation

   virtualenv env
   env/bin/pip install -r requrements.txt

   npm install phantomjs

## Running under uwsgi

   env/bin/uwsgi --ini app.ini --http localhost:8080
   
   # to debug and be able to set_trace()
   env/bin/uwsgi --ini app.ini --http localhost:8080 --honour-stdin

## Nginx Configuration

    location / {
        include proxy_params;
        
        if ($args ~* _escaped_fragment_) {
           # this is escaped-fragment-proxy
           proxy_pass localhost:8080;
        }
        # a backend, for handling usual load
        proxy_pass http://localhost:8000;
    }