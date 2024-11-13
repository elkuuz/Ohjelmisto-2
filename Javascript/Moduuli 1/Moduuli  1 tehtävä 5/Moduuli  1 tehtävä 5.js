function checkLeapYear() {
    let year=parseInt(prompt("Enter a year: "));
    let isleapYear;

    if ((year % 4===0 && year % 100 !== 0)||( year % 400===0)) {
        isleapYear = true;
    } else{
        isleapYear = false;
    }

    document.getElementById("result").textContent=isleapYear
        ? `${year} is a leap year.`
        : `${year} is not a leap year.`;
}

checkLeapYear();