import pymysql
import sys
import time

from collections import deque

"""
각 조명에 대한 평균값 구하기 (알고리즘 설계)
"""


# 5초 마다
# 5분간 데이터 평균
def data_information():
    conn = pymysql.connect(host='localhost', user='root', port=3306,
                           password='0000', db='curtain', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM brightness"

    cursor.execute(sql)
    res = cursor.fetchall()
    conn.commit()
    conn.close()

    return res


class AverageLight:
    def __init__(self):
        self.data_deque = deque([])
        self.inside_light = [data[1] for data in data_information()]
        self.outside_light = [data[2] for data in data_information()]
        self.hope_list = int(sys.argv[1])

    def control_function(self):
        print(f"inside_right --> {self.inside_light}")
        print(f"outside_right --> {self.outside_light}")
        # curtain
        for data in self.inside_light:
            self.data_deque.append(data)
            data_del = self.data_deque.popleft()

            if data_del > self.hope_list:
                for i in range(6):
                    time.sleep(1)
                    print(f"curtain 단계를 {i}단계까지 올립니다.")
                    continue
            elif self.inside_light == self.hope_list:
                break


AverageLight().control_function()
