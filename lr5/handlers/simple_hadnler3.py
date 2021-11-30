from cleanapi.server import BaseHandler
import json
import requests
import tornado
url_tail = '/volume_rectangular'

class Handler(tornado.web.RequestHandler):
    # The volume of a rectangular parallelepiped
    def post(self):
        # Receive first argument
        a = self.get_argument('a', 'No data received')
        # Receive second argument
        b = self.get_argument('b', 'No data received')
        # Receive third argument
        c = self.get_argument('c', 'No data received')
        s = str(int(a) * int(b) * int(c))

        self.write({'success': 'success'})
        self.write({'version': '0.0.0.2'})
        self.write({'result': s})