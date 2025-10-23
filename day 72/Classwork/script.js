function fibonacci(n){
    let sequence=[0,1]
    for(let i = 2 ; i < n ; i++) {
        let newValue = sequence[i-1] + sequence[i-2]
        sequence.push(newValue);
    }
    return sequence;
}
console.log(fibonacci(5)) // 0, 1, 2, 3, 5