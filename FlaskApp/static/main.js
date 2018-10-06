$(document).ready(function () {

    var url = "http://"+window.location.host
    var APIurl = url + "/api/"

    // window.alert("Window loaded");

    $("#next").click(function() {
        // window.alert("Clicked next")

        // var token =  $("#gittoken").val()
        // var username = $("#gitusername").val()
        // var repo = $("#gitrepo").val()

        var form = $('form').serialize()
        window.alert(form)

        $.ajax({
            type: "POST",
            url: APIurl + "1",
            data: form,
        })

    })

})