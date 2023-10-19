from http.server import HTTPServer,SimpleHTTPRequestHandler, CGIHTTPRequestHandler
import ssl

httpd = HTTPServer(('localhost', 1443), SimpleHTTPRequestHandler, CGIHTTPRequestHandler)
# Since version 3.10: SSLContext without protocol argument is deprecated. 
# sslctx = ssl.SSLContext()
sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
sslctx.load_cert_chain(certfile='cert.pem', keyfile="private.pem")
httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()

