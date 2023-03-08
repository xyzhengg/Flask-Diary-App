// CONFIRM EDIT MODAL FUNCTION
const submitEditButton = document.querySelector(".submit-edit")
const theEdit = document.querySelector(".the-edit")
const editBtn = document.querySelector(".edit")
const closeEdit = document.querySelector(".close-edit")
const saveEditButton = document.querySelector(".confirm-edit-btn")
const submitEditForm = document.querySelector(".edit-form")

submitEditButton.addEventListener('click', function(event) {
    event.preventDefault();
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

saveEditButton.addEventListener("click", function(){
    submitEditForm.submit()
})

// DELETE ALL IMAGES MODAL
const deleteAllImagesBtn = document.querySelector(".delete-all-images")
const deleteImagesBtn = document.querySelector(".delete-images")
const theDeleteImages = document.querySelector(".the-delete-images")
const closeDeleteImages = document.querySelector(".close-delete-images")

deleteAllImagesBtn.addEventListener('click', function() {
    console.log('click')
    deleteImagesBtn.style.display = "block";
    theDeleteImages.style.display = "block";
})

closeDeleteImages.addEventListener('click', function() {
    deleteImagesBtn.style.display = "none";
    theDeleteImages.style.display = "none";
})

theDeleteImages.addEventListener('click', function() {
    deleteImagesBtn.style.display = "none";
    theDeleteImages.style.display = "none";
})