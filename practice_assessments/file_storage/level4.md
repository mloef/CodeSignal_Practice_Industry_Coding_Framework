// Updated content for level4.md
# Scenario

Your task is to implement a simplified version of a file hosting service.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press “Submit” often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the entire question before coding. Begin by implementing the basic operations and then extend your solution
to support file expiration (TTL), timestamped operations, and state rollback.

## Task

Example of file structure with various files:

```plaintext
[server34] - 24000 Bytes Limit
    Size
    +- file-1.zip 4321 Bytes
    +- dir-a
    |   +- dir-c
    |       +- file-2.txt 1100 Bytes
    |       +- file-3.csv 2122 Bytes
    +- dir-b
        +- file-4.mdx 3378 Bytes
```

## Level 1 – Initial Design & Basic Functions

- **FILE_UPLOAD(file_name, size)**
  - Upload the file to the remote storage server.
  - If a file with the same name already exists, return: `"error: file already exists"`.
- **FILE_GET(file_name)**
  - Return the size of the file as a string, or `"file not found"` if the file doesn’t exist.
- **FILE_COPY(source, dest)**
  - Copy the source file to a new location.
  - If the source file doesn’t exist, return: `"error: source file not found"`.
  - If the destination file already exists, overwrite it.

## Level 2 – Data Structures & Data Processing

- **FILE_SEARCH(prefix)**
  - Find the top 10 files whose names start with the provided prefix.
  - Order results by file size in descending order, and in case of a tie, by file name.
  - Return the result in the format: `"found [file1, file2, ...]"`.

## Level 3 – Refactoring & Encapsulation

Files may have a specified time-to-live (TTL). The following operations include a timestamp parameter:

- **FILE_UPLOAD_AT(timestamp, file_name, file_size)**
- **FILE_UPLOAD_AT(timestamp, file_name, file_size, ttl)**
  - Upload the file at the given timestamp. With a TTL, the file is available for that many seconds.
- **FILE_GET_AT(timestamp, file_name)**
  - Retrieve the file at the given timestamp.
  - If the file does not exist or has expired, return `"file not found"`.
- **FILE_COPY_AT(timestamp, file_from, file_to)**
  - Copy the source file to a new location at the given timestamp.
  - If the source file does not exist or has expired, return `"error: source file not found"`.
  - If the destination file exists, overwrite it.
- **FILE_SEARCH_AT(timestamp, prefix)**
  - Return files in the format `"found at [file1, file2, ...]"` that match the prefix and are still alive at the given timestamp.

## Level 4 – Extending Design & Functionality

- **ROLLBACK(timestamp)**
  - Rollback the state of the file storage to the state at the specified timestamp.
  - All TTLs should be recalculated relative to the rollback timestamp.
  - Return a message in the format: `"rollback to <timestamp>"`.