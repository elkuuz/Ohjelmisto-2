const readline = require('readline');


const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let numbers = [];
let count = 0;

console.log("Enter 5 numbers:");

function getNumber() {
  rl.question(`Enter number ${count + 1}: `, (input) => {
    const num = parseFloat(input);
    if (!isNaN(num)) {
      numbers.push(num);
      count++;
      if (count < 5) {
        getNumber();
      } else {
        console.log("Numbers in reverse order:");
        for (let i = numbers.length - 1; i >= 0; i--) {
          console.log(numbers[i]);
        }
        rl.close();
      }
    } else {
      console.log("Please enter a valid number.");
      getNumber();
    }
  });
}

getNumber();
