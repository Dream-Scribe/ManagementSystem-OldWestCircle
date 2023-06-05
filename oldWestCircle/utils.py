import json, hashlib
from datetime import datetime
from index.models import Mysession
import numpy as np
from sklearn.decomposition import FactorAnalysis
from sklearn.preprocessing import MinMaxScaler

def translateDateId2Date(date_id):
    if date_id == 1:
        return "Monday"
    elif date_id == 2:
        return "Tuesday"
    elif date_id == 3:
        return 'Wednesday'
    elif date_id == 4:
        return 'Thursday'
    elif date_id == 5:
        return 'Friday'
    elif date_id == 6:
        return 'Saturday'
    elif date_id == 7:
        return 'Sunday'
    else:
        return

def translateDate2DateId(date):
    if date == "Monday":
        return 1
    elif date == "Tuesday":
        return 2
    elif date == 'Wednesday':
        return 3
    elif date == 'Thursday':
        return 4
    elif date == 'Friday':
        return 5
    elif date == 'Saturday':
        return 6
    elif date == 'Sunday':
        return 7
    else:
        return

def translateTypeId2Type(type_id):
    if type_id == 0:
        return 'other'
    elif type_id == 1:
        return 'C/C++'
    elif type_id == 2:
        return 'Java'
    elif type_id == 3:
        return 'Python'
    elif type_id == 4:
        return 'Javascript'
    elif type_id == 5:
        return 'HTML/CSS'
    elif type_id == 6:
        return 'PHP'
    elif type_id == 7:
        return 'C#'
    elif type_id == 8:
        return 'SQL'
    else:
        return

def translateType2TypeId(type):
    if type == 'other':
        return 0
    elif type == 'C/C++':
        return 1
    elif type == 'Java':
        return 2
    elif type == 'Python':
        return 3
    elif type == 'Javascript':
        return 4
    elif type == 'HTML/CSS':
        return 5
    elif type == 'PHP':
        return 6
    elif type == 'C#':
        return 7
    elif type == 'SQL':
        return 8
    else:
        return


def get_current_time():
    # 获取当前时间
    current_time = datetime.now()
    # 格式化为字符串
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_time


def check_session(session_id=None):
    try:
        user = Mysession.objects.get(session_id=session_id)
    except Exception as e:
        print(e)
        return 'nobody'

    value = json.loads(user.session_value)

    return value['power']


def hash_password(password, salt):
    """
    使用 SHA-256 哈希算法
    @param password:
    @param salt:
    @return:
    """
    salted_password = salt + password

    # 创建哈希对象
    hasher = hashlib.sha256()

    # 更新哈希对象的内容
    hasher.update(salted_password.encode('utf-8'))

    # 获取哈希值
    hashed_password = hasher.hexdigest()

    # 返回哈希值
    return hashed_password


def calculate_popularity(num, time, point, satisfaction, interaction):
    # 定义评价指标
    X = np.array([[num, time, point, satisfaction, interaction]])

    # 数据预处理，归一化处理
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # 因子分析，提取主成分
    n_components = 4  # 设置提取的主成分数量
    transformer = FactorAnalysis(n_components=n_components, random_state=0)
    X_transformed = transformer.fit_transform(X_scaled)

    # 定义各个维度的权重
    weights = np.array([0.4, 0.2, 0.2, 0.1, 0.1])

    # 计算综合评价分数
    popularity = np.sum(X_transformed * weights) * 100

    return popularity
