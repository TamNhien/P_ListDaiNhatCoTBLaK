def doan_list_trung_binh_k(L, k):
    max_length = 0
    result = []

    for i in range(len(L)):
        sum_sublist = 0
        sublist_length = 0

        for j in range(i, len(L)):
            sum_sublist += L[j]
            sublist_length += 1

            if sum_sublist / sublist_length == k and sublist_length > max_length:
                max_length, result = sublist_length, L[i:j+1]

    return result

# Ví dụ sử dụng:
L = [1, 2, 3, 4, 5, 3, 2, 1, 4, 6, 8]
k = 3
result = doan_list_trung_binh_k(L, k)
print("Đoạn list dài nhất có giá trị trung bình là", k, ":", result)

