# Scenario

Your task is to implement a simplified version of a file hosting service.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press “Submit” often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the entire question before coding. Implement the operations one by one. You may need to refactor your code to
support additional functionality in later levels. Do not change the existing method signatures.

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
  - If the destination file already exists, overwrite the existing file.
