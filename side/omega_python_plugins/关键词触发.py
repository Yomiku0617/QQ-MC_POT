# 插件: 开
import time
from omega_side.python3_omega_sync import API
from omega_side.python3_omega_sync import frame as omega
from omega_side.python3_omega_sync.bootstrap import install_lib
from omega_side.python3_omega_sync.protocol import *

def keywords_plugin(api:API):
    # 发送一条消息到 omega 并接收，可以用来测试连接
    response=api.do_echo("hello",cb=None)
    print(response.msg) # hello
    response=api.do_get_players_list(cb=None)
    for player in response:
        print(player.name) #OmeGoTest
        print(player.runtimeID) #0
        print(player.uuid) #00000000-0000-4000-8000-0000392af26c
        print(player.uniqueID) #-214748364274


omega.add_plugin(plugin=keywords_plugin)