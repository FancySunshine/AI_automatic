import pymysql
import sys
import time

"""
각 조명에 대한 평균값 구하기 (알고리즘 설계)
"""


# 5초마다 5분간 데이터 평균
# mysql 에 저장되어시는 조도값 데이터 가져옴
def data_information():
    conn = pymysql.connect(host='localhost', user='root', port=3306,
                           password='0000', db='curtain', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM brightness ORDER BY `time` desc limit 60"

    cursor.execute(sql)
    res = cursor.fetchall()
    conn.commit()
    conn.close()

    return res

# 데이터 평균 계산
def average_data():
    inside = [data[1] for data in data_information()]
    outside = [data[2] for data in data_information()]
    average_in = sum(inside) / len(inside)
    average_out = sum(outside) / len(outside)
    print(average_in, average_out)
    return average_in, average_out


# 알고리즘 설계
class AverageLight:
    def __init__(self):
        # 평균값 조도
        self.outside_average = average_data()[0]
        self.inside_average = average_data()[1]

        # 희망 조도
        self.hope = int(sys.argv[1])

    def control_function(self):
        print(f"inside_right --> {self.inside_average}")
        print(f"outside_right --> {self.outside_average}")
        while True:
            # LED
            if self.outside_average <= self.inside_average:
                time.sleep(1)
                if self.hope <= self.inside_average:
                    # 라즈베리 파이 코드 삽입 부분
                    print('밝기 약화')
                else:
                    print('밝기 강화')
            # Curtain
            else:
                time.sleep(1)
                if self.hope <= self.inside_average:
                    # 라즈베리 파이 코드 삽입 부분
                    print('커텐 단계 상승')
                else:
                    print('커텐 단계 하강')


if __name__ == '__main__':
    AverageLight().control_function()
