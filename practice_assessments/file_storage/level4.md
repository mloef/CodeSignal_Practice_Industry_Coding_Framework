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

## Level 3 – Refactoring & Encapsulation

File operations now have timestamps. Timestamps never decrease over the sequence. File uploads may have a specified time-to-live (TTL). Your system should continue to pass tests for levels 1 and 2. However, tests for levels 3 and 4 will only use timestamped operations.

- **FILE_UPLOAD_AT(timestamp, file_name, file_size, [ttl])**
  - Upload the file at the given timestamp.
  - Return `"uploaded <file_name>"` on success.
  - With a TTL, the file expires after the specified number of seconds.
  - If the file exists, return `"error: file already exists"`.

- **FILE_GET_AT(timestamp, file_name)**
  - Return `"got <file_name>"` if the file is available at the given timestamp.
  - If not found or expired, return `"file not found"`.

- **FILE_COPY_AT(timestamp, file_from, file_to)**
  - Copy the file at the given timestamp.
  - Return `"copied <file_from> to <file_to>"` on success.
  - The new file is considered to have been written at the given timestamp.
  - If the old file had a TTL, the new file expires at the same time.
  - If the source is not found or expired, return `"error: source file not found"`.

- **FILE_SEARCH_AT(timestamp, prefix)**
  - Return `"found [file1, file2, ...]"` for files that are alive at the given timestamp.

## Level 4 – Extending Design & Functionality

- **ROLLBACK(timestamp)**
  - Rollback the state of the file storage to the state at the specified timestamp.
  - Return `"rollback to <timestamp>"`.
