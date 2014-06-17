import sys
from omniORB import CORBA
import HelloApp

javaparam = ["ORBInitialHost","localhost","ORBInitialPort","1050"]
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
obj = orb.string_to_object("corbaname::localhost:1050#Hello")
eo = obj._narrow(HelloApp.Hello)
result = eo.sayHello()
print "The object said '%s'." % (result)

