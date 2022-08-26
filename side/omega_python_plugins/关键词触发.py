# 插件: 开
import time
from omega_side.python3_omega_sync import API
from omega_side.python3_omega_sync import frame as omega
from omega_side.python3_omega_sync.bootstrap import install_lib
from omega_side.python3_omega_sync.protocol import *

def keywords_plugin(api:API):
    # 发送一条消息到 omega 并接收，可以用来测试连接
    response=api.do_echo(">>>关键词plugin连接成功<<<",cb=None)
    print(response.msg)
    response=api.listen_mc_packet(pkt_type="IDText",cb=None,on_new_packet_cb=on_text_packet)


omega.add_plugin(plugin=keywords_plugin)