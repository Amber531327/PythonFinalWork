# import pickle
# # 读取pkl文件,rb是读取二进制文件，而r是读取文本文件
# file = open('usrs_info.pickle', 'rb')
# info = pickle.load(file)
# print(info)  # 打印输出读取的数据，默认是pandas的dataFrame格式
from pymysql import *

conn = connect(host='localhost', port=3306, user='root', password='123456', database='library',
               charset='utf8mb4')
cursor = conn.cursor()
cursor.execute(
    'insert into students (stu_id, stu_name, stu_college, stu_class,returnbook) values ("103928", "唐奂", "网络空间安全", "2022级",0);')
conn.commit()