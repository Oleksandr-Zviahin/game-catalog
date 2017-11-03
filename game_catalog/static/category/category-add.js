(function () {
    document.getElementById("submit")
        .addEventListener("click", function () {
                $.post("http://127.0.0.1:8080/rest-category-list/", {
                category_name: $("#id_category_name").val(),
                category_description: $("#id_category_description").val()
            },
            function(data) {
                alert(data);
            });
        });
})();