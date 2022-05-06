import logging

class Logger:
    def __init__(self, name, sh_level, ft_level, path):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        Format = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        # 定义日志内容格式时，必须通过logging.Formatter（曾有遗漏）
        sh = logging.StreamHandler()
        sh.setLevel(sh_level)
        sh.setFormatter(Format)
        fh = logging.FileHandler(path)
        fh.setLevel(ft_level)
        fh.setFormatter(Format)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def logging_info(self, message):
        self.logger.info(message)

    def logging_debug(self, message):
        self.logger.debug(message)

    def logging_warning(self, message):
        self.logger.warning(message)

    def logging_error(self, message, *args, **kwargs):
        self.logger.error(message,*args, **kwargs)

    def logging_critical(self, message):
        self.logger.critical(message)

