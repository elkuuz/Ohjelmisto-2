let dog=[]

for (let i=0;i<6; i++){
    let dogName=prompt(`Enter the name of the ${i+1} dog:`)
    dog.push(dogName);
}

dog.sort((a, b) => b.localeCompare(a));

let ul=document.createElement('ul');

for (let i=0; i<6; i++){
    let li=document.createElement("li");
    li.textContent=dog[i];
    ul.appendChild(li);
}

document.getElementById('dogs').appendChild(ul);