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

const validateLogin = (event) =>{
    event.preventDefault()
    let username = document.getElementById("useremail");
    let password = document.getElementById("password");
    let rememberme = document.getElementById("password");

    if(username.value.trim() === '' || password.value.trim() === ''){
        if(username.value.trim() === ''){
            username.style.borderColor = 'red';
            return
        }else{
            password.style.borderColor = 'red';
            return
        }
    }
}