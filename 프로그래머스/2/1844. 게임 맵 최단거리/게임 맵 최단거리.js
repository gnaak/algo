function solution(maps) {
    const rows = maps.length
    const cols = maps[0].length
    const dx = [1,0,-1,0]
    const dy = [0,1,0,-1]
    
    const queue = [[0,0,1]]
    // 시작 지점 표시
    maps[0][0] = 0 
    
    while (queue.length > 0){
        const [x, y , dist] = queue.shift()
        
        if(x===cols-1 && y===rows-1){
            return dist
        }
        
        for (let i = 0; i<4;i++){
            const nx = x + dx[i]
            const ny = y + dy[i]
            
            if (nx >=0 && ny>= 0 && nx <cols && ny < rows && maps[ny][nx] ===1){
                queue.push([nx, ny, dist +1])
                maps[ny][nx] = 0
            }
        }
    }
    return -1 
}