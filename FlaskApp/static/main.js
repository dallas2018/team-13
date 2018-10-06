$(document).ready(function () {

    var url = "http://"+window.location.host
    var APIurl = url + "/api/"

//    $("#start").click(function() {
//        window.location.href = "/static/1.html";
//    })

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
        var currentPage = parseInt(window.location.pathname.substr(8, 1));
//        var currentPage = parseInt(window.location.pathname.substr(1, window.location.pathname.indexOf('.html')));

        var email = ""

        if (currentPage == 1) {
            email = $("#email").val();
        } else {
            email = getParameterByName('email')
//            email = window.location.href.split("?email=")[1];
        }
        var nextPage = (currentPage + 1).toString() + ".html"
        nextPage = nextPage + "?email=" + email;

        // Send to back end
        $.ajax({
            type: "POST",
            url: APIurl,
            data: form,
            headers: {"page": currentPage, "email": email}
        })

        // Load next page
        window.location.href = "/static/" + nextPage;
    })

})

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}
