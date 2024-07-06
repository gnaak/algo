function solution(clothes) {
    var answer = 1;
    const closet = new Map()
    for (cloth of clothes){
        const [style, type] = cloth
        closet.set(type, (closet.get(type)||0)+1)

    }
    for (count of closet.values()){
        answer *= (count+1)
    }
    --answer
    return answer;
}