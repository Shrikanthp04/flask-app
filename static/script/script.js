function validateForm() {
    var errorDiv = document.getElementById('error-message');
    var fields = document.querySelectorAll('input[type="number"]');
    for (var i = 0; i < fields.length; i++) {
        if (!fields[i].checkValidity()) {
            errorDiv.style.display = 'block';
            return false;
        }
    }
    errorDiv.style.display = 'none';
    return true;
}