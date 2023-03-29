function printRNG() {
    inputs = ['x1','x2','x3','x4']

    for(var i = 0; i < inputs.length; i++) { 
        num = Math.random()
        p = document.getElementById(inputs[i])
        p.innerHTML = num
    } 
}

setInterval(printRNG, 1000)