import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        connection_pool = None
        key = ""
        values_list = []
    else:
        connection_pool = args.get("connection_pool", None)
        key = args.get("key", "")
        values_list = args.get("values_list", [])
    try:
        invoke_result = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="set_add", params={
            "connection_pool": connection_pool,
            "key": key,
            "values_list": values_list,
        }, _block=("set_sadd", 1, "调用模块"))
    finally:
        pass
