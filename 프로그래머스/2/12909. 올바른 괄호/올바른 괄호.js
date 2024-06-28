function solution(s){
    let check = 0 
    for(const ob1 of s){
        if (ob1 == '('){
            check ++
        }
        else{
            if(check){
                check --;
            }else{
                return false
            }
        }
    }
    if (!check){
        return true
    } else{
        return false
    }
}