import re
import cgi
import webapp2
import jinja2
from google.appengine.ext import db

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Becky's HomePage</title>
<style>
h1 {
    text-align: center;
    font-size: 250%;
    color: purple;
}
body {
    background: url("http://upload.wikimedia.org/wikipedia/commons/d/dd/Muybridge_race_horse_animated.gif");
    background-size: cover;
    background-repeat: no-repeat;
    padding-top: 40px;
}
</style>
</head>
<body>
    <h1>Becky's HomePage</h1>
"""
page_header2 = """
<!DOCTYPE html>
<html>
<head>
    <title>Beckys Home Page</title>
</head>
<body>
    <h1>Becky's Home Page</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

add_form = """
<form action="/" method = "post">
    <a href=https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin id="LoginWithAmazon">
    <img border="0" width = 100px height = 100px alt="Login with Amazon"
        src="https://lh4.googleusercontent.com/proxy/M5WvdCwmt4UeSJ0ga92vONavW76e4TLwI5bblxkzM8fc-nQYz3qqhpRBb1NdNjRUPBBJ08rMLS6seba7DFcdd9HWlnOCNmEqXsE4zeShxN2L5yRI_zOyLUYUxiCbhKdtxgo2Q7Ei7wVewrwpecgjwZpdmtYtwa8pD5g0SXbeXK_UC_wd69jlYSmIBXe0bpfirYMIePDI=w426-h346-nc"
        width="156" height="32" />
    </a>
    <label>
        <a href="https://login.yahoo.com/?.src=ym&.intl=us&.lang=en-US&.done=https%3a//mail.yahoo.com"><img border="0" height = 100px width = 100px alt="Login to yahoo mail"
            src="https://s1.yimg.com/rz/d/yahoo_en-US_f_p_bestfit_2x.png"/>
        </a>
    </label>
    <label>
        <a href="http://www.USBank.com"><img border="0" height = 100px width = 100px alt="usbank"
            src="https://lh3.googleusercontent.com/proxy/6BhMdZx8nrIAoNyRMjrx4cIKufn9yRfpcgxjv86j-W-9pOk5eQ8i5EE_oocRxYMiwB4y7dR9tlkVEH23Rx1VCNDAdo0ckDcamS8VY3j40JtgPJKhCA6DpeU=w470-h313-nc">
        </a>
    </label>
    <label>
        <a href="http://www.pncbank.com"><img height = 100px width = 100px border="0" alt="pncbank"
            src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQQQA1Pxvt6rgaxY5io6Qt4C1BlkOPdnkNSz2dBSGto7qSYbShJEKqQ91U">
            </a>
    </label>
    <br>
    <label>
        <a href="https://www.citibank.com.hk/HKGCB/JSO/signon/DisplayUsernameSignon.do"><img border="0" height = 100px width = 100px alt="Login to citibank"
            src="https://goodlogo.com/images/logos/citibank_logo_3126.gif" />
        </a>
    </label>

    <label>
        <a href="http://www.costco.com"><img border="0" height = 100px width = 100px alt="costco"
            src="http://www.commisceo-global.com/images/costco_logo.png">
        </a>
    </label>
    <label>
        <a href="http://www.steinmart.com"><img border="0" height = 100px width = 100px alt="steinmart"
            src="http://www.keycode.com/img/squares/150/3338.png" />
        </a>
    </label>
    <label>
        <a href="http://www.Mymercy.net"><img border="0" height = 100px width = 100px alt="Mercy"
            src="https://lh6.googleusercontent.com/proxy/ofWVDQ0ii0Z3y3h1iIykhFxjH8nH4zxBflPVbkHTvobDVxWhwkjxiT1Ydv-f-EKeOV7Le1umUhoksRKdJmmAyMrc_gBSbgcQhMdsPLsA2VA2VmcnXhcB-RACJgRMF12awL5NeY62-t4dVYyW=w609-h242-nc" />
        </a>
    </label>
    <label>
        <a href="http://www.Kobo.com"><img border="0" height = 100px width = 100px alt="kobo"
            src="https://lh4.googleusercontent.com/proxy/t0wTtFwxC_TxZVpJ3VWfz8fQ-GKUH9daYiSxjrcMQHQtMWZK8qvrn3Qo0DdumRYFEawlwIT0a41gCgmWqdXrfW13flFaznIkopLmd-zzfC7pOUGSzyPV3aDKhB2Kw3GQzYD5kKuNjRwX=w175-h175-nc" />
        </a>
    </label>
    <label>
	<a href="/blog">blog</a>
    </lable>
</form>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = page_header + add_form + page_footer
        self.response.write(content)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
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
