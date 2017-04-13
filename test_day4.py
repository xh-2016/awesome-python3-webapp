#coding:utf-8

#测试对数据库的三张表的操作

import orm,asyncio,sys
from models import User,Blog,Comment

loop = asyncio.get_event_loop()

async def test():
	await orm.create_pool(loop=loop,host='localhost',port=3306,user='root',password='',db='pyblog')
	new_user = User(name='test',email='test@example.com',passwd='1234567890',image='about:blank')
	await new_user.save() #insert
	r = await User.findAll()
	print(r)

	#修改一位用户
	#需要传入id，很不方便
	update_user = User(id='0014920628718533096c58d913d4e20b0403d8c3ce4a488000',name='update',email='update@example.com',passwd='123456',image='about:blank')
	await update_user.update() #update
	r = await User.findAll()
	print(r)

	#删除用户
	await update_user.delete()
	r = await User.findAll()
	print(r)
	await orm.destory_pool() #关闭数据库连接池
		
loop.run_until_complete(test())
loop.close()
if loop.is_closed():
	sys.exit(0)


