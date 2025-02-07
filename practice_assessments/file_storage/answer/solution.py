from datetime import datetime
from collections import defaultdict


class File():
    def __init__(self, size, timestamp=None, ttl=None):
        self.size = size
        self.timestamp = timestamp
        self.ttl = ttl

TS_OPS = ["FILE_UPLOAD_AT", "FILE_GET_AT", "FILE_COPY_AT", "FILE_SEARCH_AT", "ROLLBACK"]

class FileHost():
    def __init__(self):
        self.filesystem = defaultdict(list)

    def _get_at(self, name, timestamp):
        files = self.filesystem.get(name)

        if not files:
            return None

        for file in reversed(files):
            if file.ttl:
                if file.timestamp + file.ttl < timestamp:
                    continue
            
            return file
        
        return None

    def upload(self, timestamp, name, size, ttl=None):
        if ttl:
            ttl = int(ttl)

        if self._get_at(name, timestamp):
            return "error: file already exists"
        
        self.filesystem[name].append(File(size, timestamp, ttl))

        return f"uploaded {name}"
    
    def get(self, timestamp, name):
        if self._get_at(name, timestamp):
            return f"got {name}"
        else:
            return "file not found"
    
    def copy(self, timestamp, source, dest):
        source_contents = self._get_at(source, timestamp)

        if not source_contents:
            return "error: source file not found"
        
        new_ttl = None
        if source_contents.ttl:
            expiration_ts = source_contents.timestamp + source_contents.ttl
            new_ttl = expiration_ts - timestamp

        new_file = File(source_contents.size, timestamp, new_ttl)

        self.filesystem[dest].append(new_file)

        return f"copied {source} to {dest}"

    def search(self, timestamp, prefix):
        matches = [name for name in self.filesystem.keys() if name.startswith(prefix) and self._get_at(name, timestamp)]
        
        matches.sort(key = lambda name: (self._get_at(name, timestamp).size, name), reverse=True)

        return f"found [{', '.join(matches[:10])}]"
    
    def rollback(self, timestamp, ts_str):
        new_fs = defaultdict(list)
        for name, files in self.filesystem.items():
            for file in files:
                if file.timestamp <= timestamp:
                    new_fs[name].append(file)
        
        self.filesystem = new_fs

        return f"rollback to {ts_str}"


def solution(operations):
    """
    Simulates a file hosting service based on a series of operations.
    The function processes a list of operations, where each operation is represented as a list of strings.

    Note: This function is a stub. You need to implement the full functionality according to the specifications.

    Parameters:
      operations (List[List[str]]): A list of operations to perform.

    Returns:
      List[str]: A list of output messages corresponding to each operation.
    """
    file_host = FileHost()
    results = []
    last_ts = 0

    for operation in operations:
        operation_type = operation[0]
        args = operation[1:]

        if operation_type in TS_OPS:
            last_ts = datetime.strptime(args[0], "%Y-%m-%dT%H:%M:%S").timestamp()
            args = args[1:]

        match operation_type:
            case "FILE_UPLOAD" | "FILE_UPLOAD_AT":
                result = file_host.upload(last_ts, *args)
            case "FILE_GET" | "FILE_GET_AT":
                result = file_host.get(last_ts, *args)
            case "FILE_COPY" | "FILE_COPY_AT":
                result = file_host.copy(last_ts, *args)
            case "FILE_SEARCH" | "FILE_SEARCH_AT":
                result = file_host.search(last_ts, *args)
            case "ROLLBACK":
                ts_str = operation[1]
                result = file_host.rollback(last_ts, ts_str)
        
        results.append(result)
    
    return results