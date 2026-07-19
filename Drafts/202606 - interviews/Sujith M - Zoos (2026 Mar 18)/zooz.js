process.stdin.resume();
process.stdin.setEncoding("utf-8");

let input = "";
process.stdin.on("data", function(chunk) {
    input += chunk;
});

process.stdin.on("end", function() {
    let s = input.trim();

    let z = 0;
    let o = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === 'z') z++;
        else if (s[i] === 'o') o++;
    }

    if (o === 2 * z) {
        console.log("Yes");
    } else {
        console.log("No");
    }
});