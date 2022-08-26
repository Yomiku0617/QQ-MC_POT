# 插件: 开
#install_lib(lib_name="logging",lib_install_name="logging")
import logging
logging.basicConfig(
    level=logging.DEBUG, # 由于默认日志级别为WARNING， 只打印了WARNING, ERROR, CRITICAL的日志
    format='\033[46;30m %(levelname)s \033[0m\033[36m %(message)s \033[0m',
    datefmt='%H:%M:%S',
    # 'filename': 'test.log',
    # 'filemode': 'w' # 默认是追加模式
)
import time
from omega_side.python3_omega_sync import API
from omega_side.python3_omega_sync import frame as omega
from omega_side.python3_omega_sync.bootstrap import install_lib
from omega_side.python3_omega_sync.protocol import *

def keywords_plugin(api:API):
    # 发送一条消息到 omega 并接收，可以用来测试连接
    response=api.do_echo("关键词插件启动成功",cb=None)
    print(str(response.msg)) # hello
    response=api.do_get_players_list(cb=None)
    for player in response:
        logging.info("当前玩家名："+str(player.name))
        print("\033[34m当前玩家名:"+str(player.name)+"\033[0m")
    response=api.do_send_ws_cmd("/say 执行成功！",cb=None)
    logging.info(response.result.CommandOrigin)


omega.add_plugin(plugin=keywords_plugin)
