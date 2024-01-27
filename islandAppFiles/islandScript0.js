//const islandItemWriter = document.createElement("div");
//islandItemWriter.innerText = "We started to add island information";
//document.body.appendChild(islandItemWriter);

addEventListener('change', function(e) {
    document.getElementById('islandContainer').innerHTML = ""; //Clear the contents

    var season = document.getElementById('seasonSelect'); //Get customer first selection: season
    var IslandWriter0a = document.createElement('div'); //Set up selection in new div element
    IslandWriter0a.innerHTML = season.value

    var islandContainer0a = document.getElementById("islandContainer");  //Get the island information container
    islandContainer0a.appendChild(IslandWriter0a); //Apply it to the element

});

addEventListener('change', function(e) {
    document.getElementById('island2ndContainer').innerHTML = ""; //Clear the population size

    var size = document.getElementById('sizeSelect'); //Get customer second select: size
    var IslandWriter1b = document.createElement('div'); //Set up the selection in a new div element
    IslandWriter1b.innerHTML = size.value

    var islandContainer1b = document.getElementById("island2ndContainer"); //Get the 2nd island information container
    islandContainer1b.appendChild(IslandWriter1b); //Apply it to the element
})