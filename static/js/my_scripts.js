function formatdate_dd_mm_yy(date) {
    var day = date.substr(8);
    var month = date.substr(5, 2);
    var year = date.substr(0, 4);
    var result = day + '.' + month + '.' + year;
    return result
}

function formatdate_yy_mm_dd(date) {
    var day = date.substr(0,2);
    var month = date.substr(3,2);
    var year = date.substr(6);
    var result = year + '-' + month + '-' + day;
    return result
}
