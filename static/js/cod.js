var usuario = document.forms[`form`] [`usuario`];
var Contraseña = document.forms[`form`] [`password`];


function validated(){
    if (usuario.value.length < 6){
        usuario.style.border = "1px solid red";
        usuario.style.display = "block";
        usuario.focus();
        return false;
    }
    if (Contraseña.value.length < 7){
        Contraseña.style.border = "1px solid red";
        contraseña.style.display = "block";
        Contraseña.focus();
        return false;
    }
}
