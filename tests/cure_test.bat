http POST http://127.0.0.1:5000/api/cures user_id=3 name="ABC" description="Test Abc" a=1 b=2 bu_id=2 comp_id=2
 http POST http://127.0.0.1:5000/api/cures user_id=3 name="ABCD" description="Test Abcd" a=1 b=3 bu_id=2 comp_id=2
 http GET http://127.0.0.1:5000/api/cures
 http GET http://127.0.0.1:5000/api/cures/2
 http PUT http://127.0.0.1:5000/api/cures/1 user_id=2
 http GET http://127.0.0.1:5000/api/cures/1
 http DELETE http://127.0.0.1:5000/api/cures/2
 http DELETE http://127.0.0.1:5000/api/cures/1
 http GET http://127.0.0.1:5000/api/cures
