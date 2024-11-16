let numParticipants=parseInt(prompt("How many participants: "));
let participants=[];


for(let i=0; i<numParticipants; i++){
    let participantName=prompt(`Enter the name of the participant ${i+1}: `)
    participants.push(participantName);
}

participants.sort();

let ol=document.createElement("ol");

for (let i=0; i<participants.length; i++){
    let li=document.createElement("li");
    li.textContent=participants[i];
    ol.appendChild(li);
}

document.getElementById('participants-list').appendChild(ol);