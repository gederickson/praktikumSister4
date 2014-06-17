import sys
from omniORB import CORBA
import HelloApp

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

ior = "corbaname::localhost:1050#Hello"
obj = orb.string_to_object(ior)
eo  = obj._narrow(HelloApp.Hello)

message = "Hello from Python"
result  = eo.echoString(message)
print "I said '%s'. The object said '%s'" % (message,result)





