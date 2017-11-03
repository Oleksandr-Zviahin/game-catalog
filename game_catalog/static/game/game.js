function getGameList() {
    $.ajax({
        url: "http://127.0.0.1:8080/rest-game-list/",
        success: function (result) {
            var games = {"games": result};
            var newTemplate = "{{#games}}" +
                "<table border='1' align='center'>" +
                "<tr>" +
                "<td>Название игры</td>" +
                "<td>Компания</td>" +
                "<td>Дата выпуска</td>" +
                "<td>Категория</td>" +
                "<td>Возрастное ограничение</td>" +
                "<td>Жанры</td>" +
                "<td>Платформы</td>" +
                "</tr>" +
                "<tr>" +
                "<td>" + "{{game_name}}" + "</td>" +
                "<td>" + "{{game_company}}" + "</td>" +
                "<td>" + "{{game_release_date}}" +"</td>" +
                "<td>" + "{{category_id.category_name}}" +"</td>" +
                "<td>" + "{{esrb_id.rate_full_name}}" +"</td>" +
                "<td>" + "{{#genres}}" + "{{genre_name}} " + "{{/genres}}" + "</td>" +
                "<td>" + "{{#platforms}}" + "{{platform_name}} " + "{{/platforms}}" +"</td>" +
                "</tr>" +
                "<tr>" +
                "<td colspan='7'> {{game_description}} </td>" +
                "</tr></table>" +
                "{{/games}}"
            var html = Mustache.to_html(newTemplate, games);
            $("#game_list").html(html);
        }
    });
}

(function () {
    document.getElementById("get_game_list_button")
        .addEventListener("click", function () {
            getGameList();
        });
})();
