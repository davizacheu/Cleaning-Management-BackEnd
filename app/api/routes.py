from flask import Blueprint, request, jsonify

from app.net.requests import LoginRequest, GetUserRolesRequest, GetUsersRequestsRequest, LogoutRequest
from app.schemas.company_schema import CompanySchema
from app.schemas.order_schema import OrderSchema
from app.schemas.role_schema import RoleSchema
from app.services.sign_service import SignService
from app.services.user_service import UserService

bp = Blueprint('authenticate', __name__)

@bp.route('/login', methods=['POST'])
def login():
    service = SignService()
    result = service.login(LoginRequest(request))
    return jsonify(result)

@bp.route('/user/roles', methods=['GET'])
def get_user_roles():
    service = UserService()
    role_schema = RoleSchema()
    company_schema = CompanySchema()
    roles = service.get_user_roles(GetUserRolesRequest(request))
    result = [{"role": role_schema.dump(role), "company": company_schema.dump(company)} for role, company in roles]
    return jsonify(result)

@bp.route('/user/orders', methods=['GET'])
def get_user_orders():
    service = UserService()
    order_schema = OrderSchema()
    company_schema = CompanySchema()
    orders = service.get_user_orders(GetUsersRequestsRequest(request))
    result = [{"order": order_schema.dump(order), "company": company_schema.dump(company)} for order, company in orders]
    return jsonify(result)

@bp.route('/user/logout', methods=['DELETE'])
def logout():
    service = UserService()
    result = service.logout(LogoutRequest(request))
    return jsonify(result)
