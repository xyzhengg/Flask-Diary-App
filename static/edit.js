// DELETE ALL IMAGES MODAL
const deleteAllImagesBtn = document.querySelector(".delete-all-images")
const theDeleteImagesContainer = document.querySelector(".the-delete-images")
const deleteImagesContent = document.querySelector(".delete-images")
const closeDeleteImages = document.querySelector(".close-delete-images")

deleteAllImagesBtn.addEventListener('click', function() {
    console.log('click')
    theDeleteImagesContainer.style.display = "block";
    deleteImagesContent.style.display = "block";
})

closeDeleteImages.addEventListener('click', function() {
    deleteImagesContent.style.display = "none";
    theDeleteImagesContainer.style.display = "none";
})

theDeleteImagesContainer.addEventListener('click', function() {
    deleteImagesContent.style.display = "none";
    theDeleteImagesContainer.style.display = "none";
})