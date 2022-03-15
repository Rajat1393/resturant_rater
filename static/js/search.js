$(document).ready(function() {

    var googleplaceid = window.location.href.split("?")[1]
    $("#googleplaceid").val(googleplaceid);
    console.log("id:", window.location.href.split("?")[1]);

})