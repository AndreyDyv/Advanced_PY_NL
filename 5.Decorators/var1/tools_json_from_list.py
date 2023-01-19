import datetime as dt
import json


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

        try:
            data = json.load(open('log_from_list.json'))
        except:
            data = []

        data.append(log)
        with open('log_from_list.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2)

        return result

    return new_function


def logger_decor_param(log_path):
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

            try:
                data = json.load(open(log_path))
            except:
                data = []

            data.append(log)
            with open(log_path, 'w', encoding='UTF-8') as file:
                json.dump(data, file, indent=2)

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
