import logging


_LEVELLOG_ = 50

logging.basicConfig(level=_LEVELLOG_)

complex_formatter = logging.Formatter("""
    %(levelname)s :: %(asctime)s  _ %(funcName)s : %(message)s
                    """)
complex_file_handler = logging.FileHandler(
    './logs/requests.log', encoding="utf-8"
                    )
complex_file_handler.setFormatter(complex_formatter)
