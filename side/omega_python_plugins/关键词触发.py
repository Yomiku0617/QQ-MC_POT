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
    def on_text_packet(packet):
        print("接受到了聊天数据包") # 每种包内容都不一样，具体内容自己看
        print("数据包内容为: ",packet) #{'TextType': 1, 'NeedsTranslation': False, 'SourceName': '2401PT', 'Message': '啊吧', 'Parameters': None, 'XUID': '', 'PlatformChatID': '', 'PlayerRuntimeID': ''}
    
    # 订阅某类数据包，比如这个就是聊天的数据包
    response=api.listen_mc_packet(pkt_type="IDText",cb=None,on_new_packet_cb=on_text_packet) # 有哪些数据包请查看开发文档
    print(response.succ) # True
    print(response.err) # None


omega.add_plugin(plugin=keywords_plugin)