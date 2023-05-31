import json
import random

from index.models import Admin, Mysession
from utils import hash_password


def check_admin_login(admin_name, password):
    if not all([admin_name, password]):
        return None

    # # 对于 admin ，可使用 admin_id 作为 salt
    # password = hash_password(password, admin_id)

    try:
        admin = Admin.objects.get(adminname=admin_name, adminpd=password)
    except Admin.DoesNotExist:
        admin = None
    if admin is not None:
        return 'ok'


def get_session_id():
    res = ''
    for i in range(4):
        num = str(random.randint(1, 9))
        letter = chr(random.randint(65, 90))
        group = random.choice([num, letter])
        res += group
    return res


def set_login_session(name):
    """
    登录验证与权限管理。返回 Session ID。
    @param name:
    @return:
    """
    session_id = get_session_id()

    # 生成自定义session的value
    value = {'name': name, 'power': 'admin'}

    # 将自定义session信息存入数据库
    value = json.dumps(value)
    Mysession.objects.create(session_id=session_id, session_value=value)

    # 将自定义session_id返回
    return session_id
