from utils.checker import check
import numpy as np

def p1(arr):
    check.array_equal(arr, np.array([1, 2, 3, 4, 5]), "Problem 1")

def p2(arr_range):
    check.array_equal(arr_range, np.arange(10), "Problem 2")

def p3(zeros_arr):
    check.array_equal(zeros_arr, np.zeros(5), "Problem 3")

def p4(ones_arr):
    check.shape_equal(ones_arr, (3, 4), "Problem 4a")
    check.array_equal(ones_arr, np.ones((3, 4)), "Problem 4b")

def p5(arr_shape):
    check.equal(arr_shape, (2, 3), "Problem 5")

def p6(float_arr):
    check.dtype_equal(float_arr, np.float64, "Problem 6a")
    check.array_close(float_arr, np.array([1., 2., 3., 4., 5.]), "Problem 6b")

def p7(lin_arr):
    check.length_equal(lin_arr, 5, "Problem 7a")
    check.array_close(lin_arr, np.array([0., 0.25, 0.5, 0.75, 1.]), "Problem 7b")

def p8(identity):
    check.shape_equal(identity, (4, 4), "Problem 8a")
    check.array_equal(identity, np.eye(4), "Problem 8b")

def p9(reshaped):
    check.shape_equal(reshaped, (3, 4), "Problem 9a")
    check.equal(reshaped[0, 0], 0, "Problem 9b")
    check.equal(reshaped[2, 3], 11, "Problem 9c")

def p10(full_arr):
    check.shape_equal(full_arr, (2, 3), "Problem 10a")
    check.is_true(np.all(full_arr == 7), "Problem 10b", "All values should be 7")

def p11(arr_3d):
    check.shape_equal(arr_3d, (2, 3, 4), "Problem 11a")
    check.is_true(np.all(arr_3d[0] == 1), "Problem 11b", "First page should be all 1s")
    check.is_true(np.all(arr_3d[1] == 0), "Problem 11c", "Second page should be all 0s")

def p12(flat_arr):
    check.ndim_equal(flat_arr, 1, "Problem 12a")
    check.array_equal(flat_arr, np.array([1, 2, 3, 4, 5, 6]), "Problem 12b")

def p13(step_arr):
    check.array_equal(step_arr, np.array([10, 15, 20, 25, 30, 35, 40, 45]), "Problem 13")

def p14(converted):
    check.dtype_equal(converted, np.float32, "Problem 14")

def p15(v_stack, h_stack):
    check.shape_equal(v_stack, (2, 3), "Problem 15a - vstack shape")
    check.length_equal(h_stack, 6, "Problem 15b - hstack length")
