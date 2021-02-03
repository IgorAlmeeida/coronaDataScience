$("#dataInput").change(function (e) {
    let dataParameterMenor = new Date('2020-02-25');
    let dataParameterMaior = new Date('2021-01-31');
    let data = new Date($(this).val())

    if (data <= dataParameterMenor || data > dataParameterMaior){
        alert("Data informada não faz parte do danco de dados");
    }else{
        $.ajax({
            type: "POST",
            url: $(this).attr('endPoint'),
            headers:{
                "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
            },
            data: {
                data: $(this).val(),
            },
            dataType: "json",
            success: function (response) {
                $("#lista_estado").html("");
                response.forEach(element => {
                    $("#lista_estado").append(criarTrEstado(element));
                });
            }
        });

        $.ajax({
            type: "POST",
            url: $(this).attr('endPoint1'),
            headers:{
                "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
            },
            data: {
                data: $(this).val(),
            },
            dataType: "json",
            success: function (response) {
                console.log(response);
                $("#casosConfirmados").text(response[0].casosAcumulado);
                $("#novosCasos").text(response[0].casosNovos);
                $("#novosObitos").text(response[0].obitosAcumulado);
                $("#obitos").text(response[0].obitosNovos);
            }
        });
    }
    
});


function criarTrEstado(element){
    let tr = "<tr>";
            tr += "<td>"+element.estado+"</td>";
            tr += "<td>"+element.casosAcumulado+"</td>";
            tr += "<td>"+element.obitosAcumulado+"</td>";
            tr += "<td>"+element.percPopCasos+"</td>";
            tr += "<td>"+element.casoAnterior+"</td>";
            tr += "<td>"+element.percCaso+"</td>";
            tr += "<td>"+element.percObito+"</td>";
            tr += "<td>"+element.novosCasos+"</td>";
            tr += "<td>"+element.novosObitos+"</td>";
        tr += "<tr>";
    
    return tr;
}