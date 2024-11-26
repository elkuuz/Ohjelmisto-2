'use strict';

const targetElement=document.getElementById("target");

const names = ['John', 'Paul', 'Jones'];

names.forEach(name=>{
    const li=document.createElement("li");
    li.textContent=name;
    targetElement.appendChild(li);
});


