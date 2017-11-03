(function () {
    document.getElementById("submit")
        .addEventListener("click", function () {
                $.post("http://127.0.0.1:8080/rest-platform-list/", {
                platform_name: $("#id_platform_name").val(),
                platform_version: $("#id_platform_version").val(),
                platform_description: $("#id_platform_description").val()
            },
            function(data) {
                alert(data);
            });
        });
})();