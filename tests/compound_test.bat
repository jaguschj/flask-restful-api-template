http POST http://127.0.0.1:5000/api/compounds name="BGNM" description="Test Abc" 
 http POST http://127.0.0.1:5000/api/compounds name="ABCD" description="Test Abcd" 
 http GET http://127.0.0.1:5000/api/compounds
 http GET http://127.0.0.1:5000/api/compounds/2
 http PUT http://127.0.0.1:5000/api/compounds/2 description="Test Rename"
 http GET http://127.0.0.1:5000/api/compounds/1
REM  http DELETE http://127.0.0.1:5000/api/compounds/2
 http DELETE http://127.0.0.1:5000/api/compounds/1
 http GET http://127.0.0.1:5000/api/compounds
