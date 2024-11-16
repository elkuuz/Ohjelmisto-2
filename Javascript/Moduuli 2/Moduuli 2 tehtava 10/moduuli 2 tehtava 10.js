const prompt=require('prompt-sync')();

const numCandidates=parseInt(prompt("Enter the numberr of candidates: "));
const candidates=[];

for (let i = 0; i < numCandidates; i++) {
    const name=prompt(`Name for candidate ${i+1}: `);
    candidates.push({name: name, votes: 0});
}

const numVoters=parseInt(prompt("Enter the number of voters: "));

for (let i=0; i<numVoters; i++){
    const vote=prompt(`Voter ${i+1}, who will you vote for? (Enter name or leave empty for no vote): `);

    if (vote.trim() !==""){
        const candidate=candidates.find(c=> c.name.toLowerCase() === vote.toLowerCase());
        if (candidate) {
            candidate.votes++;
        } else{
            console.log(`Invalid vote: ${vote} (candidate not found)`)
        }
    }
}

candidates.sort((a,b) => b.votes-a.votes);

const winner=candidates[0];
console.log(`The winner is ${winner.name} with ${winner.votes} votes`);

console.log("Results: ");
for (const candidate of candidates){
    console.log(`${candidate.name}: ${candidate.votes} votes`);
}