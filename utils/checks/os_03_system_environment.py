from utils.checker import check
import os


def p1(home_dir):
    check.is_type(home_dir, str, "P1: Type check")
    check.is_true(home_dir.startswith('/'), "P1: Is absolute path", "HOME should be an absolute path")
    check.is_true(home_dir == os.environ.get('HOME'), "P1: Correct value")


def p2(path_list):
    check.is_type(path_list, list, "P2a: Type check")
    check.is_true(len(path_list) > 0, "P2b: Has elements", "PATH should contain directories")


def p3(retrieved_value):
    check.is_type(retrieved_value, str, "P3: Type check")
    check.is_true(retrieved_value == "hello_world", "P3: Correct value", "Should be 'hello_world'")


def p4(result):
    check.is_type(result, str, "P4: Type check")
    check.is_true(result == "default_value", "P4: Got default", "Should return the default value")


def p5(os_name):
    check.is_type(os_name, str, "P5: Type check")
    check.is_true(os_name in ['posix', 'nt'], "P5: Valid OS name", "Should be 'posix' or 'nt'")


def p6(pid):
    check.is_type(pid, int, "P6: Type check")
    check.is_true(pid > 0, "P6: Positive PID", "PID should be a positive integer")


def p7(new_path, old_path):
    check.file_exists(new_path, "P7a: New file exists")
    check.is_false(os.path.exists(old_path), "P7b: Old file removed", "Old file should no longer exist")


def p8(delete_path):
    check.is_false(os.path.exists(delete_path), "P8: File deleted", "File should no longer exist")


def p9(env_count):
    check.is_type(env_count, int, "P9: Type check")
    check.is_true(env_count > 5, "P9: Has many vars", "Should have more than 5 environment variables")


def p10(cpu_count):
    check.is_type(cpu_count, int, "P10: Type check")
    check.is_true(cpu_count >= 1, "P10: At least 1 CPU", "Should have at least 1 CPU")


def p11(empty_dir):
    check.is_false(os.path.exists(empty_dir), "P11: Directory removed", "Directory should no longer exist")


def p12(find_env_vars):
    _path_vars = find_env_vars('PATH')
    check.is_type(_path_vars, list, "P12a: Returns list")
    check.is_true(len(_path_vars) > 0, "P12b: Found matches", "Should find variables containing 'PATH'")
    check.is_true(all('path' in v.lower() for v in _path_vars), "P12c: All match pattern", "All results should contain 'PATH'")


def p13(safe_delete, temp_dir):
    _test_file = os.path.join(temp_dir, 'safe_del_test.txt')
    with open(_test_file, 'w') as f: f.write('test')
    _result1 = safe_delete(_test_file)
    _result2 = safe_delete(_test_file)  # Already deleted
    check.is_true(_result1 == True, "P13a: Deleted existing", "Should return True for existing file")
    check.is_true(_result2 == False, "P13b: Non-existent", "Should return False for non-existent file")


def p14(TempEnvVar):
    _original = os.environ.get('TEST_TEMP_VAR_14')
    with TempEnvVar('TEST_TEMP_VAR_14', 'temporary_value'):
        _inside_value = os.environ.get('TEST_TEMP_VAR_14')
    _after_value = os.environ.get('TEST_TEMP_VAR_14')
    check.is_true(_inside_value == 'temporary_value', "P14a: Inside context", "Should be 'temporary_value' inside")
    check.is_true(_after_value == _original, "P14b: Restored after", "Should restore original value")


def p15(expand_path):
    _result = expand_path('~/test')
    check.is_type(_result, str, "P15: Type check")
    check.is_true(_result.startswith('/'), "P15a: Is absolute", "Should start with '/'")
    check.is_true('~' not in _result, "P15b: No tilde", "Should not contain '~'")


def p16(get_system_info):
    _info = get_system_info()
    check.is_type(_info, dict, "P16a: Returns dict")
    check.is_true('os_name' in _info, "P16b: Has os_name", "Should have 'os_name' key")
    check.is_true('cpu_count' in _info, "P16c: Has cpu_count", "Should have 'cpu_count' key")
    check.is_true('pid' in _info, "P16d: Has pid", "Should have 'pid' key")
    check.is_true('cwd' in _info, "P16e: Has cwd", "Should have 'cwd' key")
    check.is_true('home' in _info, "P16f: Has home", "Should have 'home' key")
