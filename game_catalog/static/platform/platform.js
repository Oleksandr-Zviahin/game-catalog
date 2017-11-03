function getPlatformList() {
    $.ajax({
        url: "http://127.0.0.1:8080/rest-platform-list/",
        success: function (result) {
            var platforms = {"platforms": result};
            var template = "<ul>" +
                "{{#platforms}}" +
                "<li> <strong>{{platform_name}}:{{platform_version}}</strong> - {{platform_description}} </li>" +
                "{{/platforms}}" +
                "</ul>";
            var html = Mustache.to_html(template, platforms);
            $("#platform_list").html(html);
        }
    });
}

(function () {
    document.getElementById("get_platform_list_button")
        .addEventListener("click", function () {
            getPlatformList();
            //document.getElementById("demo").innerHTML = "Hello World";
        });
})();
