$(document).ready(function() {

    $("#brunchClub").click(function() {
        var a = "The Brunch Club";
        $("#submitValue").val(a);
        $("#targetForm").submit();
    });

    $("#Tantrum").click(function() {
        var tantrum = "Tantrum Doughnuts";
        $("#submitValue").val(tantrum);
        $("#targetForm").submit();
    });

    $("#Five").click(function() {
        var five = "Five March"
        $("#submitValue").val(five);
        $("#targetForm").submit();
    });

    $("#Mister").click(function() {
        var mister = "Mister Singh's India";
        $("#submitValue").val(mister);
        $("#targetForm").submit();
    });

    $("#Buck").click(function() {
        var buck = "Buck's BarRestaurant";
        $("#submitValue").val(buck);
        $("#targetForm").submit();
    });

    $("#Garden").click(function() {
        var garden = "The Quay China Garden";
        $("#submitValue").val(garden);
        $("#targetForm").submit();
    });
})