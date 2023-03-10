const viewDeleteButton = document.querySelector(".view-delete-button")
const deleteText = document.querySelector(".delete")
const theDelete = document.querySelector(".the-delete")
const closeDelete = document.querySelector(".close-delete")

viewDeleteButton.addEventListener('click', function() {
    console.log('click')
    deleteText.style.display = "block";
    theDelete.style.display = "block";
})

closeDelete.addEventListener('click', function() {
    deleteText.style.display = "none";
    theDelete.style.display = "none";
})


theDelete.addEventListener('click', function() {
    deleteText.style.display = "none";
    theDelete.style.display = "none";
})