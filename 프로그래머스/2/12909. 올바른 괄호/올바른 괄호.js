function solution(s){
    var answer = true;
    let stack = []
    for (let i=0; i<s.length;i++){
        if(s[i] === '('){
            stack.push('(')
        } else {
            if(stack.length ===0 || stack.pop() !== '('){
                return false;
            }
        }
    }

    return stack.length === 0;
}