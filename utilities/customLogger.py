import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)   # 🔑 ADD THIS

        fhandler = logging.FileHandler(filename='Logs/automation.log', mode='a')
        fhandler.setLevel(logging.INFO)  # 🔑 ADD THIS

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%m-%d-%Y %I:%M:%S %p'
        )
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        return logger
