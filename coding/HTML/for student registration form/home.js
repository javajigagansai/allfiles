let students = [];
document.getElementById("regForm").addEventListener("submit", saveToExcel);
function saveToExcel(event) {
    event.preventDefault();
    const form = event.target;
    const student = {
        "First Name": form.first_name.value,
        "Last Name": form.last_name.value,
        "DOB": form.dob.value,
        "Email": form.email.value,
        "Phone": form.phone.value,
        "Course": form.course.value,
        "Year": form.year.value
    };
    students.push(student);
    const worksheet = XLSX.utils.json_to_sheet(students);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "Registrations");
    XLSX.writeFile(workbook, "Student_Registration.xlsx");
    alert("Registration saved to Excel!");
    form.reset();
}