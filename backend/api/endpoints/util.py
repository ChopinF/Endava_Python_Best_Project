# endpoints/util.py

import re
from fastapi import HTTPException
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security

API_KEY_NAME = "name"
API_KEY = "key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API KEY")
    return api_key


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Cache:
    def __init__(self):
        self.dict = {}

    def get(self, key: str):
        return self.dict.get(key)

    def set(self, key: str, v):
        return self.dict.setdefault(key, v)

    def clear(self, pattern: str):
        """
        Removes all keys from the cache that match the regex pattern.
        Returns a list of (key, value) tuples that were removed.
        """
        regex = re.compile(pattern)
        to_delete = [(k, self.dict[k]) for k in list(self.dict) if regex.search(k)]
        for k, _ in to_delete:
            del self.dict[k]
        return to_delete
