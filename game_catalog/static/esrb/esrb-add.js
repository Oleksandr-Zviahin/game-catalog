(function () {
    document.getElementById("submit")
        .addEventListener("click", function () {
                $.post("http://127.0.0.1:8080/rest-esrb-list/", {
                rate_full_name: $("#id_rate_full_name").val(),
                rate_short_name: $("#id_rate_short_name").val(),
                rate_description: $("#id_rate_description").val()
            },
            function(data) {
                alert(data);
            });
        });
})();