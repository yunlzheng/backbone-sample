##说明
model表示与数据库Coolection向映射的ORM对象（MongoDB），ORM使用mongoengine实现

##添加API接口
创建文件example.py,并写入一下内容


class Example(Document):
    field1 = StringField()
    field2 = StringField()


修改__init__.py文件
添加一行

from .example import Example as example

重启应用程序
get rootUrl/api/example 获取所有的example对象
get rootUrl/api/example/{uuid} 获取特定的example对象
post rootUrl/api/example 创建新的example对象 需要输入与Example对应的json对象为参数
put rootUrl/api/example/{uuid} 修改已经存在的example对象 需要输入更新的json对象作为参数
delete rootUrl/api/example/{uuid} 删除特定的example实例对象
