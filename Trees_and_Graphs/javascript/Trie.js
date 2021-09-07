class Trie {
    constructor(){
        this.trie = {};
    }

    addWord(word){
        let node = this.trie;

        for(let i=0; i< word.length; i++){
            let char = word[i];
            if(!node[char]){
                node[char] = {}
            }
            node = node[char]
        }
        node.isEnd = true
    }
    searchWord(word){
        let node = this.trie;

        for(let i=0; i< word.length; i++){
            let char = word[i];
            if(!node[char]){
                return false
            }
            node = node[char]
        }
        return node.isEnd
    }

}

let trie = new Trie()
trie.addWord('camel')
trie.addWord('camera')
trie.addWord('taylor')
trie.addWord('tape')
console.log(trie.searchWord('tape'))
console.log(trie.searchWord('taper'))
console.log(trie.trie)