// Scroll buttons
document.querySelectorAll('.scroll-btn').forEach(btn => {
  const row = document.getElementById(btn.dataset.target);
  btn.onclick = () => {
    row.scrollBy({
      left: btn.classList.contains('left') ? -260 : 260,
      behavior: 'smooth'
    });
  };
});

// Scroll to form
const scrollTo = (id) => {
  document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
};

document.getElementById('dataBtn').onclick = () => scrollTo('data-form');
document.getElementById('heroDataBtn').onclick = () => scrollTo('data-form');

// Footer year
document.getElementById("year").textContent = new Date().getFullYear();


// ---------- FORM ----------
const form = document.getElementById("form");
const submitButton = document.getElementById("submit-button");
const messageDiv = document.getElementById("message");
const fileInput = document.getElementById("fileInput");
const fileNameDisplay = document.getElementById("fileNameDisplay");

// Show file name
fileInput.addEventListener("change", () => {
  fileNameDisplay.textContent = fileInput.files.length
    ? fileInput.files[0].name
    : "No file selected";
});

// Convert file
async function uploadFile(file) {
  return new Promise((resolve, reject) => {
    const fr = new FileReader();
    fr.onload = (e) => {
      const data = e.target.result.split(",");
      resolve({
        fileName: file.name,
        mimeType: data[0].match(/:(.*?);/)[1],
        data: data[1]
      });
    };
    fr.onerror = reject;
    fr.readAsDataURL(file);
  });
}

// Submit
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  messageDiv.style.display = "block";
  messageDiv.textContent = "Submitting...";
  submitButton.disabled = true;

  try {
    const formData = new FormData(form);
    const obj = {};

    for (let [k, v] of formData.entries()) obj[k] = v;

    if (fileInput.files.length > 0) {
      obj.fileData = await uploadFile(fileInput.files[0]);
    }

    const res = await fetch("YOUR_SCRIPT_URL", {
      method: "POST",
      body: JSON.stringify(obj),
      headers: { "Content-Type": "text/plain" }
    });

    const data = await res.json();

    if (data.status === "success") {
      messageDiv.textContent = "✅ Submitted successfully";
      form.reset();
      fileNameDisplay.textContent = "No file selected";
    } else throw new Error();

  } catch {
    messageDiv.textContent = "❌ Submission failed";
  }

  submitButton.disabled = false;
});