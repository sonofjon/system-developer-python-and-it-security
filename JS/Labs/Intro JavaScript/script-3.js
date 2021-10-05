// Using regular expression
function countLetters(array) {
    const word = array[0];
    const letter = array[1];
    const re = new RegExp(letter, 'g');
    const matches = word.match(re);
    return matches.length;
}

output = countLetters(['hello', 'l']);
console.log(output);
output = countLetters(['panther', 'n']);
console.log(output);
