let monthSelection = document.querySelector('.select-month')
let yearSelection = document.querySelector('.select-year')
let dateSelection = document.querySelector('.select-date')

monthSelection.addEventListener("change", updateDateOptions)
yearSelection.addEventListener("change", updateDateOptions)

function updateDateOptions() {
    let selectedMonth = parseInt(monthSelection.value)
    console.log(selectedMonth)
    let selectedYear = parseInt(yearSelection.value)
    let selectedDate = parseInt(dateSelection.value)
    console.log(selectedDate)
    const leapYear = selectedYear % 4 === 0 && (selectedYear % 100 !== 0 || selectedYear % 400 === 0)
    if (selectedMonth === 2 && selectedYear == leapYear) {
        for (selectedDate > 29) {
            dateSelection.style.display = "none";
        }
    } else if (selectedMonth === 2 && !leapYear) {
        if (selectedDate > 28) {
            dateSelection.style.display="none"
        }
    } else if (selectedMonth === 4 || selectedMonth === 6 || selectedMonth === 9 || selectedMonth === 11){
        if (selectedDate > 30) {
            dateSelection.style.display="none"
        }
    } else {
        dateSelection.style.display="block"
    }
}