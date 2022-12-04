function printRNG() {
    ids = ['x1','x2','x3','x4']

    for(var i = 0; i < ids.length; i++) { 
        num = Math.random()
        p = document.getElementById(ids[i])
        p.innerHTML = num
    } 
}

setInterval(printRNG, 3000)