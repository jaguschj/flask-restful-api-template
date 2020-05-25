http POST http://127.0.0.1:5000/api/bu name="VC" description="Vibration Control" 
 http POST http://127.0.0.1:5000/api/bu name="MFSHC" description="MFS Heating Cooling" 
 http GET http://127.0.0.1:5000/api/bu
 http GET http://127.0.0.1:5000/api/bu/2
 http PUT http://127.0.0.1:5000/api/bu/2 description="MFS Heating/Cooling"
 http GET http://127.0.0.1:5000/api/bu/1
REM  http DELETE http://127.0.0.1:5000/api/bu/2
 http DELETE http://127.0.0.1:5000/api/bu/1
 http GET http://127.0.0.1:5000/api/bu
