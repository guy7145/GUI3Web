import json
import SimpleHTTPServer
import urlparse

from data import get_data


class HCIRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        # API request for data

        if "/data/" in self.path or "/data?" in self.path:
            parsed_request = urlparse.urlparse(self.path)
            data = json.dumps(get_data(dict(urlparse.parse_qsl(parsed_request[4]))))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(data)
            return

        # Requesting a resource (html, js, css)
        if "/shared/" not in self.path:
            if '/' == self.path:
                self.path = "/index.html"

            if "Mobi" in self.headers['user-agent']:
                # Requested by a mobile device
                self.path = '/mobile%s' % self.path
            else:
                self.path = '/desktop%s' % self.path

        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
