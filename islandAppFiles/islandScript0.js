//const islandItemWriter = document.createElement("div");
//islandItemWriter.innerText = "We started to add island information";
//document.body.appendChild(islandItemWriter);

addEventListener('change', function(e) {
    var season = document.getElementById('seasonSelect'); //Get customer first selection: season
    
    var islandContainer = document.getElementById('islandContainer'); //Get the island information container

    var IslandWriter0a = document.createElement('div');
    IslandWriter0a.innerHTML = season.value

    if (islandContainer.innerHTML === "") {
        document.islandContainer.appendChild(IslandWriter0a); //Check if there is contents, and add their selection to the container if empty
        console.log("the div is empty, appending the customer choice")
    } else {
        document.getElementById('IslandContainer').innerHTML = ""; //Clear the contents and write to it, to keep just one season in the container.
        document.islandContainer.appendChild(IslandWriter0a); //Add their selection to the container
        console.log("The div had content, clearing it out and appending customer choice")
    }

    //var islandItemWriter0a = document.createElement('div'); //Set up the container to hold the selection on screen
    //islandItemWriter0a.setAttribute('id', 'IslandContainer')
    //islandItemWriter0a.innerHTML = season.value; //Add their selection to the container

    //document.getElementById('IslandContainer').innerHTML = ""; //Clear the contents and write to it, to keep just one season in the container.
    //document.body.appendChild(islandItemWriter0a);
});