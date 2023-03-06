// DELETE MODAL FUNCTION

const viewDeleteButton = document.querySelector(".view-delete-button")
const deleteBtn = document.querySelector(".delete")
const theDelete = document.querySelector(".the-delete")
const closeDelete = document.querySelector(".close-delete")

viewDeleteButton.addEventListener('click', function() {
    deleteBtn.style.display = "block";
    theDelete.style.display = "block";
})

closeDelete.addEventListener('click', function() {
    deleteBtn.style.display = "none";
    theDelete.style.display = "none";
})

theDelete.addEventListener('click', function() {
    deleteBtn.style.display = "none";
    theDelete.style.display = "none";
})
