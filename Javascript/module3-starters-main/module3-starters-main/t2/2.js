const targetElement=document.getElementById("target");

const items=["First Item", "Second Item", "Third Item"];

items.forEach((text, index)=>{
    const li=document.createElement("li");
    li.textContent=text;

    if (index===1) {
        li.classList.add("my-item");
    }

    targetElement.appendChild(li);
});