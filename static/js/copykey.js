function copy() {
    $('button').on('click', function () {
        var id_btn = this.id;
        var td_copy = "t" + id_btn;

        var code = document.querySelector('#' + td_copy); // #text - блок из которого нужно скопировать
        var range = document.createRange();
        range.selectNode(code);
        window.getSelection().addRange(range);

        try {
            var successful = document.execCommand('copy');
            var msg = successful ? 'удачно' : 'неудачно';

        } catch (err) {

        }
        window.getSelection().removeAllRanges();
    });

}