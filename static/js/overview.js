$(document).ready(function() {

    $("#addReview").click(function() {
        var restaurantId = $("#restaurantId").text()
        window.location.href = "../redirectRating" + "?" + restaurantId;
    });


    $("#addReview1").click(function() {
        var restaurantId = $("#restaurantId").text()
        window.location.href = "../login" + "?" + restaurantId;
    });



    // $.ajax({
    //     url: "../redirectRating",
    //     data: {
    //         restaurantId: $("#restaurantId").text(),
    //     },
    //     success: function(data) {
    //         alert("Success: " + response);
    //     },
    //     error: function(jqXHR, textStatus, errorThrown) {
    //         alert("Error");
    //     }
    // });


});