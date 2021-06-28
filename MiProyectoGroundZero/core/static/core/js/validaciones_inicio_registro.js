function mensajeError(caja, mensaje) {
    $("#" + caja).html(mensaje)
    $("#" + caja).fadeIn()
}

function noError(caja) {
    $("#" + caja).fadeOut()
}
function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validarNombre() {
    if ($("#nombre").val().trim().length == 0) {
        mensajeError("errorNombre", "Debe ingresar un Nombre")
        return false
    } else {
        noError("errorNombre")
        return true
    }
}

function validarEmail() {
    if ($("#correo").val().trim().length == 0) {
        mensajeError("errorCorreo", "Debe ingresar un correo")
        return false
    } else {

        if (!isEmail($("#correo").val())) {
            mensajeError("errorCorreo", "Correo electrónico no válido")
            return false
        } else {
            noError("errorCorreo")
            return true
        }
    }
}

function validarContraseña() {
    if ($("#contraseña").val().trim().length == 0) {
        mensajeError("errorContraseña", "Debe escribir una contraseña")
        return false
    }

    else if ($("#contraseña").val().trim().length < 9) {
        mensajeError("errorContraseña", "La contraseña debe tener un minimo de 9 caracteres")
        return false
    }

    else {
        noError("errorContraseña")
        return true
    }
}

$(document).ready(function () {

    $(".invalid-feedback").hide()

    $("#nombre").blur(function () {
        exito = validarNombre()
    });

    $("#correo").blur(function () {
        exito = validarEmail()
    });


    $("#contraseña").blur(function () {
        exito = validarContraseña()
    });


});