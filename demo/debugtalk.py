import time
import random

from httprunner.response import ResponseObject
from httprunner import __version__


def get_httprunner_version():
    return __version__

def gen_random_title():
    return f"title_{random.randint(100000,999999)}"
def sum_two(m, n):
    return str(m + n)

def get_doc_id_len(docId):
    print("doc==", docId)
    return str(len(docId))

def sleep(n_secs):
    time.sleep(n_secs)
#自定义函数
def gen_member_id():
    return  f"346636299773{random.randint(100,999)}"

def get_folders_num(response: ResponseObject):
    folders = response.resp_obj.json()["data"]["folders"]
    return len(folders)