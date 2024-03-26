function solution(sizes) {
    var answer = 0;
    let max_height = 0
    let max_width = 0
    for (size of sizes){
        let width = Math.max(size[0],size[1])
        max_width = Math.max(max_width, width)
        
        let height = Math.min(size[0],size[1])
        max_height = Math.max(max_height, height)
    }
    return max_width*max_height
}
