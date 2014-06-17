javac *.java HelloApp/*.java
orbd -ORBInitialPort 1050&
java HelloServer -ORBInitialPort 1050 -ORBInitialHost localhost&
