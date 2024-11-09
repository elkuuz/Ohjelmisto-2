const num1=Number(prompt('Enter the first integer: '))
const num2=Number(prompt('Enter the second integer: '))
const num3=Number(prompt('Enter the third integer: '))

const sum= num1+num2+num3
const average=sum/3
const product= num1*num2*num3

document.getElementById("results").innerHTML=`
        <p>Sum: ${sum}</p>
        <p>Average:${average.toFixed(2)} </p>
        <p>Product: ${product}</p>
`;