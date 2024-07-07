function dfs(k,dungeons,visit,index,answer,resultArr){

    for(let a=0;a<dungeons.length;a++){
        if((!visit[a])&&(k>=dungeons[a][0])){   
            resultArr.push(answer+1);
            k-=dungeons[a][1];
            visit[a]=1;
            dfs(k,dungeons,visit,a+1,answer+1,resultArr);
            visit[a]=0;
            k+=dungeons[a][1];

        }
    }


}
function solution(k, dungeons) {
    var answer = 0;
    let index=0;
    const result=[];
    const visit=Array(dungeons.length).fill(0);

    dfs(k,dungeons,visit,index,answer,result);
  answer= Math.max(...result);

    return answer;
}