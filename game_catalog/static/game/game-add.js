(function () {
    document.getElementById("submit")
        .addEventListener("click", function () {
                $.post("http://127.0.0.1:8080/rest-game-list/", {
                game_name: $("#id_game_name").val(),
                game_company: $("#id_game_company").val(),
                game_description: $("#id_game_description").val(),
                game_release_date: $("#id_game_release_date").val()
            },
            function(data) {
                alert(data);
            });
        });
})();