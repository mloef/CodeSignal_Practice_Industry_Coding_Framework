# Scenario

Your task is to implement a simplified version of a file hosting service.
All operations that should be supported are listed below.

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
