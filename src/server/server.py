from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
import json

db = {} 

class MyHttpHandler(BaseHTTPRequestHandler):

    global db    

    def print_http_request(self):
        
        print(':: client address   : {}'.format(self.client_address[0] + ':' + str(self.client_address[1])))
        print(':: request line     : {}'.format(self.requestline))
        print(':: request line     : {}'.format(self.headers['User-Agent']))

    # CREATE
    def do_POST(self):

        print(">> do_POST() activated")
        self.print_http_request()

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        key = list(json.loads(post_data).keys())[0]
        value = list(json.loads(post_data).values())[0]

        if key in db :
            print(':: CREATE {}:{} rejected'.format(key, value))
            content = b'CREATE rejected'
        else:
            db[key] = value

            print(':: CREATE {}:{} created'.format(key, value))
            content = b'CREATE accpeted'

        self.send_response_customized(200)
        self.end_headers()
        self.wfile.write(content)

    # READ
    def do_GET(self):

        print(">> do_GET() activated")
        self.print_http_request()

        key = self.path.split('/')[-1]

        if key in db:
            print(':: READ {}:{} completed'.format(key, db[key]))
            content = 'READ accepted for < {} : {} >'.format(key, db[key])
            content = content.encode()
        else:
            print(':: READ {} rejected'.format(key))
            content = b'READ rejected'

        self.send_response_customized(200)
        self.end_headers()
        self.wfile.write(content)

    # UPDATE
    def do_PUT(self):

        print(">> do_PUT() activated")
        self.print_http_request()

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        key = list(json.loads(post_data).keys())[0]
        value = list(json.loads(post_data).values())[0]

        if key in db :
            db[key] = value

            print(':: UPDATE {}:{} completed'.format(key, value))
            content = b'UPDATE completed'
        else:
            print(':: UPDATE {}:{} rejected'.format(key, value))
            content = b'UPDATE rejected'

        self.send_response_customized(200)
        self.end_headers()
        self.wfile.write(content)

    # DELETE
    def do_DELETE(self):

        print(">> do_DELETE() activated")
        self.print_http_request()

        key = self.path.split('/')[-1]

        if key in db:
            del db[key]

            print(':: DELETE {} completed'.format(key))
            content = b'DELETE accepted'
        else:
            print(':: DELETE {} rejected'.format(key))
            content = b'DELETE rejected'

        self.send_response_customized(200)
        self.end_headers()
        self.wfile.write(content)

    def do_OPTIONS(self): # to support CORS from web browsers

        print(">> do_OPTIONS() activated")
        self.print_http_request()

        self.send_response_customized(200)
        
        self.end_headers()

    def send_response_customized(self, code): # to support negative http response for browsers

        browser_list = ['Mozilla', 'Chromium', 'Chrome', 'Safari', 'Firefox', 'Edge']
        for item in browser_list:
            if item in self.headers['User-Agent']:
                if code in [201]:
                    self.send_response(code)
                else:
                    self.send_response(200)
                return
        self.send_response(code)

    def end_headers (self): # to support CORS from web browsers

        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        BaseHTTPRequestHandler.end_headers(self)

if __name__ == "__main__": 
    
    server_name = "localhost"
    server_port = 8080

    restful_server = ThreadingHTTPServer((server_name, server_port), MyHttpHandler)
    print(">> restful-api server started at http://{0}:{1}".format(server_name, server_port))
    print(">> ctrl-c to stop server")

    try:
        restful_server.serve_forever()
    except KeyboardInterrupt:
        restful_server.server_close()
        print(">> restful-api server stopped")

