function calcVat(strings) {

    function sumArray(total, value) {
        return total + value;
    };

    let numbers = strings.map(Number);
    let sum = numbers.reduce(sumArray);
    let vat = 0.20 * sum; 
    let total = sum + vat; 

    console.log(`sum = ${sum}`);
    console.log(`VAT = ${vat.toFixed(2)}`);
    console.log(`total = ${total.toFixed(2)}`);
}

calcVat(['1.20', '2.60', '3.50']);
calcVat(['3.12', '5', '18', '19.24', '1953.2262',
'0.001564', '1.1445']);