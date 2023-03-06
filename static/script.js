
// ON CHANGE FUNCTION TO GET CORRECT NUMBER OF DAYS TO SHOW BASED ON MONTH AND YEAR
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

    if (selectedMonth === 2 && leapYear) {
        dateList.forEach((dateOption, index) => {
            if (index >= 29) {
                dateOption.style.display = "none"
            } else {
                dateOption.style.display = "block"
            }
        })
    } else if (selectedMonth === 2 && !leapYear) {
        dateList.forEach((dateOption, index) => {
            if (index >= 28) {
                dateOption.style.display = "none"
            } else {
                dateOption.style.display = "block"
            }
        })
    } else if (selectedMonth == 4 || selectedMonth == 6 || selectedMonth == 9 || selectedMonth == 11){
        dateList.forEach((dateOption, index) => {
            if (index >= 30) {
                dateOption.style.display = "none"
            } else {
                dateOption.style.display = "block"
            }
        })
    } else {
        dateList.forEach((dateOption) => {
            dateOption.style.display = "block"
        })
    }
}