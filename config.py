from urllib import parse

SECRET_KEY = "qwertyuiop[]zxcvbnm"

# MySQL所在的主机名
HOSTNAME = "localhost"
# MySQL监听的端口号，默认3306
PORT = "3306"
# 连接MySQL的用户名，读者用自己设置的
USERNAME = "root"
# 连接MySQL的密码
# 在连接前将特殊的密码转码再链接即可
PASSWORD = parse.quote_plus("hy@20011211")
# MySQL上创建的数据库名称
DATABASE = "hyy"

DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
SQLALCHEMY_DATABASE_URI = DB_URI