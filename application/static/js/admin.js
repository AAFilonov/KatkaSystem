$.ajax({
    type: "get",
    url: "./api/v1.0/user",
    data: {

    },
    success: succes_handler,
    error: {
        function(result) {
            console.log("error");
            console.log(result);
            console.log(result.responseText);
        }
    }
});

function succes_handler(result) {
    console.log("sucess");
    console.log(result);
    webix.ui({
        rows: [
            { view: "template", type: "header", template: "My App!" },
            { view: "datatable", autoConfig: true, data: result['users'] }
        ]
    });
}