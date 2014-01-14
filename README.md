# Escaped Fragment Proxy

This renders pages according to the [AJAX crawl specification](https://developers.google.com/webmasters/ajax-crawling/).

## Running under uwsgi
virtualenv env
env/bin/pip install -r requrements.txt
env/bin/uwsgi --ini app.ini --http :8080

## Nginx Configuration

    location / {
            include uwsgi_params;
            if ($args ~* _escaped_fragment_) {
                    uwsgi_pass unix:/tmp/ajax-proxy.socket;
            }
    }
