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
    {
        /* <div>
        						<label for="male">Email address</label>
        						<input type="text" placeholder=" name@example.com ">
        					</div>
        					<div>
        						<label for="male">username</label>
        						<input type="password" placeholder=" username ">{{profile}}
        					</div>
        					<div>
        						<label for="male">History review 1</label>
        						<textarea placeholder="History review 1">{{reviews}}</textarea>
        					</div>

        					<div>
        						<label for="male">History review 2</label>
        						<textarea placeholder="History review 2"></textarea><br>
        					</div> */
    }
    // function chooseImg(file) {
    //     var file = file.files[0]
    //     var reader = new FileReader()
    //     reader.readAsDataURL(file)
    //     reader.onload = function() {
    //         var img = document.getElementById('img')

    //         img.src = this.result
    //         console.log('---',img.src)
    //     }
    // }


    // $(document).ready(function(){

    //     $("#f").onchange(function(file){
    //         var file = file.files[0]
    //         var reader = new FileReader()
    //         reader.readAsDataURL(file)
    //         reader.onload = function() {
    //             var img = document.getElementById('img')

    //             img.src = this.result
    //             console.log('---',img.src)
    //         }
    //     })
    //     $("#createProfile").onclick(function({
    //         $.ajax({
    //             url:"{% url 'rater:updateuserprofile' %}",
    //             type:"get",
    //             dataType:"json",
    //             success:function(data){
    //                 $(this).text("恢复按钮一");
    //                 console.log("看看进来没有？");
    //             }
    //         }); 


    //     })) 
});