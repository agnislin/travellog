$(function () {
    $(".js-upload-photos").click(function () {
        url = $("#fileupload")[0].dataset["url"]
        url = url.substr(0, url.length - 1)
        $("#fileupload")[0].dataset["url"] = url + '?name="'+ $("#name").val() + '"&desc="' + $("#description").val() + '"';
        alert($("#fileupload")[0].dataset["url"]);
        $("#fileupload").click();
    });


    $("#fileupload").fileupload({
        sequentialUploads: true,


        start: function (e) {
            $("#modal-progress").modal("show");
        },

        stop: function (e) {
            $("#modal-progress").modal("hide");
        },

        progressall: function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            var strProgress = progress + "%";
            $(".progress-bar").css({"width": strProgress});
            $(".progress-bar").text(strProgress);
        },

        done: function (e, data) {
            if (data.result.is_valid) {
                $("#gallery tbody").prepend(
                    "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
                )
            }
        }
    });
});
