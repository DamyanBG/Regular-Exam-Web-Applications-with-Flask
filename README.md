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
  
 ## Creating offers from workers
  
 ### Reguest

`POST /workers/offers`
  
  curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <worker_token>" -d '{
    "title": "towa e ofertata za izrabotka na buton",
    "amount": 20,
    "order_pk": 5
 }' http://127.0.0.8:5000/workers/offers
  
 ### Response
  
  HTTP/1.1" 201 CREATED
  
  {
    "pk": 2,
    "title": "towa e ofertata za izrabotka na buton",
    "status": "pending",
    "amount": 20.0,
    "order_pk": 5
  }
  

 ## List all offers (for customer you see offers for your orders, if you are admin or worker - you receive response for all offers)
 
 ### Reguest
  
`GET /workers/offers`
  
  curl -H "Authorization: Bearer <token>" http://127.0.0.8:5000/workers/offers
  
  
### Response
  
  HTTP/1.1" 200 OK
  
  {
        "pk": 5,
        "title": "towa e ofertata za izrabotka na buton",
        "status": "pending",
        "amount": 20.0,
        "order_pk": 16
   }
  
  
## Delete offer 
  
### Request
  
  'DELETE /workers/offers/<int:pk_>`
  
  curl -X DELETE -H "Authorization: Bearer <admin_token>" http://127.0.0.8:5000/workers/offers/<int:pk_>
  
### Response
    
  HTTP/1.1" 204 NO CONTENT
  
## Update info about offer
  
### Reguest
  
  `PUT /workers/offers/<int:pk_>`
  
    curl -X PUT "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{
    "title": "towa e novata oferta za izrabotka na buton",
    "amount": 30,
    "order_pk": 5
     }' http://127.0.0.8:5000/workers/offers/<int:pk_>
  
### Response
  
  HTTP/1.1" 200 OK
  
  {
    "pk": 1,
    "title": "towa e novata oferta za izrabotka na buton",
    "status": "pending",
    "amount": 30.0,
    "order_pk": 5
  }

## Accept offer 
 
### Reguest
  
`GET /customers/offers/<int:pk_>/accept`
  
  curl -H "Authorization: Bearer <token>" http://127.0.0.8:5000/customers/offers/<int:pk_>/accept
  
  
### Response
  
  HTTP/1.1" 200 OK
  
  {
    "pk": 5,
    "title": "towa e ofertata za izrabotka na buton",
    "status": "accepted",
    "amount": 20.0,
    "order_pk": 16
  }
  
## Refuse offer 
 
### Reguest
  
`GET /customers/offers/<int:pk_>/refuse`
  
  curl -H "Authorization: Bearer <token>" http://127.0.0.8:5000/customers/offers/<int:pk_>/refuse
  
  
### Response
  
  HTTP/1.1" 200 OK
  
  {
    "pk": 4,
    "title": "towa e ofertata za izrabotka na buton",
    "status": "rejected",
    "amount": 20.0,
    "order_pk": 15
  }
  
## List all products
 
### Reguest
  
`GET /workers/products`
  
  curl -H "Authorization: Bearer <token>" http://127.0.0.8:5000/workers/products
  
  
### Response
  
  HTTP/1.1" 200 OK
  
  {
        "pk": 1,
        "photo_url": "https://damyans-bucket.s3.eu-central-1.amazonaws.com/6ccbee4a-6212-4d34-bcf7-e19786e5ac0b.jpg",
        "description": "Some description",
        "title": "Some nice product",
        "create_on": "2022-01-01T18:50:51.318235",
        "amount": 30.0
   }
  
  ! ! ! LIST OF ALL PRODUCTS ! ! !
  
## Creating products
  
### Reguest

`POST /workers/products`
  
  curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <worker_token>" -d '{
    "amount": 30,
    "photo_extension": "jpg",
    "photo":<base64photo>
    "title": "Some nice product",
    "description": "Some description"
  }
  ' http://127.0.0.8:5000/workers/offers
  
 ### Response
  
  HTTP/1.1" 201 CREATED
  
  {
    "pk": 11,
    "photo_url": "https://damyans-bucket.s3.eu-central-1.amazonaws.com/e62ef383-a234-49b6-9c80-fbfed6d5174a.jpg",
    "description": "Some description",
    "title": "Some nice product",
    "create_on": "2022-01-03T21:03:50.863564",
    "amount": 30.0
  }
  
## Delete product
  
### Request
  
  'DELETE /workers/products`
  
  curl -X DELETE -H "Authorization: Bearer <admin_token>" http://127.0.0.8:5000/workers/offers/<int:pk_>
  
### Response
    
  HTTP/1.1" 204 NO CONTENT

  
 

  

  
  
  
  
  
  
  
  
