import webapp2
import os
import jinja2

jina_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to StopGo!")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
