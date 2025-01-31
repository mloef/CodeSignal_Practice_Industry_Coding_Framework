# Scenario

Your task is to implement a simplified version of a file hosting service.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press “Submit” often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the entire question before coding. Implement the operations sequentially, starting with basic functions,
and then adding additional features in subsequent levels.

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
  - Return `"uploaded <file_name>"` on success.
  - If a file with the same name already exists, return `"error: file already exists"`.

- **FILE_GET(file_name)**
  - Return `"got <file_name>"` if the file exists.
  - If the file doesn’t exist, return `"file not found"`.

- **FILE_COPY(source, dest)**
  - Copy the source file to a new location.
  - Return `"copied <source> to <dest>"` on success.
  - If the source file doesn’t exist, return `"error: source file not found"`.
  - If the destination file already exists, overwrite it.

## Level 2 – Data Structures & Data Processing

- **FILE_SEARCH(prefix)**
  - Find the top 10 files whose names start with the provided prefix.
  - Order the results by file size in descending order, and in case of a tie, by file name in descending order.
  - Return the result in the format: `"found [file1, file2, ...]"`. If no files match, return `"found []"`.