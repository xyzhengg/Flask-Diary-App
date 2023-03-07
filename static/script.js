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

// CONFIRM EDIT MODAL FUNCTION
const submitEditButton = document.querySelector(".submit-edit")
const editBtn = document.querySelector(".edit")
const theEdit = document.querySelector(".the-edit")
const closeEdit = document.querySelector(".close-edit")

submitEditButton.addEventListener('click', function() {
    editBtn.style.display = "block";
    theEdit.style.display = "block";
})

closeEdit.addEventListener('click', function() {
    editBtn.style.display = "none";
    theEdit.style.display = "none";
})

theEdit.addEventListener('click', function() {
    editBtn.style.display = "none";
    theEdit.style.display = "none";
})
