function tab_inv(shop, url) {
    $.ajax({
        method: 'GET',
        url: url,
        data: {
            'shop': shop
        },
        dataType: 'json',
        success: function (data) {
            console.log(data);
            $("#table_id tr").slice(1).remove();
            for (var i = 0; i < data.elements.length; i++) {
                var table_row = '<tr>' +
                    '<td class="util-table">' + data.elements[i].shop + '</td>' +
                    '<td>' + data.elements[i].date_inv + '</td>' +
                    '<td class="util-table">' + data.elements[i].vscro + '</td>' +
                    '<td>' + data.elements[i].type_inv + '</td>' +
                    '<td class="util-table">' + data.elements[i].dm_shop + '</td>' +
                    '<td class="util-table">' + data.elements[i].dm_shop_new + '</td>' +
                    '<td class="util-table">' + data.elements[i].sv_shop + '</td>' +
                    '<td>' + data.elements[i].res_main + '</td>' +
                    '<td>' + data.elements[i].res_defect + '</td>' +
                    '<td>' + data.elements[i].res_6_line + '</td>' +
                    '<td>' + data.elements[i].res_4_line + '</td>' +
                    '<td>' + data.elements[i].resort_001 + '</td>' +
                    '<td>' + data.elements[i].res_total + '</td>' +
                    '<td>' + data.elements[i].t_o + '</td>' +
                    '<td>' + data.elements[i].percent_of_to + '%' + '</td>' +
                    '<td>' + data.elements[i].previous_date +
                    '</td></tr><';

                $('table').append(table_row);
            }
        }
    });
}
