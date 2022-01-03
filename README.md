# Flask Rest API e-shop and order system for 3D printing service

The application is running from the main.py file

## Register of customers

### Reguest

`POST /register`

  curl -X POST -H "Content-Type: application/json" -d '{"password": "<password>", "email": "<email>", "first_name": "<first_name>", "last_name": "<last_name>", "phone": "+359111111111}' http://127.0.0.8:5000/register
  
### Response
  
  HTTP/1.1" 201 CREATED
  
  {
    "token": "<token>"
  }

## Login of customers

### Reguest

`POST /login`

  curl -X POST -H "Content-Type: application/json" -d '{"password": "<password>", "email": "<email>"}' http://127.0.0.8:5000/register
 
### Response
  
  HTTP/1.1" 200 OK
  
  {
    "token": "<token>"
  }
  
## Create order for 3D printing service
  
### Reguest
  
`POST /customers/orders`
  
  curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{"title": "<title>", "description": "<description>", "stl": <stl_file_in_base64>, "address": "<address>"}' http://127.0.0.8:5000/customers/orders
  
  ! (color optional) !
  
### Response
  
  HTTP/1.1" 201 CREATED
  
  {
    "color": null,
    "pk": 9,
    "address": "<address>",
    "description": "<description>",
    "title": "buton",
    "stl_url": "<url_in_aws_s3_bucket>",
    "create_on": "2022-01-03T11:16:51.478377",
    "customer_pk": 7
 }
  
  
 ## List all orders for 3D printing service
 
 ### Reguest
  
`GET /customers/orders`
  
  curl -H "Authorization: Bearer <token>" http://127.0.0.8:5000/customers/orders
  
  
### Response
  
  HTTP/1.1" 200 OK
  
  {
    "color": null,
    "pk": 9,
    "address": "<address>",
    "description": "<description>",
    "title": "buton",
    "stl_url": "<url_in_aws_s3_bucket>",
    "create_on": "2022-01-03T11:16:51.478377",
    "customer_pk": 7
 }
  

## Update info about order (on update you can't make change of the stl file, you must make new order for new file!)
  
### Reguest
  
  `PUT /customers/orders/<int:pk_>`
  
    curl -X PUT "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{"title": "<title>", "description": "<description>", "stl_url": "<stl_url_in_s3_bucket>", "address": "<address>"}' http://127.0.0.8:5000/customers/orders/<int:pk_>
  
### Response
  
  HTTP/1.1" 200 OK
  
  {
    "color": null,
    "pk": 9,
    "address": "<address>",
    "description": "<description>",
    "title": "buton",
    "stl_url": "<url_in_aws_s3_bucket>",
    "create_on": "2022-01-03T11:16:51.478377",
    "customer_pk": 7
 }
  
  
## Delete order
  
### Request
  
  'DELETE /customers/orders/<int:pk_>`
  
  curl -X DELETE -H "Authorization: Bearer <admin_token>" http://127.0.0.8:5000/customers/orders/<int:pk_>
  
### Response
    
  HTTP/1.1" 204 NO CONTENT
  
## Create admin 
  
### Request
    
 `POST /admins/create-admin`

  curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <admin_token>" -d '{"password": "<password>", "email": "<email>", "first_name": "<first_name>", "last_name": "<last_name>", "phone": "+359111111111}' http://127.0.0.8:5000/admins/create-admin
  
### Response
  
  HTTP/1.1" 201 CREATED
  
  {
    "token": "<token>"
  }
  
## Login of admins

### Reguest

`POST /admins/login`

  curl -X POST -H "Content-Type: application/json" -d '{"password": "<password>", "email": "<email>"}' http://127.0.0.8:5000/admins/login
 
### Response
  
  HTTP/1.1" 200 OK
  
  {
    "token": "<token>"
  }
  
  
## Create worker
  
### Request
    
 `POST /workers/create-workers`

  curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <admin_token>" -d '{"password": "<password>", "email": "<email>", "first_name": "<first_name>", "last_name": "<last_name>", "phone": "+359111111111}' http://127.0.0.8:5000/workers/create-workers
  
### Response
  
  HTTP/1.1" 201 CREATED
  
  {
    "token": "<token>"
  }
  
## Login of workers

### Reguest

`POST /workers/login`

  curl -X POST -H "Content-Type: application/json" -d '{"password": "<password>", "email": "<email>"}' http://127.0.0.8:5000/workers/login
 
### Response
  
  HTTP/1.1" 200 OK
  
  {
    "token": "<token>"
  }
  

  

  
  
  
  
  
  
  
  
