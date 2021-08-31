
function isUniqueCharacters(word) {
    let map = new Set()

    for(let i=0; i< word.length; i++){
        char = word[i]
        if(!map.has(char)){
            map.add(char)
        } else {
            return false
        }
    }
    return true;
}

console.log(isUniqueCharacters("hello"))
console.log(isUniqueCharacters("hi"))
console.log(isUniqueCharacters("tale"))
console.log(isUniqueCharacters("straw"))
console.log(isUniqueCharacters("people"))

