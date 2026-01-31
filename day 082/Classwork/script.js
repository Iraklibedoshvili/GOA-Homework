const account = [];

class Account{
    constructor(Firstname,Lastname,email,password){
        this.Firstname = Firstname,
        this.Lastname = Lastname,
        this.email = email,
        this.password = password
    }
}
const form = document.getElementById("register form");
form.addEventListener("Submit"),(event) =>{
    event.preventDefault();

    const makeaccount = () => {
        const Firstname = document.getElementById("Firstname").value;
        const Lastname = document.getElementById("Lastname").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        const account = new Account(Firstname,Lastname,email,password);
        account.push(account);

        console.log("New user",account)
        console.log("Account",account)
    }
    makeaccount()
}
