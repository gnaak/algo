function solution(s) {
    var answer = []
    let zero = 0
    let cnt = 0
    while (s!='1'){
        let str = ''
        for(let i =0; i<s.length;i++){
            if(s[i]=='0'){
                zero++
            }
            else{
            str += s[i]
        }}

        str = (str.length).toString(2);
        cnt ++
        s = str
    }
    answer =[cnt, zero]
    return answer;
}

// function solution(s) {
//     let answer = [];
//     let count = 0;
//     let zero_count = 0;


//     while(s !== '1') {
//         let str = '';

//         for(let i=0; i<s.length; i++) {
//             if(s[i] == '0') {
//                 zero_count += 1;
//             } else {
//                 str += s[i];
//             }
//         }

//         count += 1;

//         str = (str.length).toString(2);

//         s = str;
//     }

//     answer = [count, zero_count]

//     return answer;
// }
