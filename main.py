# !/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import jinja2
import os
import webapp2
from google.appengine.api import users


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
        variables = {"header": greeting}
        self.response.write(template.render(variables))

class CssiHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/first_day_cssi.html')
        self.response.write(template.render())

class HobbiesHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/hobbies.html')
        self.response.write(template.render())

class FamilyHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/family.html')
        self.response.write(template.render())

class MainPage(webapp2.RequestHandler):
    def get(self):


        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/firstdayOfcssi', CssiHandler),
  ('/hobbies', HobbiesHandler),
  ('/family', FamilyHandler)
], debug=True)
