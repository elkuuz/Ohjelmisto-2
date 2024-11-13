function sortingHat() {
    let studentName=prompt("Enter your name: ");

    let houseNumber= Math.floor(Math.random()*4)+1;
    let house;

    if (houseNumber===1) {
        house="Gryffindor";
    } else if(houseNumber===2) {
            house="Slytherin";
    } else if(houseNumber===3){
            house="Hufflepuff";
    } else{
            house="Ravenclaw";
    }

    document.getElementById("Result").textContent=`${studentName} you are ${house}`;
}

sortingHat();