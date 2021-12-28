from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from managers.user import UserManager
from schemas.request.user import (
    CustomerRegisterRequestSchema,
    CustomerLoginRequestSchema,
    AdminLoginRequestSchema,
    WorkerLoginRequestSchema,
)
from utils.decorators import validate_schema


class Register(Resource):
    @validate_schema(CustomerRegisterRequestSchema)
    def post(self):
        user = UserManager.register(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class Login(Resource):
    @validate_schema(CustomerLoginRequestSchema)
    def post(self):
        user = UserManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200


class LoginAdmin(Resource):
    @validate_schema(AdminLoginRequestSchema)
    def post(self):
        user = UserManager.login_admin(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200


class LoginWorker(Resource):
    @validate_schema(WorkerLoginRequestSchema)
    def post(self):
        user = UserManager.login_worker(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200
