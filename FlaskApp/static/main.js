$(document).ready(function () {

    var url = "http://"+window.location.host
    var APIurl = url + "/api/"

    $("#start").click(function() {
        window.location.href = "1.html";
    })

    $("#next").click(function() {
        var flag = 0;
        // Make sure each element of required class is inputed
        $('.req').each(function(i, obj) {
            if (obj.value == "") {
                window.alert(obj.placeholder + " is required!");
                flag = 1;
            }
        });
        
        // Check if inputed all required fields
        if (flag == 1) {
            return;
        }

        // Gather all objects in our form
        var form = $('form').serialize();
        // window.alert(form);

        // Send to back end
        $.ajax({
            type: "POST",
            url: APIurl + "1",
            data: form,
        })

        var currentPage = parseInt(window.location.pathname.substr(1, window.location.pathname.indexOf('.html')));
        var nextPage = (currentPage + 1).toString() + ".html"
        // Load next page
        window.location.href = nextPage;
    })

})