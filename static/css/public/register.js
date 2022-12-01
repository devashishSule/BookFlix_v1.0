console.log("HelloWorld")

function show1() {
    var x = $("#pass1");
    if (x.attr('type') === "password") {
        x.attr('type', 'text')
    } else {
        x.attr('type', 'password')
    }
}

function show2() {
    var x = $("#pass2");
    if (x.attr('type') === "password") {
        x.attr('type', 'text')
    } else {
        x.attr('type', 'password')
    }
}

function show1() {
    var x = $("#pass1");
    if (x.attr('type') === "password") {
        x.attr('type', 'text')
    } else {
        x.attr('type', 'password')
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