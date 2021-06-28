function getMoneda(codigo) {

    var url_api = 'https://api.gael.cloud/general/public/monedas/' + codigo

    var precio_chileno = 20000

    $("#precioProducto").html(precio_chileno + " Pesos Chileno(s)")

    $.getJSON(
        //URL DEL API
        url_api
        ,
        //FUNCION QUE PROCESARA LA INFO QUE TRAE EL JSON
        function (data) {
            $("#precioProducto").html(Math.round(20000/parseInt(data.Valor)) + " " + data.Nombre+ "(s)")

        

        }
    );

}
$(document).ready(function () {


    //getMoneda("usd")


    $("#cambiarMoneda").click(function () {
        var codigo = $("#monedas").val()
        getMoneda(codigo)

    })


})