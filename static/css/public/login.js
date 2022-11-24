function show() {
    var x = $("#pass");
    if (x.attr('type') === "password") {
        x.attr('type', 'text')
    } else {
        x.attr('type', 'password')
    }
}