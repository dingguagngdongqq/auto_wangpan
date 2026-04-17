# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep
from .import package

import redis
import json


# 建立连接
def redis_pool(host='127.0.0.1', port='6379', password='', db=0):
    pool = redis.ConnectionPool(host=host, port=port, password=password, db=db)
    connection_pool = redis.Redis(connection_pool=pool)
    return connection_pool


# 关闭连接
def redis_close(connection_pool):
    connection_pool.close()
    


# 设置指定 key 的值
def set(connection_pool, key, value):
    connection_pool.set(key, json.dumps(value))


# 获取指定 key 的值
def get(connection_pool, key):
    value = connection_pool.get(key)
    if not value:  # 包括 None 和 b''
        return value
    try:
        # 如果 value 是 bytes，先 decode
        if isinstance(value, bytes):
            value = value.decode('utf-8')
        return json.loads(value)
    except Exception:
        return value  # 或抛异常


'''
哈希hash操作
'''

# 将哈希表 key 中的字段 field 的值设为 value 
def hset(connection_pool, key, field, value):
    connection_pool.hset(key, field, json.dumps(value))


# 获取存储在哈希表中指定字段的值。
def hget(connection_pool, key, field):
    value = connection_pool.hget(key, field)
    return json.loads(value) if value else value


# 获取所有哈希表中的字段
def hkeys(connection_pool, key):
    return [x.decode() for x in connection_pool.hkeys(key)]


# 获取所有哈希表的字段和值
def hgetall(connection_pool, key):
    ret = {}
    for k, v in connection_pool.hgetall(key).items():
        ret[k.decode()] = v.decode() if v else v
    return ret


'''
列表list的操作
'''

# 获取列表长度
def llen(connection_pool, key):
    return connection_pool.llen(key)


# 移出并获取列表的第一个元素
def lpop(connection_pool, key):
    value = connection_pool.lpop(key)
    return value if not value else value.decode('utf-8')


# 将一个或多个值插入到列表头部
def lpush(connection_pool, key, value_list):
    for value in value_list[::-1]:
        connection_pool.lpush(key, value)


# 移除列表的最后一个元素，返回值为移除的元素。
def rpop(connection_pool, key):
    value = connection_pool.rpop(key)
    # return value.decode('utf-8')
    return value if not value else value.decode('utf-8')


# 在列表中添加一个或多个值
def rpush(connection_pool, key, value_list):
    for value in value_list:
        connection_pool.rpush(key, json.dumps(value))


# 通过索引获取列表的值
def lindex(connection_pool, key, index):
    value = connection_pool.lindex(key, index)
    return value if not value else json.loads(value)


# 获取列表指定范围内的元素
def lrange(connection_pool, key, start, end):
    value = connection_pool.lrange(key, start, end)
    for i, item in enumerate(value):
        value[i] = json.loads(item.decode()) if item else item
    return value

# 设置redis中key值的过期时间
def key_expire(connection_pool,key,time):
    connection_pool.expire(key,time)


'''
集合set的操作
'''
# 添加集合成员
def set_add(connection_pool,key,values_list):
    if isinstance(values_list,list):
        connection_pool.sadd(key,*values_list)
    else:
        raise TypeError("参数values_list不是列表类型")


# 获取集合成员
def set_members(connection_pool,key):
     members_set=connection_pool.smembers(key)
     return members_set

# 移除集合成员
def set_romove(connection_pool,key,values_list):
    if isinstance(values_list,list):
        connection_pool.srem(key,*values_list)
    else:
        raise TypeError("参数values_list不是列表类型")







def main(args):
    pass
