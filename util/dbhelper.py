# -*- coding:utf-8 -*-
from tcsoa.util import dbpool
import logging

log = logging.getLogger('core')


class DBHelper(object):
    config = None

    def __init__(self):

        # logging.debug(self.config)
        self.db = dbpool.get_mysql_connection(self.config)
        self.db.query = self.db.raw  # add this just for compatibility
        # self.db._conn.query('SET AUTOCOMMIT = 1')  # add this of avoid  DBRouter distributed transaction error


class SqlServerHelper(object):
    config = None

    def __init__(self):

        # logging.debug(self.config)
        self.db = dbpool.get_sqlserver_connection(self.config)
        self.db.query = self.db.raw  # add this just for compatibility