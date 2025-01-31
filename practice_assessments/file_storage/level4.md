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

(Definitions as above.)

## Level 2 – Data Structures & Data Processing

(Definitions as above.)

## Level 3 – Refactoring & Encapsulation

(Definitions as above.)

## Level 4 – Extending Design & Functionality

- **ROLLBACK(timestamp)**
  - Rollback the state of the file storage to the state at the specified timestamp.
  - All TTLs should be recalculated relative to the rollback timestamp.
  - Return `"rollback to <timestamp>"`.