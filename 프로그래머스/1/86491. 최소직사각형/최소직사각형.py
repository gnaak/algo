def solution(sizes):
    max_height = max_width = 0
    for size in sizes:
        width = max(size)
        max_width = max(max_width,width)
        
        height = min(size)
        max_height = max(max_height, height)
        
        
    return max_width*max_height