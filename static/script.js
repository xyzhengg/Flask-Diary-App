let monthSelection = document.querySelector('.select-month')
let yearSelection = document.querySelector('.select-year')
let dateSelection = document.querySelector('.select-date')
let dateList = document.querySelectorAll('.date-list')

monthSelection.addEventListener("change", updateDateOptions)
yearSelection.addEventListener("change", updateDateOptions)

function updateDateOptions() {
    let selectedMonth = parseInt(monthSelection.value)
    console.log(selectedMonth)
    let selectedYear = parseInt(yearSelection.value)
    let selectedDate = parseInt(dateSelection.value)
    console.log(selectedDate)
    const leapYear = selectedYear % 4 === 0 && (selectedYear % 100 !== 0 || selectedYear % 400 === 0)
    console.log(leapYear)
    if (selectedMonth == 2 && leapYear) {
        if (dateList.value > 29) {
            dateList.style.display="none";
        }
    } else if (selectedMonth == 2 && !leapYear) {
        if (dateList.value > 28) {
            dateList.style.display="none";
        }
    } else if (selectedMonth == 4 || selectedMonth == 6 || selectedMonth == 9 || selectedMonth == 11){
        if (dateList.value > 30) {
            dateList.style.display="none";
        }
    } else {
        dateList.style.display="block";
    }
}