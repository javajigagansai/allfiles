document.querySelector("body").addEventListener("mousemove", eyeball);

function eyeball(event) {
    const eyes = document.querySelectorAll(".eyes"); // Select all eyes
    eyes.forEach(function (eye) {
        let x = eye.getBoundingClientRect().left + eye.clientWidth / 2; // Correct clientWidth
        let y = eye.getBoundingClientRect().top + eye.clientHeight / 2; // Correct clientHeight
        let radian = Math.atan2(event.pageX - x, event.pageY - y); // Calculate angle
        let rotate = radian * (180 / Math.PI) * -1 + 270; // Convert radian to degrees and rotate
        eye.style.transform = "rotate(" + rotate + "deg)"; // Apply rotation
    });
}
