#!/usr/bin/python3
"""
This module creates a FileStorage instance for the console
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
