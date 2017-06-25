import SocketServer

from handler import HCIRequestHandler

Handler = HCIRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()