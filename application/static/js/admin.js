webix.ui({
    rows: [{
        template: "Header"
    }, {
        cols: [{
                template: "List"
            },
            {
                view: "datatable",
                id: "film_list",
                scroll: "y",
                autoConfig: true,
                data: small_film_set
            }, {
                template: "Form"
            }
        ]
    }, {
        template: "Footer"
    }]
});
$.ajax({
    type: "get",
    url: "./api/v1.0/user",
    data: {

    },
    success: {
        function(result) {
            console.log("sucess");
            console.log(result);


        }

    },
    error: {
        function(result) {
            console.log("error");
            console.log(result);
            console.log(result.responseText);
        }
    }
});