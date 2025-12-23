# Module 1: Python OS Module

Master file system operations - an essential skill for any data scientist working with real-world data pipelines.

## What You'll Learn

This module covers Python's `os` module for interacting with the operating system. These skills are fundamental for:
- Automating data ingestion from multiple files
- Building ETL pipelines
- Managing project directories programmatically
- Creating reproducible data workflows

## Notebooks

### 1. File Operations (`01_file_operations.ipynb`)
**Problems:** 15 | **Difficulty:** Easy to Medium

Learn to read, write, and manage files programmatically:
- Reading and writing text files
- Working with file modes (read, write, append)
- Using context managers (`with` statements) for safe file handling
- Reading files line by line for memory efficiency
- Checking file existence and properties

**Practical Application:** Automate log file processing, configuration management, and batch data imports.

---

### 2. Directory & Path Operations (`02_directory_paths.ipynb`)
**Problems:** 15 | **Difficulty:** Easy to Medium

Navigate and manipulate the file system:
- Getting and changing the current working directory
- Creating and removing directories
- Listing directory contents
- Building cross-platform file paths with `os.path.join()`
- Extracting file names, extensions, and parent directories

**Practical Application:** Build data pipelines that work across Windows, Mac, and Linux systems.

---

### 3. System & Environment (`03_system_environment.ipynb`)
**Problems:** 15 | **Difficulty:** Medium to Hard

Interact with system-level features:
- Accessing and setting environment variables
- Getting system information (platform, user, etc.)
- Working with file metadata (size, modification time)
- Walking directory trees recursively
- Pattern matching with file paths

**Practical Application:** Create environment-aware applications and automate file discovery across complex directory structures.

---

## Prerequisites

- Basic Python knowledge (variables, loops, functions)
- Understanding of file systems and directories

## Getting Started

1. Open `01_file_operations.ipynb` in Jupyter
2. Run the setup cell at the top
3. Read each problem's concept and syntax sections
4. Write your solution in the provided cell
5. Run the verification cell to check your answer

## Tips for Success

- Always use `os.path.join()` instead of hardcoding path separators
- Use context managers (`with open(...) as f:`) to ensure files are properly closed
- Test your code with both existing and non-existing files to understand error handling
