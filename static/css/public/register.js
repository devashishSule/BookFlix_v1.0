console.log("HelloWorld")

function show1() {
    // console.log("HelloWorld")
    var x = $("#pass1");
    // console.log(x.type)

    if (x.attr('type') === "password") {
        x.attr('type', 'text')
    } else {
        x.attr('type', 'password')
    }
}

function show2() {
    var y = $("#pass2");
    // console.log(y.type)

    if (y.attr('type') === "password") {
        y.attr('type', 'text')
    } else {
        y.attr('type', 'password')
    }
}

function verify() {
    var a = $("#pass1").val();
    var b = $("#pass2").val();
    if (a == b) {
        return alert('Registeration Successful...');
    } else {
        return alert('Password entered does not match. Please fill out again')
    }
}