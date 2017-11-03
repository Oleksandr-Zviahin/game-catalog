(function () {
    document.getElementById("submit")
        .addEventListener("click", function () {
                $.post("http://127.0.0.1:8080/rest-genre-list/", {
                genre_name: $("#id_genre_name").val(),
                genre_description: $("#id_genre_description").val()
            },
            function(data) {
                alert(data);
            });
        });
})();