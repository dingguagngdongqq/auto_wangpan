import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    value_list = []
    if args is None:
        connection_pool = None
        key = ""
        start = 0
        end = -1
    else:
        connection_pool = args.get("connection_pool", None)
        key = args.get("key", "")
        start = args.get("start", 0)
        end = args.get("end", -1)
    try:
        value_list = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="lrange", params={
            "connection_pool": connection_pool,
            "key": key,
            "start": start,
            "end": end,
        }, _block=("list_lrange", 1, "调用模块"))
    finally:
        args["value_list"] = value_list
