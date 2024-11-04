def solution(sequence, k):
    n = len(sequence)

    tot_sum = 0
    end = 0
    length = n

    for start in range(n):
        while tot_sum < k and end < n:
            tot_sum += sequence[end]
            end += 1

        if tot_sum == k and end - 1 - start < length:
            ans = [start, end - 1]
            length = end - 1 - start
        tot_sum -= sequence[start]


    return ans