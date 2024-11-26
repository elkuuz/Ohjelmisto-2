const num1input=document.getElementById('num1');
const num2input=document.getElementById('num2');
const operationSelect=document.getElementById('operation');
const calculateButton=document.getElementById('start');
const resultParagraph=document.getElementById('result');

calculateButton.addEventListener('click', function(){

    event.preventDefault();

    const num1=parseFloat(num1input.value);
    const num2=parseFloat(num2input.value);
    const operation=operationSelect.value;



    let result;
    if (isNaN(num1) || isNaN(num2)) {
        result='Enter a valid number: ';
    } else{
        switch(operation) {
            case 'add':
                result=num1+num2;
                break;
            case 'sub':
                result=num1-num2;
                break;
            case 'multi':
                result=num1*num2;
                break;
            case 'div':
                result=num2 !==0 ? num1/num2: 'Cannot divide by 0';
                break;
            default:
                result="Unknown operation: "
        }
    }

    resultParagraph.textContent=`Result: ${result}`;
});