$('#btn-export').click(function () {
    $('#table_sv_id').table2excel({
        exclude: '.noExport',
        name: 'My doc',
        filename: 'Table_exp'
    });
});

$('#btn-export_dm').click(function () {
    $('#table_dm_id').table2excel({
        exclude: '.noExport',
        name: 'My doc',
        filename: 'Table_exp'
    });
});

$('#btn-export_shop').click(function () {
    $('#table_shop_id').table2excel({
        exclude: '.noExport',
        name: 'My doc',
        filename: 'Table_exp'
    });
});