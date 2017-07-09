# __author__ = 'slh6488'
# -*- coding:utf-8 -*-
import copy


def get_default_params(user_input):
    """
    :param user_input: 请求初始参数
    :return: 将所有的参数小写
    """
    result_params = {}  # 初始化剩余参数
    for keys in user_input.keys():
        new_key = keys.lower()
        result_params[new_key] = user_input[keys]

    return result_params


def get_turn_uppercase_to_lowercase(use_input):
    """
    大写转小写
    :return:
    """
    test_data = copy.deepcopy(use_input)
    input_keys = test_data.keys()  # 先将字典中的key提取出来
    for num in range(len(input_keys)):
        result = ''
        s = input_keys[num]
        for i in range(len(s)):  # 将key转换成小写，以下划线分隔
            if i == 0:
                result += s[0].upper()
            elif s[i - 1] == '_':
                result += s[i].upper()
            elif s[i] != '_':
                result += s[i]
        test_data[result] = test_data[s]  # 新增新元素
        test_data.pop(s)  # 删除原先元素
    return test_data


def get_turn_lowercase_to_uppercase(use_input):
    """
    小写转大写
    :return:
    """
    test_data = copy.deepcopy(use_input)
    input_keys = test_data.keys()  # 先将字典中的key提取出来
    for num in range(len(input_keys)):
        s = input_keys[num]
        result = ''
        for i in range(len(s)):  # 将key转换成大写
            if i == 0:
                result += s[0].lower()
            elif s[i].isupper():
                result += '_' + s[i].lower()
            else:
                result += s[i]
        test_data[result] = test_data[s]
        test_data.pop(s)
    return test_data
