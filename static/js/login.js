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

window.onload= setUser;


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