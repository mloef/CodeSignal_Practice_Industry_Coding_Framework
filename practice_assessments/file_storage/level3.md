# Scenario

Your task is to implement a simplified version of a file hosting service.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press “Submit” often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the entire question before coding. Start by implementing the basic operations, then extend your solution
to support file expiration using time-to-live (TTL) values and timestamped operations.

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
  - Upload the file and return `"uploaded <file_name>"` on success.
  - If the file exists, return `"error: file already exists"`.

- **FILE_GET(file_name)**
  - Return `"got <file_name>"` if it exists; otherwise, return `"file not found"`.

- **FILE_COPY(source, dest)**
  - Copy the source file and return `"copied <source> to <dest>"` on success.
  - If the source is not found, return `"error: source file not found"`.

## Level 2 – Data Structures & Data Processing

- **FILE_SEARCH(prefix)**
  - Return `"found [file1, file2, ...]"` as described.

## Level 3 – Refactoring & Encapsulation

Files may have a specified time-to-live (TTL). The following operations include a timestamp parameter:

- **FILE_UPLOAD_AT(timestamp, file_name, file_size)**
- **FILE_UPLOAD_AT(timestamp, file_name, file_size, ttl)**
  - Upload the file at the given timestamp.
  - Return `"uploaded at <file_name>"` on success.
  - With a TTL, the file expires after the specified number of seconds.
  - If the file exists, return `"error: file already exists"`.

- **FILE_GET_AT(timestamp, file_name)**
  - Return `"got at <file_name>"` if the file is available at the given timestamp.
  - If not found or expired, return `"file not found"`.

- **FILE_COPY_AT(timestamp, file_from, file_to)**
  - Copy the file at the given timestamp.
  - Return `"copied at <file_from> to <file_to>"` on success.
  - If the source is not found or expired, return `"error: source file not found"`.

- **FILE_SEARCH_AT(timestamp, prefix)**
  - Return `"found at [file1, file2, ...]"` for files that are alive at the given timestamp.