# coding: utf-8
# author: @yos1up


import hiragana2tex as h2t
print(h2t.hiragana2tex('にえー ぶんの まいなすびーぷらすまいなするーと びーにじょうひくよんえーしー'))

# 参考：
# http://blog.sarabande.jp/post/81479479934
# http://coreblog.org/ats/stuff/minpy_web/13/03.html 
import argparse
import urllib
from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
	def __init__(self, *initargs):
		'''
		初期化
		'''
		super(SimpleHTTPRequestHandler, self).__init__(*initargs)
	def handle_query(self, path, query):
		return h2t.hiragana2tex(query)
	def do_GET(self):
		i=self.path.rfind('?')
		if i>=0:
			path, query=self.path[:i], self.path[i+1:]
		else:
			path=self.path
			query=''

		unquoted_query = urllib.parse.unquote(query)
		rslt = self.handle_query(path, unquoted_query)
		if (rslt != ''):
			print('<<< result >>> ', rslt)

		body = ('<img src="http://chart.apis.google.com/chart?cht=tx&amp;chs=1x0&amp;chf=bg,s,FFFFFF00&amp;'
			+ 'chco=000000&amp;chl='
			+ urllib.parse.quote(rslt)+'" />').encode('utf-8');

		self.send_response(200)
		self.send_header('Content-type', 'text/html; charset=utf-8')
		self.send_header('Content-length', len(body))
		self.end_headers()
		self.wfile.write(body)


parser = argparse.ArgumentParser(description='server')
parser.add_argument('-p', '--port',
			   default=8000, help='port number', type=int)
commandargs = parser.parse_args()


host = 'localhost'
port = commandargs.port
httpd = HTTPServer((host, port), MyHandler)
print('serving at port', port)
httpd.serve_forever()
