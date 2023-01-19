import datetime as dt
import json
import os


def logger_decor(old_function):
    def new_function(*args, **kwargs):
        start = str(dt.datetime.now())

        result = old_function(*args, **kwargs)

        arguments = f'Positional arguments: {args} ___ Keyword arguments: {kwargs}'

        log = {
            'date_time': start,
            'function_name': old_function.__name__,
            'arguments': arguments,
            'return': result
        }

        if 'log_from_os.json' not in os.listdir(os.getcwd()):
            with open('log_from_os.json', 'w', encoding='UTF-8') as file:
                json.dump(log, file, indent=2)
        else:
            with open('log_from_os.json', 'a', encoding='UTF-8') as file:
                json.dump(log, file, indent=2)

        return result

    return new_function


def logger_decor_param(log_path: str):
    def logger_decor(old_function):
        def new_function(*args, **kwargs):
            start = str(dt.datetime.now())

            result = old_function(*args, **kwargs)

            arguments = f'Positional arguments: {args} ___ Keyword arguments: {kwargs}'

            log = {
                'date_time': start,
                'function_name': old_function.__name__,
                'arguments': arguments,
                'return': result
            }

            if log_path not in os.listdir(os.getcwd()):
                with open(log_path, 'w', encoding='UTF-8') as file:
                    json.dump(log, file, indent=2)
            else:
                with open(log_path, 'a', encoding='UTF-8') as file:
                    json.dump(log, file, indent=2)
            return result

        return new_function

    return logger_decor


if __name__ == '__main__':
    @logger_decor
    def summator(a, b):
        return a + b


    summator(15, b=9)
    summator(50, 3)
    summator(a=5, b=8)
