# ==========================================
# LAB 1: MA TRẬN, VECTOR VÀ CÁC PHÉP TOÁN
# NỀN TẢNG TRONG AI
# ==========================================


# ==========================================
# BÀI 1: CHUYỂN VỊ MA TRẬN
# ==========================================

def transpose_matrix(A):
    rows = len(A)
    cols = len(A[0])

    # Tạo ma trận chuyển vị
    A_T = [[0 for _ in range(rows)] for _ in range(cols)]

    # Hoán đổi hàng và cột
    for i in range(rows):
        for j in range(cols):
            A_T[j][i] = A[i][j]

    return A_T


print("========== BÀI 1 ==========")

A = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Ma trận A:")
for row in A:
    print(row)

print("Ma trận chuyển vị A_T:")
for row in transpose_matrix(A):
    print(row)


# ==========================================
# BÀI 2: CHUẨN VECTOR L1 VÀ L2
# ==========================================

def norm_l1(v):
    total = 0

    for x in v:
        total += abs(x)

    return total


def norm_l2(v):
    sum_sq = 0

    for x in v:
        sum_sq += x ** 2

    return sum_sq ** 0.5


print("\n========== BÀI 2 ==========")

error_vector = [3, -4]

print("Vector:", error_vector)
print("L1 Norm:", norm_l1(error_vector))
print("L2 Norm:", norm_l2(error_vector))


# ==========================================
# BÀI 3: NHÂN MA TRẬN VỚI VECTOR
# ==========================================

def matrix_vector_multiply(W, x):

    rows = len(W)
    cols = len(W[0])

    # Kiểm tra kích thước
    if cols != len(x):
        print("Lỗi: Số cột của W phải bằng số phần tử của x.")
        return None

    # Tạo vector kết quả
    y = [0] * rows

    # Tính W * x
    for i in range(rows):
        for j in range(cols):
            y[i] += W[i][j] * x[j]

    return y


print("\n========== BÀI 3 ==========")

W = [
    [0.2, 0.5, -0.1],
    [0.8, -0.3, 0.4]
]

x = [10, 2, 5]

y = matrix_vector_multiply(W, x)

print("Ma trận W:")
for row in W:
    print(row)

print("Vector x:", x)
print("Kết quả y = W * x:", y)


# ==========================================
# BÀI 4: NHÂN HAI MA TRẬN
# ==========================================

def matrix_multiply(A, B):

    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    # Kiểm tra điều kiện nhân ma trận
    if cols_A != rows_B:
        print("Lỗi: Số cột của A phải bằng số hàng của B.")
        return None

    # Tạo ma trận kết quả
    C = [
        [0 for _ in range(cols_B)]
        for _ in range(rows_A)
    ]

    # Đếm số phép nhân
    multiplication_count = 0

    # 3 vòng lặp
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):

                C[i][j] += A[i][k] * B[k][j]

                multiplication_count += 1

    print("Tổng số phép nhân:", multiplication_count)

    return C


print("\n========== BÀI 4 ==========")

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 1],
    [2, 3]
]

C = matrix_multiply(A, B)

print("Ma trận A:")
for row in A:
    print(row)

print("Ma trận B:")
for row in B:
    print(row)

print("Ma trận C = A * B:")
for row in C:
    print(row)


# ==========================================
# BÀI 5: KHỬ GAUSS
# ==========================================

def gaussian_elimination(aug_matrix):

    # Tạo bản sao của ma trận
    matrix = [row[:] for row in aug_matrix]

    rows = len(matrix)
    cols = len(matrix[0])

    # Duyệt qua từng cột
    for k in range(min(rows, cols - 1)):

        # ------------------------------
        # PARTIAL PIVOTING
        # ------------------------------

        max_row = k

        for i in range(k + 1, rows):

            if abs(matrix[i][k]) > abs(matrix[max_row][k]):
                max_row = i

        # Hoán đổi dòng
        if max_row != k:
            matrix[k], matrix[max_row] = matrix[max_row], matrix[k]

        # Nếu pivot bằng 0 thì bỏ qua
        if abs(matrix[k][k]) < 1e-10:
            continue

        # ------------------------------
        # FORWARD ELIMINATION
        # ------------------------------

        for i in range(k + 1, rows):

            factor = matrix[i][k] / matrix[k][k]

            for j in range(k, cols):

                matrix[i][j] -= factor * matrix[k][j]

        # Làm tròn 2 chữ số
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = round(matrix[i][j], 2)

    return matrix


print("\n========== BÀI 5 ==========")

augmented_matrix = [
    [2.0, 1.0, -1.0, 8.0],
    [-3.0, -1.0, 2.0, -11.0],
    [-2.0, 1.0, 2.0, -3.0]
]

print("Ma trận bổ sung ban đầu:")

for row in augmented_matrix:
    print(row)

result = gaussian_elimination(augmented_matrix)

print("\nMa trận sau khi khử Gauss:")

for row in result:
    print(row)


# Độ phức tạp thời gian:
# O(n^3)