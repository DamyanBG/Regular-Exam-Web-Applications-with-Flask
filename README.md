# Flask Rest API e-shop and order system for 3D printing service

The application is running from the main.py file

## Register of customers

### Reguest

`POST /register`

  curl -X POST -H "Content-Type: application/json" -d '{"password": "<password>", "email": "<email>", "first_name": "<first_name>", "last_name": "<last_name>", "phone": "+359111111111}' http://127.0.0.8:5000/register
  
### Response

## Login of customers

### Reguest

`POST /login`

  curl -X POST -H "Content-Type: application/json" -d '{"password": "<password>", "email": "<email>"}' http://127.0.0.8:5000/register
 
### Response
  
## Create order for 3D printing service
  
`POST /customers/orders`
