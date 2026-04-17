import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        connection_pool = None
        key = ""
        value_list = []
    else:
        connection_pool = args.get("connection_pool", None)
        key = args.get("key", "")
        value_list = args.get("value_list", [])
    try:
        invoke_result = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="rpush", params={
            "connection_pool": connection_pool,
            "key": key,
            "value_list": value_list,
        }, _block=("list_rpush", 1, "调用模块"))
    finally:
        pass
