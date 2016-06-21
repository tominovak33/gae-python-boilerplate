import os
import jinja2
import webapp2
from webapp2_extras import json
import MySQLdb
import config

from google.appengine.api import users

# [START DB]
# When running on Google App Engine, connect to the cloud database
# https://cloud.google.com/appengine/docs/python/cloud-sql/#code_sample_overview
# if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
#     db = MySQLdb.connect(
#         host=config.production_database.get('host'),
#         user=config.production_database.get('user'),
#         passwd=config.production_database.get('password'),
#         db=config.production_database.get('name'),
#         cursorclass=MySQLdb.cursors.DictCursor
#     )
# # When running locally, connect to a local db
# else:
#     # add cursorclass=MySQLdb.cursors.DictCursor to constructor means that values can be accessed by their column names
#     db = MySQLdb.connect(
#         host=config.local_database.get('host'),
#         user=config.local_database.get('user'),
#         passwd=config.local_database.get('password'),
#         db=config.local_database.get('name'),
#         cursorclass=MySQLdb.cursors.DictCursor
#     )
# [END DB]

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            # nickname = user.nickname() # use later if needed

        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'


        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
            'description': 'Tomi - Google App Engine - Python Boilerplate'
        }

        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.set_status(405)
        self.response.headers['Content-Type'] = 'application/json'

        res = {
            'error': 'You cannot POST to this url endpoint.'
        }
        self.response.write(json.encode(res))


class AboutHandler(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'description': "A boilerplate site for quickly getting started with Google App Engine and Python.",
        }
        template = JINJA_ENVIRONMENT.get_template('templates/about.html')

        self.response.write(template.render(template_values))


class ExamplesHandler(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'description': "Examples and code snippets",
        }
        template = JINJA_ENVIRONMENT.get_template('templates/examples.html')

        self.response.write(template.render(template_values))


class URLTestHandler(webapp2.RequestHandler):

    def get(self, url):
        template = JINJA_ENVIRONMENT.get_template('templates/url.html')
        template_values = {
            'url': url
        }

        self.response.write(template.render(template_values))

    def post(self, url):
        self.response.set_status(405)
        self.response.headers['Content-Type'] = 'application/json'
        res = {
            'error': 'You cannot POST to this url endpoint.'
        }
        self.response.write(json.encode(res))

app = webapp2.WSGIApplication([
    webapp2.Route('/', handler=HomeHandler, name='home'),
    webapp2.Route('/about', handler=AboutHandler, name='about'),
    webapp2.Route('/examples', handler=ExamplesHandler, name='example'),
    # '/<url> must be the last route defined as otherwise other routes like '/new' etc will fall into that route
    # and will get treated as if 'new' was the value of a short url so they must be 'caught' first
    webapp2.Route('/<url>', handler=URLTestHandler, name='url-test'),
], debug=True)
