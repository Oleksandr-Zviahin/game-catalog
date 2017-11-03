function getGenreList() {
    $.ajax({
        url: "http://127.0.0.1:8080/rest-genre-list/",
        success: function (result) {
            var genres = {"genres": result};
            var template = "<ul>" +
                "{{#genres}}" +
                "<li> <strong>{{genre_name}}</strong> - {{genre_description}} </li>" +
                "{{/genres}}" +
                "</ul>";
            var html = Mustache.to_html(template, genres);
            $("#genre_list").html(html);
        }
    });
}

(function () {
    document.getElementById("get_genre_list_button")
        .addEventListener("click", function () {
            getGenreList();
            //document.getElementById("demo").innerHTML = "Hello World";
        });
})();
