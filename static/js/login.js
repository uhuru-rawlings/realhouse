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