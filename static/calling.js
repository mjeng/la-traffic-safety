function display() {
    $('.loop').html("Calling");
    loop(0);
}

function loop(i) {
    setTimeout((i) => {
        if (i % 4 == 0) {
            $('.loop').html("Calling .");
        } else {
            $('.loop').html($('.loop').html() + " .");
        }
        loop(i + 1);
    }, 600, i);
}


window.onload = display;