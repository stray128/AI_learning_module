from utils.checker import check
import os


def p1(cwd):
    check.is_type(cwd, str, "P1: Type check")
    check.is_true(cwd.startswith('/'), "P1: Is absolute path", "Path should start with '/'")
    check.is_true(cwd == os.getcwd(), "P1: Correct value")


def p2(new_dir):
    check.dir_exists(new_dir, "P2: Directory created")


def p3(dir_contents):
    check.is_type(dir_contents, list, "P3a: Type check")
    check.contains(dir_contents, 'test_folder', "P3b: Contains test_folder")


def p4(is_directory):
    check.is_type(is_directory, bool, "P4: Type check")
    check.is_true(is_directory, "P4: Is a directory", "test_folder should be a directory")


def p5(joined_path):
    check.is_type(joined_path, str, "P5: Type check")
    check.is_true(joined_path.startswith('/home'), "P5a: Starts correctly", "Should start with '/home'")
    check.is_true(joined_path.endswith('file.txt'), "P5b: Ends correctly", "Should end with 'file.txt'")
    check.is_true('documents' in joined_path, "P5c: Contains documents", "Should contain 'documents'")


def p6(filename):
    check.is_type(filename, str, "P6: Type check")
    check.is_true('/' not in filename, "P6a: No path separators", "Should not contain '/'")
    check.is_true(filename.endswith('.pdf'), "P6b: Has extension", "Should end with '.pdf'")


def p7(dir_path):
    check.is_type(dir_path, str, "P7: Type check")
    check.is_true(dir_path.endswith('documents'), "P7a: Ends with directory", "Should end with 'documents'")
    check.is_true('report.pdf' not in dir_path, "P7b: No filename", "Should not contain filename")


def p8(name, ext):
    check.is_type(name, str, "P8a: Name type check")
    check.is_type(ext, str, "P8b: Ext type check")
    check.is_true('.' not in name, "P8c: Name has no dot", "Name should not contain dot")
    check.is_true(ext.startswith('.'), "P8d: Ext starts with dot", "Extension should start with dot")


def p9(nested_path):
    check.dir_exists(nested_path, "P9: Nested directories created")


def p10(abs_path):
    check.is_type(abs_path, str, "P10: Type check")
    check.is_true(abs_path.startswith('/'), "P10a: Is absolute", "Should start with '/'")
    check.is_true(abs_path.endswith('test_folder'), "P10b: Ends correctly", "Should end with 'test_folder'")


def p11(list_files, temp_dir):
    # Create test files first
    with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f: f.write('test')
    with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f: f.write('test')
    _files = list_files(temp_dir)
    check.is_type(_files, list, "P11a: Returns list")
    check.contains(_files, 'file1.txt', "P11b: Contains file1.txt")
    check.not_contains(_files, 'test_folder', "P11c: No directories")


def p12(list_directories, temp_dir):
    _dirs = list_directories(temp_dir)
    check.is_type(_dirs, list, "P12a: Returns list")
    check.contains(_dirs, 'test_folder', "P12b: Contains test_folder")
    check.not_contains(_dirs, 'file1.txt', "P12c: No files")


def p13(find_by_extension, temp_dir):
    _txt_files = find_by_extension(temp_dir, '.txt')
    check.is_type(_txt_files, list, "P13a: Returns list")
    check.is_true(len(_txt_files) >= 2, "P13b: Found txt files", "Should find at least 2 .txt files")
    check.is_true(all(f.endswith('.txt') for f in _txt_files), "P13c: All have .txt extension", "All files should end with .txt")


def p14(count_all_files, temp_dir):
    # Create a nested file for testing
    _nested_file = os.path.join(temp_dir, 'level1', 'nested_file.txt')
    with open(_nested_file, 'w') as f: f.write('nested')
    _count = count_all_files(temp_dir)
    check.is_type(_count, int, "P14a: Returns integer")
    check.is_true(_count >= 3, "P14b: Found multiple files", "Should find at least 3 files (including nested)")


def p15(find_all_files, temp_dir):
    _all_txt = find_all_files(temp_dir, '.txt')
    check.is_type(_all_txt, list, "P15a: Returns list")
    check.is_true(any('nested_file.txt' in f for f in _all_txt), "P15b: Found nested file", "Should find nested_file.txt")
    check.is_true(all(f.endswith('.txt') for f in _all_txt), "P15c: All are .txt files", "All results should be .txt files")


def p16(get_dir_size, temp_dir):
    _size = get_dir_size(temp_dir)
    check.is_type(_size, int, "P16a: Returns integer")
    check.is_true(_size > 0, "P16b: Has positive size", "Directory should have files with size > 0")


def p17(mirror_structure, temp_dir):
    _mirror_dir = os.path.join(temp_dir, 'mirror')
    mirror_structure(os.path.join(temp_dir, 'level1'), _mirror_dir)
    check.dir_exists(os.path.join(_mirror_dir, 'level2'), "P17a: level2 mirrored")
    check.dir_exists(os.path.join(_mirror_dir, 'level2', 'level3'), "P17b: level3 mirrored")
