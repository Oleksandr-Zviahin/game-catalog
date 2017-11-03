function getCategoryList() {
    $.ajax({
        url: "http://127.0.0.1:8080/rest-category-list/",
        success: function (result) {
            var categories = {"categories": result};
            var template = "<ul>" +
                "{{#categories}}" +
                "<li> <strong>{{category_name}}</strong> - {{category_description}} </li>" +
                "{{/categories}}" +
                "</ul>";
            var html = Mustache.to_html(template, categories);
            $("#category_list").html(html);
        }
    });
}

(function () {
    document.getElementById("get_category_list_button")
        .addEventListener("click", function () {
            getCategoryList();
        });
})();
