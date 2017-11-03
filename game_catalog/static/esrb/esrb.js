function getESRBList() {
    $.ajax({
        url: "http://127.0.0.1:8080/rest-esrb-list/",
        success: function (result) {
            var esrb = {"esrb": result};
            var template = "<ul>" +
                "{{#esrb}}" +
                "<li> <strong>{{rate_full_name}} ({{rate_short_name}})</strong> - {{rate_description}} </li>" +
                "{{/esrb}}" +
                "</ul>";
            var html = Mustache.to_html(template, esrb);
            $("#esrb_list").html(html);
        }
    });
}

(function () {
    document.getElementById("get_esrb_list_button")
        .addEventListener("click", function () {
            getESRBList();
            //document.getElementById("demo").innerHTML = "Hello World";
        });
})();
