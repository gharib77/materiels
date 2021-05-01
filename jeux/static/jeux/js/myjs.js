$(document).ready(function () {
    $(".edit-js").on('click', function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modalpers").modal("show");
            },
            success: function (data) {
                $("#modalpers .modal-content").html(data.html_form);
            }
        });
    });

    $("#modalpers").on("submit", ".create-pers-js", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#personnes tbody").html(data.html_Pers_list);  // <-- Replace the table body
                    $("#modalpers").modal("hide");  // <-- Close the modal
                }
                else {
                    $("#modalpers .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });
    
})