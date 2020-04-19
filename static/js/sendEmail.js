
function sendMail(contactForm) {
    emailjs.send("gmail", "scriptio", {
        "from_name": contactForm.from_name.value,
        "from_email": contactForm.from_email.value,
        "message": contactForm.message.value
    }, "user_zryNwhPPBjpsX5Jah5OM5")
    .then(
        function(response) {
            // aslong as the response is ok, the modal will close and reset the values
            $("#modal-contact").modal("close")
            document.getElementById("contactForm").reset();
        },
        function(error) {
            alert("FAILED, sorry there was an error on ourside sending the email", error);
        }
    );
    return false;  // To block from loading a new page
}