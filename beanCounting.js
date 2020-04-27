//traditional approach
function countBs(str) {
    var cnt = 0
    for(var i = 0; i < str.length; i++) {
        if(str.charAt(i) == "B") {
            cnt += 1
        }
    }
    return cnt
}

//using the method match() - searches a string for a match against a regular exp, and returns the matches as an array object. We should 
//include the g modifier(global search) to search the whole string or else it will only return the first occurrence.

var countBsNew = function(str) {
    return str.match(/B/g).length
}

function countChar(str,c) {
    var cnt = 0
    for(var i = 0; i < str.length; i++) {
        if(str.charAt(i) == c) {
            cnt += 1
        }
    }
    return cnt
}

console.log(countBs("BBB"))
console.log(countBsNew("BBB"))
console.log(countChar("sscca","a"))