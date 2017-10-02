class Employee:
  def __init__(self,first,last,dob):
    self.first = first
    self.last = last
    self.dob  = dob
    self.age = 2017 - dob
    self.fullname = '{} {}'.format(first,last)
    
  def fullname(first,last):
    return ('{} {}'.format(first,last))
    
  def age(age):
    return ("age is {}".format(age))
    
class Aiwi:
  def __init__(self,surname,givenname,dob):
    self.surname = surname
    self.givenname = givenname
    self.fullname = givenname + givenname
    self.dob = dob
    
  def fullname(surname,givenname):
    return ('{} {}'.format(givenname,surname))
    
class child(Aiwi,Employee):
  pass

Eg = child('ravi','teja',20)
print(Eg.fullname)
