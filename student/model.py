#insert ndb to use google database
from google.appengine.ext import ndb


#inheriting a model class to create database table
class Student(ndb.Model):
    'Database table to store Emp Detail'
    EName = ndb.StringProperty()
    EGender = ndb.StringProperty()
    Edob = ndb.StringProperty()
    EMobile = ndb.StringProperty()
    EEmail = ndb.StringProperty()
    EStream = ndb.StringProperty()

  
                 






     