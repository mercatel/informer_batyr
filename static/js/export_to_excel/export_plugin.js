$('#btn-export').click(function () {
    $('#table_id').table2excel({
        exclude: '.noExport',
        name: 'My doc',
        filename: 'Table_exp',
    });
});
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




$('#btn-export_mk_report').click(function () {
    $('#table_mk_report').table2excel({
        exclude: '.noExport',
        name: 'My doc',
        filename: 'Table_exp',
        exclude_links: true,
    });
});

$('#btn-export_report_etc').click(function () {
    $('#table_mk_report_etc').table2excel({
        exclude: '.noExport',
        name: 'My doc',
        filename: 'Table_exp'
    });
});