 http POST http://127.0.0.1:5000/api/users name="John John"
 http POST http://127.0.0.1:5000/api/users name="Cosi van tute"
 http PUT http://127.0.0.1:5000/api/users/1 name="John Smith"
 http DELETE http://127.0.0.1:5000/api/users/1
 
 http GET http://127.0.0.1:5000/api/users
 
 http GET http://127.0.0.1:5000/api/users/2
 http GET http://127.0.0.1:5000/api/users?name="John John"
 http GET http://127.0.0.1:5000/api/users?limit=2"&"offset=1
 
 http POST http://127.0.0.1:5000/api/todos user_id=3 name="shopping" description="Buy what you can"
 http POST http://127.0.0.1:5000/api/todos user_id=1 name="car fix" description="No User: Do what you can"
 http POST http://127.0.0.1:5000/api/todos user_id=2 name="car fix" description="Do what you can"
 http GET http://127.0.0.1:5000/api/todos
 http DELETE http://127.0.0.1:5000/api/todos/2
 http PUT http://127.0.0.1:5000/api/todos/3 user_id=2 name="edit car fix" description="Do what you can"
 
 