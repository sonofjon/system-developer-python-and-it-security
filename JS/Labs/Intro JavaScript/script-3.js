// Using regular expression
function countLetters(array) {
    const word = array[0];
    const letter = array[1];
    const re = new RegExp(letter, 'g');
    const matches = word.match(re);
    return matches.length;
}

// Using forEach
function countLetters2(array) {

    function sumArray(total, value) {
        return total + value;
    };

    const word = array[0];
    const letter = array[1];
    // const charArray = array.split("");
    let sum = numbers.reduce(sumArray, 0);
}

// output = countLetters(['hello', 'l']);
// console.log(output);
// output = countLetters(['panther', 'n']);
// console.log(output);

output = countLetters2(['hello', 'l']);
console.log(output);
output = countLetters2(['panther', 'n']);
console.log(output);

try {

} catch (error) {

}
