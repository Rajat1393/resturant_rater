$(document).ready(function() {

    $("#addReview").click(function() {
        var restaurantId = $("#restaurantId").text()
        window.location.href = "../redirectRating" + "?" + restaurantId;
    });


    $("#addReview1").click(function() {
        var restaurantId = $("#restaurantId").text()
        window.location.href = "../login" + "?" + restaurantId;
    });
});