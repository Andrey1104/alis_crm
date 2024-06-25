function toggleOnHoldReason() {
    var productionStatus = document.getElementById("id_production_status");
    var onHoldReasonField = document.getElementById("onHoldReasonField");
    if (productionStatus.value === "ON_HOLD") {
        onHoldReasonField.style.display = "block";
    } else {
        onHoldReasonField.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", function () {
    toggleOnHoldReason();
    document.getElementById("id_production_status").addEventListener("change", toggleOnHoldReason);
});
