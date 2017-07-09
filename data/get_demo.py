# __author__ = 'yyy12642'
# -*- coding:utf-8 -*-
# 获取单个酒店的点评

import config as con
from util import dbhelper
from util.common_helper_data import get_default_params


class GetHotelReviewDbHelper(dbhelper.DBHelper):
    config = con.sql_server_dict  # 数据库连接

    def get_hotel_review_info(self, use_input=None):
        """
        获取酒店点评信息
        :return:
        """
        # 查询的字段一定要写清楚，不要直接一个*号代替，影响查询效率。需要返回哪些字段，就写明哪些字段即可
        str_sql = "SELECT HCAverageScore,HCSupplierId FROM TCGlobalHotelResource.dbo.HotelComment WHERE 1=1 "
        if use_input != None:  # 拼接查询条件
            if use_input.has_key('hotelId') and use_input['hotelId'] > 0:  # 具体对于传入条件的验证要看服务那边的要求
                str_sql += 'and hotelId={0} '.format(use_input['hotelId'])
                # 其他的查询条件

        return_data = self.db.query(str_sql)  # 查询
        return return_data  # 返回查询结果
