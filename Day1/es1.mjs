import fs from 'fs';
import readline from 'readline';

const filePath = 'input.txt';
let rt = 0
let rt1 = 0
const digits = new Map([
    [1, 'one'],
    [2, 'two'],
    [3, 'three'],
    [4, 'four'],
    [5, 'five'],
    [6, 'six'],
    [7, 'seven'],
    [8, 'eight'],
    [9, 'nine']
]);

// Create new reading interface
const rl = readline.createInterface({
  input: fs.createReadStream(filePath),
  output: process.stdout,
  terminal: false
});

// New line event
rl.on('line', (line) => {
    rt1 += findDigit(line)
   rt += findDigit2(line)
});

//Close file event
rl.on('close', () => {
    console.log("The sum of all of the calibration values, part one: ", rt1)
    console.log("The sum of all of the calibration values, part two: ", rt)
});

function findDigit(line){
    let digitToConvert
    let first = -1
    let last = -1
    let charArray = line.split("")
    charArray.forEach(function (e, i) {
        if(!isNaN(parseInt(e))){
            if(first == -1){
                first = i
            } else {
                last = i
            }
        }
    })
    
    let firstDigitChar = charArray[first]
    let lastDigitChar = ""
    last != -1 ? lastDigitChar = charArray[last] : lastDigitChar = firstDigitChar
    last == -1 ? last = first : first = first
    digitToConvert = firstDigitChar.concat(lastDigitChar)

    return parseInt(digitToConvert)
}

function findDigit2(line) {
    const digits2 = new Map([
        [1, { text: 'one', indices: [] }],
        [2, { text: 'two', indices: [] }],
        [3, { text: 'three', indices: [] }],
        [4, { text: 'four', indices: [] }],
        [5, { text: 'five', indices: [] }],
        [6, { text: 'six', indices: [] }],
        [7, { text: 'seven', indices: [] }],
        [8, { text: 'eight', indices: [] }],
        [9, { text: 'nine', indices: [] }]
    ]);

    let charArray = line.split("");
    charArray.forEach(function (e, i) {
      if (!isNaN(parseInt(e))) {
        const digit = parseInt(e);
        const digitInfo = digits2.get(digit);
        digitInfo.indices.push(i);
        digits2.set(digit, digitInfo);
      }
    });

    digits2.forEach((value, key) => {
        let startIndex = 0;
        const searchStrLen = value.text.length;
      
        let index;
        while ((index = line.indexOf(value.text, startIndex)) > -1) {
          value.indices.push(index);
          startIndex = index + searchStrLen;
        }
      });

    let firstDigit = {text: "", index: 99999999999999999}, lastDigit= {text: "", index: -1}

    digits2.forEach((value, key) =>{
        value.indices.forEach((i) => {
            i < firstDigit.index ? (firstDigit.index = i, firstDigit.text = key.toString()) : ""
            i > lastDigit.index ? (lastDigit.index = i, lastDigit.text = key.toString()) : ""
        })
    })

    return parseInt(firstDigit.text + lastDigit.text)
}