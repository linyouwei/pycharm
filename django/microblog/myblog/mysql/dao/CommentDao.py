from myblog.mysql.DBUtil import DBUtil
import json
from myblog.mysql.CJsonEncoder import CJsonEncoder



class CommentDao:
    def __init__(self):
        self.db = DBUtil()

    def addComment(self, content, create_time, daily_id, user_id):
        db = DBUtil()
        print(content, create_time, daily_id, user_id)
        db.execute("INSERT INTO `COMMENT` VALUE(ID,'%s','%s',%d,%d)"%(content, create_time, daily_id, user_id))

    def getAllComments(self):
        db = DBUtil()
        pass

    def getAllCommentByDailyId(self, id):
        db = DBUtil()
        data = self.db.execute_select(
            "SELECT c.`ID`,c.`CONTENT`,c.`create_time`,c.`daily_id`,c.`user_id`,u.`USERNAME` FROM `comment` AS c LEFT JOIN `user_login` AS u ON c.`USER_ID`=u.`ID` WHERE c.`daily_id` = %s",
            id)
        commentList = []
        if data:
            for row in data:
                dict = {}
                dict['id'] = row[0]
                dict['content'] = row[1]
                dict['create_time'] = row[2]
                dict['daily_id'] = row[3]
                dict['user_id'] = row[4]
                dict['user_name'] = row[5]
                commentList.append(dict)
        return commentList

    def getLastComment(self, daily_id,user_id):
        db = DBUtil()
        row = self.db.execute_select("SELECT c.`ID`,c.`CONTENT`,c.`create_time`,c.`daily_id`,c.`user_id`,u.`USERNAME` FROM `comment` AS c LEFT JOIN `user_login` AS u ON c.`USER_ID`=u.`ID` WHERE c.`daily_id` = %s AND c.`USER_ID`=%s  ORDER BY CREATE_TIME DESC LIMIT 1",
                                     (daily_id,user_id))[0]
        print(row)
        dict = {}
        dict['id'] = row[0]
        dict['content'] = row[1]
        dict['create_time'] = json.dumps(row[2], cls=CJsonEncoder)
        dict['daily_id'] = row[3]
        dict['user_id'] = row[4]
        dict['user_name'] = row[5]
        print(dict)
        return dict
