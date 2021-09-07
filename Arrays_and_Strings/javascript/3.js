
function urlify(string, trueLength) {
    let url = string.split("")
    for(let i=0; i< trueLength; i++){
        if(url[i] == ' '){
            url[i] = '%20'
        }
    }
    return url.join('');
}

console.log(urlify("Mr John Smith ",13))
console.log(urlify("Mr John  Smith ",14))
console.log(urlify("Mr John Smith ",13))
console.log(urlify("Mr John Smith ",13))
console.log(urlify("Mr John Smith ",13))

