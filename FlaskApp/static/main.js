$(document).ready(function () {

    var url = "http://"+window.location.host
    var APIurl = url + "/api/"

    // window.alert("Window loaded");

    $("#next").click(function() {
        // window.alert("Clicked next")

        if ($("#fn").val() == "") {
            window.alert("First name is required!")
        } else if ($("#ln").val() == "") {
            window.alert("Last name is required!")
        } else {
            var form = $('form').serialize()
            window.alert(form)
    
            $.ajax({
                type: "POST",
                url: APIurl + "1",
                data: form,
            })
    
        }
    })

})