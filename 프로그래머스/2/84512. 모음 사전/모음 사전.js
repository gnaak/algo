function solution(word) {
    var answer = 0;
    const vowels = ['A','E','I','O','U'];
    const words = []
    
    function create(current){
        if (current.length ===5){
            return
        }
        for (vowel of vowels){
            words.push(current+vowel)
            create(current+vowel)
        }
    }
    create("");
    words.sort()
    return words.indexOf(word)+1
}