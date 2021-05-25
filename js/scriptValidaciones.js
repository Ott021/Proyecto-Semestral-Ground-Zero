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

function isTelefono(telefono) {
    var regex = /^\d{6,10}$/;
    return regex.test(telefono);
}

function validarRut() {
    if ($("#rut").val().trim().length == 0) {
        mensajeError("errorRut", "Campo Obligatorio (*)")
        return false
    }

    else if ($("#rut").val().trim().length < 8) {
        mensajeError("errorRut", "Rut inválido(*)")
        return false
    }

    else {
        noError("errorRut")
        return true
    }
}


function validarNombre() {
    if ($("#nombre").val().trim().length == 0) {
        mensajeError("errorNombre", "Campo Obligatorio (*)")
        return false
    } else {
        noError("errorNombre")
        return true
    }
}

function validarEmail() {
    if ($("#correo").val().trim().length == 0) {
        mensajeError("errorCorreo", "Campo Obligatorio (*)")
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

function validarCelular() {
    if ($("#telefono").val().trim().length != 0) {
        if (!isTelefono($("#telefono").val())) {
            mensajeError("errorCelu", "Campo Obligatorio (*)")
            return false
        } else {
            noError("errorCelu")
            return true
        }
    } else {
        noError("errorCelu")
        return true
    }
}

function validarComentarios(largo) {
    if ($("#texto").val().trim().length < largo) {
        mensajeError("errorTexto", "Comentario debe tener al menos " + largo + " caracteres")
        return false
    } else {
        noError("errorTexto")
        return true
    }
}



$(document).ready(function () {

    $(".invalid-feedback").hide()

    $("#rut").blur(function () {
        exito = validarRut()
    });

    //Validar Nombre
    $("#nombre").blur(function () {
        exito = validarNombre()
    });

    //Validar Email
    $("#correo").blur(function () {
        exito = validarEmail()
    });

    //Validar Telefono
    $("#telefono").blur(function () {
        exito = validarCelular()
    });

    //Validar Ciudad
    $("#cboCiudad").change(function () {
        exito = validaCiudad()
    });

    //Validar Comentarios
    $("#texto").blur(function () {
        exito = validarComentarios(50)
    });

    $("#texto").keyup(function () {
        var totalcaracteres = $("#texto").val().trim().length
        $("#contChar").text(totalcaracteres)
    });


    //Envío del formulario
    $("#form1").submit(function () {
        exito = false


        //valida antes de enviar el formulario

        if (!validaNombre() ||
            !validaEmail() ||
            !validaTelefono() ||
            !validaCiudad() ||
            !validaComentarios(50)
        ) {
            event.preventDefault()
        }

    });
});