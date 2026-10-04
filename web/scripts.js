document.addEventListener("DOMContentLoaded", function () {
    const status = document.querySelector("#status");

    if (status) {
        status.textContent = "System Ready";
    }
});

function showMessage() {
    alert("Road Accident Severity Prediction System is working successfully!");
}
