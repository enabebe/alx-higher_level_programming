#!/usr/bin/python3
class LockedClass:
    __setattr__ = ['first_name']
