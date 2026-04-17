import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    field_list = []
    if args is None:
        connection_pool = None
        key = ""
    else:
        connection_pool = args.get("connection_pool", None)
        key = args.get("key", "")
    try:
        field_list = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="hkeys", params={
            "connection_pool": connection_pool,
            "key": key,
        }, _block=("hash_hkeys", 1, "调用模块"))
    finally:
        args["field_list"] = field_list
