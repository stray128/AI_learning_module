from utils.checker import check
import os


def p1(passwd_exists):
    check.is_type(passwd_exists, bool, "P1: Type check")
    check.is_true(passwd_exists == os.path.exists('/etc/passwd'), "P1: Correct value")


def p2(is_file):
    check.is_type(is_file, bool, "P2: Type check")
    check.is_true(is_file == os.path.isfile('/etc/passwd'), "P2: Correct value")


def p3(filepath):
    check.file_exists(filepath, "P3: File created")
    _content = open(filepath).read()
    check.has_length(_content, 13, "P3: Content length")
    check.is_true(_content.startswith("Hello"), "P3: Content starts correctly", "Content should start with 'Hello'")


def p4(file_content):
    check.is_type(file_content, str, "P4: Type check")
    check.has_length(file_content, 13, "P4: Content length")
    check.is_true("World" in file_content, "P4: Contains expected text", "Should contain 'World'")


def p5(appended_content):
    check.is_type(appended_content, str, "P5: Type check")
    check.has_length(appended_content, 22, "P5: Content length after append")
    check.is_true("\n" in appended_content, "P5: Contains newline", "Should have a newline character")
    check.is_true("Goodbye" in appended_content, "P5: Contains appended text", "Should contain 'Goodbye'")


def p6(file_size):
    check.is_type(file_size, int, "P6: Type check")
    check.is_true(file_size > 0, "P6: Positive size", "File size should be positive")
    check.is_true(file_size == 22, "P6: Correct size", "Size should match the content length")


def p7(lines_path):
    check.file_exists(lines_path, "P7: File created")
    _lines = open(lines_path).readlines()
    check.has_length(_lines, 3, "P7: Correct number of lines")
    check.is_true(_lines[0].strip() == "Line 1", "P7: First line content", "First line should be 'Line 1'")


def p8(lines_list):
    check.is_type(lines_list, list, "P8: Type check")
    check.has_length(lines_list, 3, "P8: Correct number of elements")
    check.is_true(all('\n' not in line for line in lines_list), "P8: No newlines in elements", "Elements should not contain newline characters")
    check.is_true(lines_list[0] == "Line 1", "P8: First element", "First element should be 'Line 1'")


def p9(safe_read, temp_dir):
    _result1 = safe_read(os.path.join(temp_dir, 'hello.txt'))
    _result2 = safe_read('/nonexistent/file/path/xyz.txt')
    check.is_type(_result1, str, "P9a: Returns string for existing file")
    check.is_true(len(_result1) > 0, "P9b: Non-empty for existing file", "Should return file content")
    check.is_true(_result2 == "FILE_NOT_FOUND", "P9c: Correct return for non-existent", "Should return 'FILE_NOT_FOUND' for missing files")


def p10(count_lines, temp_dir):
    _count = count_lines(os.path.join(temp_dir, 'lines.txt'))
    check.is_type(_count, int, "P10: Returns integer")
    check.is_true(_count == 3, "P10: Correct count", "lines.txt should have 3 lines")


def p11(binary_path):
    check.file_exists(binary_path, "P11: File created")
    _size = os.path.getsize(binary_path)
    check.is_true(_size == 5, "P11: Correct size", "File should be exactly 5 bytes")
    with open(binary_path, 'rb') as _f:
        _data = _f.read()
    check.is_true(_data[0] == 0 and _data[-1] == 4, "P11: Correct byte values", "First byte should be 0, last should be 4")


def p12(mod_time):
    check.is_type(mod_time, (int, float), "P12: Type check")
    check.is_true(mod_time > 1000000000, "P12: Valid timestamp", "Should be a Unix timestamp (large positive number)")


def p13(copy_file, temp_dir):
    _src = os.path.join(temp_dir, 'hello.txt')
    _dst = os.path.join(temp_dir, 'hello_copy.txt')
    copy_file(_src, _dst)
    check.file_exists(_dst, "P13: Destination file created")
    check.is_true(os.path.getsize(_src) == os.path.getsize(_dst), "P13: Same size", "Files should have same size")
    with open(_src, 'rb') as _f1, open(_dst, 'rb') as _f2:
        check.is_true(_f1.read() == _f2.read(), "P13: Identical content", "File contents should be identical")


def p14(find_lines, temp_dir):
    _test_file = os.path.join(temp_dir, 'search_test.txt')
    with open(_test_file, 'w') as _f:
        _f.write("apple pie\nbanana bread\napple juice\norange soda")
    _result = find_lines(_test_file, 'apple')
    check.is_type(_result, list, "P14: Returns list")
    check.has_length(_result, 2, "P14: Correct number of matches")
    check.is_true(all('apple' in line for line in _result), "P14: All contain pattern", "All results should contain 'apple'")


def p15(read_chunks, temp_dir):
    _chunks = list(read_chunks(os.path.join(temp_dir, 'hello.txt'), 5))
    check.is_true(len(_chunks) > 0, "P15a: Has chunks", "Should return at least one chunk")
    check.is_true(all(len(c) <= 5 for c in _chunks), "P15b: Chunk sizes", "Each chunk should be at most 5 bytes")
    _total = sum(len(c) for c in _chunks)
    check.is_true(_total == os.path.getsize(os.path.join(temp_dir, 'hello.txt')), "P15c: Total size", "Sum of chunks should equal file size")


def p16(word_frequency, temp_dir):
    _test_file = os.path.join(temp_dir, 'words.txt')
    with open(_test_file, 'w') as _f:
        _f.write("the quick brown fox\nthe lazy dog\nthe fox jumps")
    _freq = word_frequency(_test_file)
    check.is_type(_freq, dict, "P16: Returns dictionary")
    check.is_true(_freq.get('the', 0) == 3, "P16a: 'the' count", "'the' should appear 3 times")
    check.is_true(_freq.get('fox', 0) == 2, "P16b: 'fox' count", "'fox' should appear 2 times")


def p17(merge_files, temp_dir):
    _file1 = os.path.join(temp_dir, 'merge1.txt')
    _file2 = os.path.join(temp_dir, 'merge2.txt')
    _merged = os.path.join(temp_dir, 'merged.txt')
    with open(_file1, 'w') as _f: _f.write('Content 1')
    with open(_file2, 'w') as _f: _f.write('Content 2')
    merge_files([_file1, _file2], _merged)
    check.file_exists(_merged, "P17: Output file created")
    with open(_merged) as _f:
        _result = _f.read()
    check.is_true('Content 1' in _result, "P17a: Contains first file", "Should contain 'Content 1'")
    check.is_true('Content 2' in _result, "P17b: Contains second file", "Should contain 'Content 2'")
