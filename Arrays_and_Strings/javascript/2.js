
function isPermuation(word1, word2) {
    if(word1.length != word2.length){
        return false
    }
    let map = new Set()

    for(let i=0; i< word1.length; i++){
        char = word1[i]
        char2 = word2[i]

        if(!map.has(char)){
            map.add(char)
        } else {
            map.delete(char)
        }

        if(!map.has(char2)){
            map.add(char2)
        } else {
            map.delete(char2)
        }
    }
    return map.size == 0;
}

console.log(isPermuation("hello","helol"))
console.log(isPermuation("tello","helol"))
console.log(isPermuation("hellp","helpl"))
console.log(isPermuation("hello","helol"))
console.log(isPermuation("hello","heloL"))

