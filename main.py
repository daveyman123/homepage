import re
import cgi
import webapp2
import os
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
class MainHandler(webapp2.RequestHandler):
    def get(self):

        t = jinja_env.get_template("main.html")
        content = t.render()
        self.response.write(content)


class Post(db.Model):
    title = db.StringProperty()
    body = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add = True)
class Index(webapp2.RequestHandler):

    def get(self):
        #postr = ""
        error = ""
        error2 = ""
        stuff2 = ""
        stuff = ""
        error1 = ""
        error3 = ""
        error = self.request.get("error")
        if error:
            d2 = eval(error)
            for k in d2:
                error2 += k+"="+d2[k]
            if 'bodyerror' in d2:
                error1 = d2['bodyerror']
            if 'titleerror' in d2:
                error3 = d2['titleerror']
            if 'title' in d2:
                stuff = d2['title']
            if 'body' in d2:
                stuff2 = d2['body']



        title = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT 5")
        body = db.GqlQuery("SELECT body FROM Post ORDER BY created DESC LIMIT 5")



        t = jinja_env.get_template("front.html")
        content = t.render(title = title, body = body, error1 = error1, error2 = error3, stuff = stuff, stuff2 = stuff2)
        self.response.write(content)


class add(webapp2.RequestHandler):
    def post(self):

        title = self.request.get("subject")
        body = self.request.get("body")
        title_escaped = cgi.escape(title, quote=True)
        body_escaped = cgi.escape(body, quote=True)
        params = dict("")

        if body == "":
            params['bodyerror'] = "no body"
            params['title'] = title
        if title == "":
            params['titleerror']= "no title"
            params['body'] = body
        s = str(params)
        if s != "{}":
            self.redirect("/blog?error=" + s)
        else:
            titles = Post(title = title_escaped, body = body_escaped)
            #bodies = Post(body = body_escaped, title = title_escaped)



            titles.put()
            #bodies.put()

            t = jinja_env.get_template("add.html")
            content = t.render(title = title, body = body)
            self.response.write(content)

class ViewPostHandler(webapp2.RequestHandler):
    def get(self, id):


        entry = db.GqlQuery("SELECT * FROM Post WHERE ID = 'post_id'")



        t= jinja_env.get_template("view.html")
        #content = t.render()
        content = t.render(post = Post.get_by_id(int(id)))
        self.response.write(content)
    def post(self,id):
        t= jinja_env.get_template("view.html")
        #content = t.render()
        content = t.render(post = Post.get_by_id(int(id)))
        self.response.write(content)
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', Index),
    ('/add', add),
    webapp2.Route('/blog/<id:\d+>', ViewPostHandler)
], debug=True)
