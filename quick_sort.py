#  Hoare partition scheme

# def swap(a, b, arr):
#     if a != b:
#         tmp = arr[a]
#         arr[a] = arr[b]
#         arr[b] = tmp
#
#
# def partition(elements, start, end):
#     pivot_index = start
#     pivot = elements[pivot_index]
#
#     while start < end:
#         while start < len(elements) and elements[start] <= pivot:
#             start += 1
#
#         while elements[end] > pivot:
#             end -= 1
#
#         if start < end:
#             swap(start, end, elements)
#     swap(pivot_index, end, elements)
#
#     return end
#
# def quick_sort(elements, start, end):
#     if start < end:
#         pi = partition(elements, start, end)
#         quick_sort(elements, start, pi - 1)     # Left Side
#         quick_sort(elements, pi+1, end)         # Right Side
#
# if __name__ == '__main__':
#     elements = [11, 9, 29, 7, 2, 15, 28]
#     quick_sort(elements, 0, len(elements) - 1)
#     print (elements)


# Lomuto partition scheme


def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start, end):
    pivot = elements[end]
    pivot_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, pivot_index, elements)
            pivot_index += 1
    swap(pivot_index, end, elements)
    return pivot_index


def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)  # Left Side
        quick_sort(elements, pi + 1, end)  # Right Side


def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    elements = [[10, 7, 8, 9, 1, 5],
                [15, 2, 5, 1243, 23, 29],
                [234,35,24,8676,246,3465,73,43,2456,45353,54554,46,65]]
    for i in elements:
        quick_sort(i, 0, len(i) - 1)
        print(i)
