
function rollDice(){
    return Math.floor(Math.random() * 6)+1;
}

function main(){
    let ul=document.createElement('ul');

    let result;
    do {
        result=rollDice();

        let li=document.createElement('li');
        li.textContent=`You rolled ${result}`;
        ul.appendChild(li);
    } while (result != 6);

    document.getElementById('dice-results').appendChild(ul);
}

main();