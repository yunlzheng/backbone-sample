# Backbone Sample

## What is Backbon Sample

   Backbone Sample 是一个提供通用rest接口测试服务的Python程序
该程序可以根据测试需求动态添加rest api。
   同时也有几个在学习Backbone过程中用到的示例程序，示例程序会随着学习进程不断完善

## How to add RESTFul API?
1  在/model目录下添加新model文件:

example.py:

    class Example(Document):
	    field1 = StringField()
	    field2 = StringField()

对象字段定义参考[mongoengine filed]

2  在/model目录下__init__.py:


    # coding: utf-8
    from .user import User as user
    from .wine import Wine as wine
    from .todo import Todo as todo
    from .example import Example as example // New Api

3 重新运行python main.py

4 访问新的Rest API

  * (/api/example) GET 获取example对象列表
  * (/api/example) POST 创建新的example对象
  * (/api/example/{uuid}) GET 获取example对象列表
  * (/api/example/{uuid}) UPDATE 更新特定example对象列表
  * (/api/example/{uuid}) DETELE 删除特定的example对象信息


## How to Use?
   * run python ./main.py
   * [vist local]


   Backbone Todo Application
   *****
   ![screenshot](https://github.com/yunlzheng/backbone-sample/raw/master/static/pics/todos.png)

   Backbone wine cellar
   *****
   ![screenshot](https://github.com/yunlzheng/backbone-sample/raw/master/static/pics/cellar.png)


## What is New?
   * [Changelog](CHANGELOG)

## Prerequisites
   * Ubuntu
   * python 2.7+
   * mongoDB

### Installation
   * install mongodb [install mongo]
   * pip install -r requirements.txt

[vist local]: http://localhost:8888
[install mongo]: http://docs.mongodb.org/manual/installation/
[mongoengine filed]: http://docs.mongoengine.org/en/latest/guide/defining-documents.html#fields
