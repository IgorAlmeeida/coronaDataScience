$(document).ready(function(){
    var inputBuscar = $("#input-search");
    var formBuscar = $("#search-form");
    var buttonBuscar = $("#search-btn");

    $(buttonBuscar).click(function (e) { 
        e.preventDefault();
        formBuscar.submit();
    });

});