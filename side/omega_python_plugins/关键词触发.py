# 插件: 开
#install_lib(lib_name="logging",lib_install_name="logging")
from omega_python_plugins.mylog import *
import time
from omega_side.python3_omega_sync import API
from omega_side.python3_omega_sync import frame as omega
from omega_side.python3_omega_sync.bootstrap import install_lib
from omega_side.python3_omega_sync.protocol import *

def keywords_plugin(api:API):
    # 发送一条消息到 omega 并接收，可以用来测试连接
    response=api.do_echo("关键词插件启动成功",cb=None)
    logger.info(str(response.msg)) # hello

    def on_text_packet(packet):
        logger.info("接受到了聊天数据包") # 每种包内容都不一样，具体内容自己看
        logger.info("数据包内容为: "+str(packet)) #{'TextType': 1, 'NeedsTranslation': False, 'SourceName': '2401PT', 'Message': '啊吧', 'Parameters': None, 'XUID': '', 'PlatformChatID': '', 'PlayerRuntimeID': ''}
        playername = str(packet['SourceName'])
        msg = str(packet['Message'])
        msgtype = int(packet['TextType'])
        if (msgtype == 1) or (msgtype == 8):
            if msg == '112' or msg == ('['+playername+']'+' 112'):
                api.do_send_player_cmd("/say 触发成功",cb=None)

    # 订阅某类数据包，比如这个就是聊天的数据包
    response=api.listen_mc_packet(pkt_type="IDText",cb=None,on_new_packet_cb=on_text_packet)

omega.add_plugin(plugin=keywords_plugin)
