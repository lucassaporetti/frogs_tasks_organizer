import logging as log
import os
from time import sleep
from typing import Type
from src.model.entity_model import Entity

DEFAULT_LOG_FMT = '{} {} {} {}{} {} '.format(
    '%(asctime)s',
    '[%(threadName)-10.10s]',
    '%(levelname)-5.5s',
    '%(name)s::',
    '%(funcName)s(@Line:%(lineno)d)',
    '%(message)s'
)


def log_init(log_file: str, level: int = log.INFO, log_fmt: str = DEFAULT_LOG_FMT):
    with open(log_file, 'w'):
        os.utime(log_file, None)
    f_mode = "a"
    log.basicConfig(
        filename=log_file,
        format=log_fmt,
        level=level,
        filemode=f_mode)

    return log


def print_error(msg: str, arg: str = None):
    print(f"\033[0;31m### Error: {msg} \"{arg}\"\033[0;0;0m")
    sleep(2)
    print('\033[2A\033[J', end='')


def print_warning(msg: str, arg: str = None):
    print(f"\033[0;93m### Warn: {msg} \"{arg}\"\033[0;0;0m")
    sleep(2)
    print('\033[2A\033[J', end='')


def print_list(the_list: list):
    print('\033[2J\033[H')
    print('-=' * 80)
    if the_list and len(the_list) > 0:
        for next_item in the_list:
            if the_list.index(next_item) > 0:
                print('-+' * 80)
            print('\033[0;36m{}\033[0;0;0m'.format(str(next_item)))
    else:
        print('')
        print('\033[0;93mNo data to display\033[0;0;0m')
        print('')
    print('-=' * 80)
    print('')
    wait_enter()


def print_one(entity: Entity):
    print(str(entity))
    wait_enter()


def prompt(message: str = '', end: str = '', clear: bool = False):
    try:
        if clear:
            print('\033[2J\033[H', end='')
        input_data = input('{}{}'.format(message, end))
        return input_data
    except EOFError:
        return None


def wait_enter():
    print('')
    prompt('Press \033[0;32m[Enter]\033[0;0;0m to continue ...')


def check_criteria(partial_value, whole_value):
    if isinstance(whole_value, str):
        return str(partial_value).upper() in whole_value.upper()
    elif isinstance(whole_value, int):
        return int(partial_value) == whole_value
    elif isinstance(whole_value, float):
        return float(partial_value) == whole_value
    elif isinstance(whole_value, bool):
        return bool(partial_value) == whole_value
    else:
        return False


def class_attribute_names(clazz: Type) -> tuple:
    return tuple(vars(clazz()).keys()) if clazz else None


def class_attribute_values(entity: Entity) -> tuple:
    return tuple(entity.__dict__.values()) if entity else None
