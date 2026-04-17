import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    connection_pool = None
    if args is None:
        host = "127.0.0.1"
        port = "6379"
        password = ""
        db = 0
    else:
        host = args.get("host", "127.0.0.1")
        port = args.get("port", "6379")
        password = args.get("password", "")
        db = args.get("db", 0)
    try:
        connection_pool = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="redis_pool", params={
            "host": host,
            "port": port,
            "password": password,
            "db": db,
        }, _block=("启动redis连接", 1, "调用模块"))
    finally:
        args["connection_pool"] = connection_pool
