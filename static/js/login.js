const seePasswordSignup = () =>{
    let password = document.getElementById("passwords")
    let cpassword = document.getElementById("cpasswords")
    if(password.type == "password" || cpassword.type == "password"){
        password.type = "text";
        cpassword.type = "text";
    }else{
        password.type = "password";
        cpassword.type = "password";
    }
}

const tooglePasswordLogin = () =>{
    let password = document.getElementById("password")
    if(password.type == "password"){
        password.type = "text";
    }else{
        password.type = "password"
    }
}

const removeError = (clicked_id) =>{
    document.getElementById(clicked_id).style.borderColor = "#CED4DA";
}

const validateLogin = () =>{
    let username = document.getElementById("useremail");
    let password = document.getElementById("password");
    let rememberme = document.getElementById("password");

    if(username.value.trim() === '' || password.value.trim() === ''){
        if(username.value.trim() === ''){
            username.style.borderColor = 'red';
            return false;
        }else{
            password.style.borderColor = 'red';
            return false;
        }
    }else{
        if(rememberme.checked){
            let userdet = {
                'useremail':useremail.value,
                'password':password.value
            }

            localStorage.setItem("userdet", JSON.stringify(userdet))
        }
    }
}

const setUser = () =>{
    let username = document.getElementById("useremail");
    let password = document.getElementById("password");
    
    let details = localStorage.getItem("userdet")
    if(details){
        let userobj = JSON.parse(details);
        username.value = userobj.useremail;
        password.value = userobj.password;
    }
}

window.onload = setUser;


const validateSignup = () =>{
    let useremails = document.getElementById('useremails')
    let passwords = document.getElementById('passwords')
    let cpasswords = document.getElementById('cpasswords')

    if(useremails.value.trim() === '' || passwords.value.trim() === ''|| cpasswords.value.trim() === ''){
        if(useremails.value.trim() === ''){
            useremails.style.borderColor = "red";
            return false;
        }else if(passwords.value.trim() === ''){
            passwords.style.borderColor = "red";
            return false;
        }else{
            cpasswords.style.borderColor = "red";
            return false;
        }
    }else{
        if(passwords.value.trim() != cpasswords.value.trim()){
            passwords.style.borderColor = "red";
            cpasswords.style.borderColor = "red";
            return false;
        }
    }
}

const validateTestimonial = (event) =>{
    event.preventDefault()
    let targets = document.getElementById("testimony")
    if(targets.value.trim() === ''){
        targets.style.borderColor= "red";
    }
}

const closeTestimonials = () =>{
    document.getElementById("toogleinput").style.display = "none";
}

const openTestimonials = () =>{
    document.getElementById("toogleinput").style.display = "block";
}

const validateSearch = () =>{
    let location = document.getElementById("location")
    let types = document.getElementById("types")
    let price = document.getElementById("price")

    if(location.value.trim() === '' || types.value.trim() === '' || price.value.trim() === ''){
        if(location.value.trim() === ''){
            location.style.borderColor = "red";
            return false;
        }else if(types.value.trim() === ''){
            types.style.borderColor = "red";
            return false;
        }else{
            price.style.borderColor = "red";
            return false;
        }
    }
}

const validatContact = () =>{
    let firstname = document.getElementById("firstname");
    let lastname = document.getElementById("lastname");
    let emailadress = document.getElementById("emailadress");
    let phonenumber = document.getElementById("phonenumber");
    let messages = document.getElementById("messages");

    if(firstname.value.trim() === '' || lastname.value.trim() === '' || emailadress.value.trim() === '' || phonenumber.value.trim() === '' || messages.value.trim() === ''){
        if(firstname.value.trim() === ''){
            firstname.style.borderColor = "red";
            return false;
        }else if(lastname.value.trim() === ''){
            lastname.style.borderColor = "red";
            return false;
        }else if(emailadress.value.trim() === ''){
            emailadress.style.borderColor = "red";
            return false;
        }else if(phonenumber.value.trim() === ''){
            phonenumber.style.borderColor = "red";
            return false;
        }else{
            messages.style.borderColor = "red";
            return false;
        }
    }
}

const validateAvailability = () =>{
    let useremails = document.getElementById("useremails");
    let telephoneno = document.getElementById("telephoneno");
    let availabilitymessage = document.getElementById("availabilitymessage");

    if(useremails.value.trim() === '' || telephoneno.value.trim() === '' || availabilitymessage.value.trim() === ''){
        if(useremails.value.trim() === ''){
            useremails.style.borderColor = "red";
            return false;
        }else if(telephoneno.value.trim() === ''){
            telephoneno.style.borderColor = "red";
            return false;
        }else{
            availabilitymessage.style.borderColor = "red";
            return false;
        }
    }
}

const closeCheckAvailability = () =>{
    document.getElementById("checkavailability").style.display = "none";
}


const openCheckAvailability = () =>{
    document.getElementById("checkavailability").style.display = "block";
}