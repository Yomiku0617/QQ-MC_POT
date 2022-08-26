# 插件: 开
import logging

class logger():
    logging.basicConfig(
        level=logging.DEBUG, # 由于默认日志级别为WARNING， 只打印了WARNING, ERROR, CRITICAL的日志
        #format='\033[45;30m %(levelname)s \033[0m\033[35m %(message)s \033[0m',
        format='%(message)s'
    )
    def debug(msg):
        #return logging.debug(("\033[1;35m {} \033[0m").format(msg))
        return logging.debug('\033[45;30m DEBUG \033[0m\033[35m'+' '+msg+'\033[0m')

    def info(msg):
        #return logging.info(("\033[1;36m {} \033[0m").format(msg))
        return logging.info('\033[46;30m INFO \033[0m\033[36m'+' '+msg+'\033[0m')

    def warning(msg):
        #return logging.warning(("\033[1;33m {} \033[0m").format(msg))
        return logging.warning('\033[43;30m WARNING \033[0m\033[33m'+' '+msg+'\033[0m')

    def error(msg):
        #return logging.error(("\033[1;34m {} \033[0m").format(msg))
        return logging.error('\033[44;30m ERROR \033[0m\033[34m'+' '+msg+'\033[0m')

    def critical(msg):
        #return logging.critical(("\033[1;31m {} \033[0m").format(msg))
        return logging.critical('\033[45;30m CRITICAL \033[0m\033[1;31m'+' '+msg+'\033[0m')