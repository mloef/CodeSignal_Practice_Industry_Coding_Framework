from datetime import datetime

class Server:
  def __init__(self):
     self.filesystem = {}
     self.expirations = {}
  

  def performOperations(self, operations):
      results = []
      
      for i, operation in enumerate(operations):
        operation_name = operation[0]
        args = operation[1:]

        match operation_name:
          case "FILE_UPLOAD":
            result = self.uploadFile(args)
          case "FILE_GET":
            result = self.getFile(args)
          case "FILE_COPY":
            result = self.copyFile(args)
          case "FILE_SEARCH":
            result = self.fileSearch(args)
          case "FILE_UPLOAD_AT":
            result = self.uploadFileAt(args)
          case "FILE_GET_AT":
            result = self.getFileAt(args)
          case "FILE_COPY_AT":
            result = self.copyFileAt(args)
          case "FILE_SEARCH_AT":
            result = self.fileSearchAt(args)
          case "ROLLBACK":
            result = self.rollback(operations, i, args)
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
    
    return f'got {file_name}'


  def copyFile(self, args):
    source, dest = args

    if not self.filesystem.get(source):
      return "error: source file not found"
    
    self.filesystem[dest] = self.filesystem[source]

    return f'copied {source} to {dest}'


  def fileSearch(self, args):
    [prefix] = args

    matches = []

    for filename in self.filesystem.keys():
      if filename.startswith(prefix):
        matches.append(filename)
    
    matches.sort(key = self.fileSortKey, reverse=True)

    return f'found [{", ".join(matches[:10])}]'


  def fileSortKey(self, fileName):
    size = self.filesystem[fileName]
    intSize = int(size[:-2])
    
    return (intSize, fileName)


  def uploadFileAt(self, args):
    if len(args) == 3:
      timestamp, file_name, size = args
      ttl = None
    else:
      timestamp, file_name, size, ttl = args

    if self.accessFileSystemWithTimestamp(file_name, timestamp):
      return "error: file already exists"
    

    timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S').timestamp()

    if ttl:
      expiration = timestamp + int(ttl)
    else:
      expiration = float('inf')

    self.expirations[file_name] = (expiration, timestamp)
    
    self.filesystem[file_name] = size

    return f"uploaded at {file_name}"
  

  def getFileAt(self, args):
    timestamp, file_name = args

    if not self.accessFileSystemWithTimestamp(file_name, timestamp):
      return "file not found"
    
    return f'got at {file_name}'


  def copyFileAt(self, args):
    timestamp, source, dest = args

    if not self.accessFileSystemWithTimestamp(source, timestamp):
      return "error: source file not found"
    
    self.filesystem[dest] = self.filesystem[source]

    expiration = self.expirations.get(source)
    if expiration:
      self.expirations[dest] = expiration

    return f'copied at {source} to {dest}'


  def fileSearchAt(self, args):
    timestamp, prefix = args

    matches = []

    for filename in self.filesystem.keys():
      if filename.startswith(prefix):
        if self.accessFileSystemWithTimestamp(filename, timestamp):
          matches.append(filename)
    
    matches.sort(key = self.fileSortKey, reverse=True)

    return f'found at [{", ".join(matches[:10])}]'


  def accessFileSystemWithTimestamp(self, fileName, timestamp):
    size = self.filesystem.get(fileName)

    timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S').timestamp()

    if not size:
      return None
  

    if not self.expirations.get(fileName):
      return size

    expiration, written_at = self.expirations.get(fileName)
    if expiration < timestamp or written_at > timestamp:
      return None
    
    return size

  def rollback(self, operations, rollback_index, args):
    [rollback_timestamp_string] = args
    rollback_timestamp = datetime.strptime(rollback_timestamp_string, '%Y-%m-%dT%H:%M:%S').timestamp()

    previous_ops = operations[:rollback_index]

    post_rollback_ops = []

    for operation in previous_ops:
        args = operation[1:]

        possible_timestamp = args[0]
        try:
          op_timestamp = datetime.strptime(possible_timestamp, '%Y-%m-%dT%H:%M:%S').timestamp()
        except NotImplementedError:
          # not a timestamped op, throw it on
          post_rollback_ops.append(operation)
          continue
        
        if op_timestamp <= rollback_timestamp:
          post_rollback_ops.append(operation)
          continue
      
    self.__init__()
    self.performOperations(post_rollback_ops)

    return f"rollback to {rollback_timestamp_string}"

def solution(operations):
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
      operations (List[List[str]]): A list of operations to perform.

    Returns:
      List[str]: A list of output messages corresponding to each operation.
    """
    
    server = Server()

    return server.performOperations(operations)
