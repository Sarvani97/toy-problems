function deepEqual(a,b) {
    if(a === b) {
        return true
    }
    if(a == null || typeof a != "object" || b == null || typeof b != "object") {
        return false
    }
    var cntA = 0, cntB = 0;
    for(var i in a) {
        cntA++;
    }
    for(var i in b) {
        cntB++;

        if(!(i in a) || !deepEqual(a[i],b[i])) {
            return false
        }
    }
    return cntA === cntB

}

var obj = {s:1}
//we can't compare {s:1} to its reference using equality operator.
//it returns true only when they refer to the same location in memory.
console.log(deepEqual ({s:1}, obj))

var o2 = {here: {is: "an"}, object: 2};
console.log(deepEqual(o2, {here: 1, object: 2}));
console.log(deepEqual(o2,o2))
