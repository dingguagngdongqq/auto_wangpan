from .import package
import xbot_visual

def process2(host,port,password,db):
    """
    启动redis连接
    通过python的第三方redis库建立redis连接，并返回一个redis连接实例。（注意：该指令必须与“关闭redis连接”指令配合使用）
    * @param host，连接地址，默认为127.0.0.1
    * @param port，端口号，默认为6379
    * @param password，redis密码，默认为空
    * @param db，数据库索引，默认为0
    * @return connection_pool，redis连接实例，在后续的指令中传参使用
    """
    outputs = ["connection_pool"]
    inputs = {"host":host,"port":port,"password":password,"db":db}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process2", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process2",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process2", extension_module, activity_func)

def process3(connection_pool,key,value):
    """
    string_set
    设置指定 key 的值
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，用于查找value值的索引名称，建议使用python的标识符命名规则，格式为字符串
    * @param value，存储在key下的值，各种类型均可，该指令会对value进行一次json封装后再set到redis中
    """
    outputs = []
    inputs = {"connection_pool":connection_pool,"key":key,"value":value}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process3", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process3",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process3", extension_module, activity_func)

def process4(connection_pool,key):
    """
    string_get
    获取指定 key 的值。
    * @param connection_pool，
    * @param key，
    * @return value，
    """
    outputs = ["value"]
    inputs = {"connection_pool":connection_pool,"key":key}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process4", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process4",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process4", extension_module, activity_func)

def process5(connection_pool,key,field,value):
    """
    hash_hset
    将哈希表 key 中的字段 field 的值设为 value
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，保存hash的名称，格式为字符串
    * @param field，需要在hash中设置的字段名称，格式为字符串
    * @param value，需要在hash中设置的字段值，格式为字符串
    """
    outputs = []
    inputs = {"connection_pool":connection_pool,"key":key,"field":field,"value":value}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process5", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process5",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process5", extension_module, activity_func)

def process6(connection_pool,key,field):
    """
    hash_hget
    获取指定哈希表中的指定字段的值
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，
    * @param field，
    * @return value，
    """
    outputs = ["value"]
    inputs = {"connection_pool":connection_pool,"key":key,"field":field}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process6", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process6",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process6", extension_module, activity_func)

def process7(connection_pool,key):
    """
    hash_hkeys
    获取所有哈希表中的字段
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，需要查询的hash的名称，格式为字符串
    * @return field_list，返回该查询的hash所有的字段名列表，格式为列表
    """
    outputs = ["field_list"]
    inputs = {"connection_pool":connection_pool,"key":key}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process7", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process7",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process7", extension_module, activity_func)

def process8(connection_pool,key):
    """
    hash_hgetall
    获取指定哈希表中的所有字段和值，并返回一个dict
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，需要查询的hash的名称，格式为字符串
    * @return values_dict，返回该查询的hash所有的字段和值，格式为字典
    """
    outputs = ["values_dict"]
    inputs = {"connection_pool":connection_pool,"key":key}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process8", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process8",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process8", extension_module, activity_func)

def process9(connection_pool,key):
    """
    list_llen
    获取列表长度
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，需要查询的列表key，格式为字符串
    * @return list_len，返回该查询列表的元素个数，格式为整数
    """
    outputs = ["list_len"]
    inputs = {"connection_pool":connection_pool,"key":key}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process9", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process9",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process9", extension_module, activity_func)

def process10(connection_pool,key):
    """
    list_lpop
    移出并获取列表头部的第一个元素
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，用于保存该列表的索引名称，建议使用python的标识符命名规则，格式为字符串
    * @return value，从key这个列表的头部移除的一个元素值
    """
    outputs = ["value"]
    inputs = {"connection_pool":connection_pool,"key":key}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process10", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process10",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process10", extension_module, activity_func)

def process11(connection_pool,key,value_list):
    """
    list_lpush
    将一个或多个值插入到列表头部
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，用于保存该列表的索引名称，建议使用python的标识符命名规则，格式为字符串
    * @param value_list，将在列表头部插入元素值的列表，格式必须为一个列表
    """
    outputs = []
    inputs = {"connection_pool":connection_pool,"key":key,"value_list":value_list}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process11", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process11",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process11", extension_module, activity_func)

def process12(connection_pool,key):
    """
    list_rpop
    移除列表的最后一个元素，返回值为移除的元素。
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，用于保存该列表的索引名称，建议使用python的标识符命名规则，格式为字符串
    * @return value，从key这个列表的尾部移除的一个元素值
    """
    outputs = ["value"]
    inputs = {"connection_pool":connection_pool,"key":key}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process12", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process12",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process12", extension_module, activity_func)

def process13(connection_pool,key,value_list):
    """
    list_rpush
    在列表中添加一个或多个值
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，用于保存该列表的索引名称，建议使用python的标识符命名规则，格式为字符串
    * @param value_list，将依次在列表尾部添加元素值的列表，格式必须为一个列表
    """
    outputs = []
    inputs = {"connection_pool":connection_pool,"key":key,"value_list":value_list}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process13", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process13",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process13", extension_module, activity_func)

def process14(connection_pool,key,index):
    """
    list_lindex
    通过索引获取列表的值
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，需要查询的列表索引名称，格式为字符串
    * @param index， 需要查询的列表指定下标位置，格式为整数
    * @return value，返回列表中该查询下标的元素值，格式为字符串
    """
    outputs = ["value"]
    inputs = {"connection_pool":connection_pool,"key":key,"index":index}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process14", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process14",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process14", extension_module, activity_func)

def process15(connection_pool,key,start,end):
    """
    list_lrange
    获取列表指定范围内的元素
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，需要切片的redis列表的索引名称，必须为redis库中已存在的key
    * @param start，需要获取范围的开始下标，格式为整数
    * @param end，需要获取范围的结束下标，格式为整数
    * @return value_list，获取到的列表指定范围内元素值列表，格式为列表
    """
    outputs = ["value_list"]
    inputs = {"connection_pool":connection_pool,"key":key,"start":start,"end":end}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process15", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process15",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process15", extension_module, activity_func)

def process16(connection_pool):
    """
    关闭redis连接
    
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    """
    outputs = []
    inputs = {"connection_pool":connection_pool}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process16", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process16",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process16", extension_module, activity_func)

def process17(connection_pool,key,values_list):
    """
    set_sadd
    该指令实现了往集合中添加成员
    * @param connection_pool，
    * @param key，
    * @param values_list，
    """
    outputs = []
    inputs = {"connection_pool":connection_pool,"key":key,"values_list":values_list}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process17", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process17",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process17", extension_module, activity_func)

def process19(connection_pool,key,time):
    """
    key_expire
    该指令可以给redis的key值设置过期时间
    * @param connection_pool，redis连接实例，是启动redis连接指令的返回值
    * @param key，需要设置key，格式为字符串
    * @param time，设置过期的时间
    """
    outputs = []
    inputs = {"connection_pool":connection_pool,"key":key,"time":time}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process19", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process19",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process19", extension_module, activity_func)

def process21(connection_pool,key):
    """
    set_members
    该指令实现了获取set集合里面的成员
    * @param connection_pool，
    * @param key，
    * @return membes_set，
    """
    outputs = ["membes_set"]
    inputs = {"connection_pool":connection_pool,"key":key}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process21", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process21",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process21", extension_module, activity_func)

def process22(connection_pool,key,values_list):
    """
    set_srem
    该指令实现了在移除集合的成员
    * @param connection_pool，
    * @param key，
    * @param values_list，
    """
    outputs = []
    inputs = {"connection_pool":connection_pool,"key":key,"values_list":values_list}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.activity_babf50cf.process22", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.activity_babf50cf.process22",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.activity_babf50cf.process22", extension_module, activity_func)

