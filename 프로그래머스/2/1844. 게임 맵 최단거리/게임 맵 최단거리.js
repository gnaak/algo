class Queue {
  constructor() {

    this.items = [];
  }

  enqueue(item) {
    this.items.push(item);
  }

  dequeue() {
    return this.items.shift();
  }

  peek() {
    return this.items[0];
  }

  getSize() {
    return this.items.length;
  }

  isEmpty() {
    return this.getSize() === 0;
  }
}

function solution(maps) {

    const dx=[0,1,0,-1];
    const dy=[1,0,-1,0];
    const width=maps[0].length;
    const height=maps.length;
    const visit=Array.from({length:height},()=>Array(width).fill(0));
    function bfs(){
        const queue=new Queue();
        queue.enqueue([0,0]);

        while(!queue.isEmpty()){

            const [x,y]= queue.dequeue();



            if((x===height-1)&&(y===width-1))return visit[x][y]+1;
            for(let a=0;a<4;a++){
             let newX=x+dx[a];
             let newY=y+dy[a]; 

                if (newX < 0 || newY < 0 || newX >= height || newY >= width || maps[newX] === undefined || maps[newX][newY] === undefined || maps[newX][newY] === 0) {
    continue;
}
                if(visit[newX][newY]===0){
                     visit[newX][newY]=visit[x][y]+1;
              //      console.log('newX newY',newX,newY);
             queue.enqueue([newX,newY]);  
                }


            }

        }
        return -1;
    }
    return bfs();
}