import webapp2
import jinja2
import cloudstorage as gcs
from google.appengine.api import app_identity
import os
from model import Student


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        file = open('start.html')
        self.response.write(file.read())

        
class Form(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        file=open('addstd.html')
        self.response.write(file.read())

class AddStd(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        en = self.request.get('tfname')
        egen = self.request.get('gender')
        edob = self.request.get('dob')
        emobile = self.request.get('mobile')
        eemail = self.request.get('email')
        estream = self.request.get('stream')

        #creating employee instance to store in google ndb
        std = Student()
        std.EName=en
        std.EGender = egen
        std.Edob = edob
        std.EMobile = emobile
        std.EEmail=eemail
        std.EStream = estream
        #putting into google ndb
        key = std.put()
        self.response.write("<h3> Your response have been submitted <a  style='color:red;' href='/form'>click here</a> to submit another respnse </h3>")
        
        
class viewStd(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        std_all = Student.query()
        values = {"std_info":std_all}
        template = JINJA_ENVIRONMENT.get_template('viewstd.html')        
        html = template.render(values)
        self.response.write(html)


class uploadFile(webapp2.RequestHandler):
    def get(self):
        file = open('header.html')
        self.response.write(file.read())
        file = open("uploadfile.html")
        self.response.write(file.read())

class uploaded(webapp2.RequestHandler):
    def post(self):
        file = open('header.html')
        self.response.write(file.read())
        bucket_name = app_identity.get_default_gcs_bucket_name()
        self.response.write("<h4>"+bucket_name+"</h4>")
        
        name = self.request.POST.get('tfName')
        branch = self.request.POST.get('ddBranch')
        self.response.write(name)
        self.response.write(branch)
        
        data = self.request.POST.getall('file1')
        self.response.write(data)
        self.response.write("<hr/>")

        for file in data:
            f1 = gcs.open("/"+bucket_name+"/"+file.filename, 
                            "w", 
                            content_type=file.type)
            f1.write(file.file.read())
            f1.close()
            self.response.write("<h4>https://storage.googleapis.com/"+bucket_name+"/"+file.filename+"</h4>")
        self.response.write("Files uploaded successfully")

                




app = webapp2.WSGIApplication([
 ('/' , MainHandler),
 ('/form' , Form),
 ('/addstd', AddStd),
 ('/viewstd',viewStd),
 ('/upload',uploadFile),
 ('/uploaded',uploaded)

 ] , debug= True)
