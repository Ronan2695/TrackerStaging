$(document).ready(function () {
    toggleFields();
    $("#id_Escalated").change(function () {
        toggleFields();
    });

});

function toggleFields() {
    if ($("#id_Escalated").val() === "Yes")
        $("#id_Escalated_to").show() && $("#id_Escalated_Reason").show();
    else
        $("#id_Escalated_to").hide() && $("#id_Escalated_Reason").hide();
}
