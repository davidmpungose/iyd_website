function emailSend(){

    Email.send({
        Host : "smtp.elastice.com",
        Username : "inhlosoyetfu@gmail.com",
        Password : "25E9CFF0F39E0656AAA4B7BECB79B2A9FCC4",
        To : 'mpungosedavid4@gmail.com',
        From : "inhlosoyetfu@gmail.com",
        Subject : "This is the subject",
        Body : "And this is the body"
    }).then(
      message => alert(message)
    );
}