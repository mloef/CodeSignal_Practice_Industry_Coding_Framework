import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict

import numpy
import sortedcontainers

class Server:
  def __init__(self):
     self.filesystem = {}
  
  def performOperations(self, operations):
      results = []
      
      for operation in operations:
        operation_name = operation[0]
        args = operation[1:]

        match operation_name:
          case "FILE_UPLOAD":
            result = self.uploadFile(args)
          case "FILE_GET":
            result = self.getFile(args)
          case "FILE_COPY":
            result = self.copyFile(args)
          case _:
            raise NotImplementedError
        
        results.append(result)
      
      return results

  def uploadFile(self, args):
    file_name, size = args

    if self.filesystem.get(file_name):
      return "error: file already exists"
    
    self.filesystem[file_name] = size

    return f"uploaded {file_name}"
  
  def getFile(self, args):
    [file_name] = args

    if not self.filesystem.get(file_name):
      return "file not found"
    
    return self.filesystem[file_name]

  def copyFile(self, args):
    source, dest = args

    if not self.filesystem.get(source):
      return "error: source file not found"
    
    self.filesystem[dest] = self.filesystem[source]

    return f'copied {source} to {dest}'


def simulate_coding_framework(list_of_lists):
    """
    Simulates a file hosting service based on a series of operations.

    The function processes a list of operations, where each operation is represented as a list of strings.
    Supported operations include:

    Level 1:
      - FILE_UPLOAD(file_name, size)
      - FILE_GET(file_name)
      - FILE_COPY(source, dest)
      
    Level 2:
      - FILE_SEARCH(prefix)
      
    Level 3:
      - FILE_UPLOAD_AT(timestamp, file_name, file_size) or FILE_UPLOAD_AT(timestamp, file_name, file_size, ttl)
      - FILE_GET_AT(timestamp, file_name)
      - FILE_COPY_AT(timestamp, file_from, file_to)
      - FILE_SEARCH_AT(timestamp, prefix)
      
    Level 4:
      - ROLLBACK(timestamp)
    
    Expected output messages:
      - Successful uploads: "uploaded <file_name>" or "uploaded at <file_name>" for timestamped uploads.
      - Successful retrievals: "got <file_name>" or "got at <file_name>".
      - Successful copies: "copied <source> to <dest>" or "copied at <source> to <dest>".
      - Searches: "found [file1, file2, ...]" or "found at [file1, file2, ...]".
      - Rollback: "rollback to <timestamp>".

    Error conditions:
      - If a file already exists during upload: return "error: file already exists".
      - If a file is not found during get operations: return "file not found".
      - If a source file is missing during a copy operation: return "error: source file not found".

    Files uploaded with a TTL expire after the specified number of seconds.
    Operations with timestamps should only consider files that are "alive" at that timestamp.
    
    Note: This function is a stub. You need to implement the full functionality according to the specifications.

    Parameters:
      list_of_lists (List[List[str]]): A list of operations to perform.

    Returns:
      List[str]: A list of output messages corresponding to each operation.
    """
    
    server = Server()

    return server.performOperations(list_of_lists)
