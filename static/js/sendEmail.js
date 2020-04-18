
function sendMail(contactForm) {
    emailjs.send("gmail", "scriptio", {
        "from_name": contactForm.from_name.value,
        "from_email": contactForm.from_email.value,
        "message": contactForm.message.value
    }, "user_zryNwhPPBjpsX5Jah5OM5")
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}