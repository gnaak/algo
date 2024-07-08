function solution(gs, ps) {
    var answer = [];
    let gSort = new Map()
    const eg = {}
    for (let i = 0; i< gs.length; i++){
        gSort.set(gs[i], (gSort.get(gs[i])||0) + ps[i])
        if (!eg[gs[i]]) eg[gs[i]] = []
        eg[gs[i]].push({plays: ps[i], idx : i})
    }
    gSort = [...gSort].sort((a,b)=> b[1]-a[1])
    for (s of gSort){
        // console.log(s[0]) 'pop' , 'classic'
        for (let i=0; i< Math.min(2, eg[s[0]].length); i++){
            eg[s[0]].sort((a,b)=> b.plays - a.plays)
            answer.push(eg[s[0]][i].idx)
        }
    }
    return answer;
}