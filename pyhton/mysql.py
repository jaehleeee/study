import time
import pymysql
import datetime


def delete_raw_stat(delete_count):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='test', charset='utf8')
    curs = conn.cursor()
    sql = "SELECT FROM USER WHERE `time` < '2020-08-28' LIMIT %s"

    while True:
        deleted_row_count = curs.execute(sql, delete_count)
        print("[{}] Deleted row count: {}".format(datetime.datetime.now(), delete_count))
        if deleted_row_count < 1:
            break
        time.sleep(1)
        # commit 코드는?

    conn.close()


if __name__ == "__main__":
    delete_raw_stat(100000)