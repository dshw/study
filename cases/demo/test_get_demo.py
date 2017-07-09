# __author__ = 'slh6488'
# -*- coding:utf-8 -*-
# Get
# 获取单个酒店的点评

import copy
import logging
from tcsoa.case import DsfCase
from tcsoa.decorators import gen
import config as con
from data.get_demo import GetHotelReviewDbHelper

log = logging.getLogger(__name__)  # 记录日志


class GetSingleHotelReviewInfo(DsfCase):
    @classmethod
    def setUpClass(cls):
        cls.api_name = 'Get'  # apiName
        cls.service_name = 'GHotelCommentList'  # serviceName
        cls.sg_key = 'resourcedsf'  # config文件中dsf字典里对应的项目key
        cls.db = GetHotelReviewDbHelper()

    def test_get_demo(self):
        """
        脚本文件，及用例以test开头，名称小写，单词与单词之间用下划线分开
        :return:
        """
        use_input = {
            "hotelId": 6140,  # 酒店ID
            "PageIndex": 1,  # 页数
            "PageSize": 10,  # 每页大小
            "PlatID": 1,  # 平台ID
            "ClientIP": "10.10.1.0",  # 请求IP
            "CommentType": 2,  # 好中差评筛选， 默认全部。（2：好，3：中，4:差,0:全部）（包含标签筛选）
            "SupplierType": 0  # 需要供应商点评，0：全部点评，3：猫途鹰,else：同程点评以及供应商点评
        }
        res = self.client.get(self.api_name, use_input)  # 发送请求
        self.assertEqual(200, res.status_code, '实际返回编码与期望值不同,{0}'.format(res.status_code))
        self.check_expected_results_and_actual_results(use_input=use_input, actual_results_dict=res.dict)

    def check_expected_results_and_actual_results(self, use_input, actual_results_dict):
        """
        检查预期结果与实际结果
        :param use_input:
        :param actual_results:
        :return:
        """
        expected_results = self.db.get_hotel_review_info(use_input=use_input)  # 预期结果
        actual_results = actual_results_dict['HotelCommentList']  # 实际结果

        if expected_results.__len__() != actual_results.__len__():
            self.assertEqual(expected_results.__len__(), actual_results.__len__(),
                             '预期结果与实际结果长度返回不一致'.format(expected_results.__len__(), actual_results.__len__()))
        else:
            for num in range(0, actual_results.__len__()):  # for循环
                self.assertEqual(expected_results[num]["HCAverageScore"], actual_results[num]["HCAverageScore"],
                                 'HCAverageScore,预期结果与实际结果长度返回不一致'.format(expected_results[num]["HCAverageScore"],
                                                                          actual_results[num]["HCAverageScore"]))
                self.assertEqual(expected_results[num]["HCSupplierId"], actual_results[num]["HCSupplierId"],
                                 'HCSupplierId,预期结果与实际结果长度返回不一致'.format(expected_results[num]["HCSupplierId"],
                                                                        actual_results[num]["HCSupplierId"]))
                # 对于每个返回结果进行验证
                #……
                #……
