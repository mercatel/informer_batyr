function ajax_filter(start, end, url) {
    $.ajax({
        method: 'GET',
        url: url,
        data: {
            'start': start,
            'end': end,
        },
        dataType: 'json',
        success: function (data) {
            console.log(data);
            $("#table_sv_id tr").slice(1).remove();
            $("#table_dm_id tr").slice(1).remove();
            $("#table_shop_id tr").slice(1).remove();
            var itog_scu = 0;
            var itog_p2_1 = 0;
            var itog_p2_sum = 0;
            var itog_lack_price = 0;
            var itog_dis_price = 0;
            var itog_etc = 0;


            for (var j = 0; j < data.onsv.length; j++) {
                itog_scu += parseInt(data.onsv[j].sku);
                itog_p2_1 += parseInt(data.onsv[j].p2_1);
                itog_p2_sum += parseFloat(data.onsv[j].p2_sum);
                itog_lack_price += parseInt(data.onsv[j].lack_price);
                itog_dis_price += parseInt(data.onsv[j].dis_price);
                itog_etc += parseInt(data.onsv[j].etc);
                var table_row_sv = '<tr>' +
                    '<td class="util-table">' + data.onsv[j].sv + '</td>' +
                    '<td>' + data.onsv[j].sku + '</td>' +
                    '<td>' + data.onsv[j].p2_1 + '</td>' +
                    '<td>' + data.onsv[j].p2_sum + '</td>' +
                    '<td>' + data.onsv[j].lack_price + '</td>' +
                    '<td>' + data.onsv[j].dis_price + '</td>' +
                    '<td>' + data.onsv[j].etc + '</td>' +
                    '</tr>';

                $('#table_sv_id').append(table_row_sv);
            }
            var table_itog_sv = '<tbody><tr>' +
                '<td class="util-table">' + "Итого:" + '</td>' +
                '<td>' + itog_scu + '</td>' +
                '<td>' + itog_p2_1 + '</td>' +
                '<td>' + parseFloat(itog_p2_sum) + '</td>' +
                '<td>' + itog_lack_price + '</td>' +
                '<td>' + itog_dis_price + '</td>' +
                '<td>' + itog_etc + '</td>' +
                '</tr></tbody>';
            $('#table_sv_id').append(table_itog_sv);

            for (var i = 0; i < data.ondm.length; i++) {
                var table_row_dm = '<tr>' +
                    '<td>' + data.ondm[i].dm + '</td>' +
                    '<td>' + data.ondm[i].shop + '</td>' +
                    '<td>' + data.ondm[i].address + '</td>' +
                    '<td>' + formatdate_dd_mm_yy(data.ondm[i].date) + '</td>' +
                    '<td>' + data.ondm[i].sv + '</td>' +
                    '<td>' + data.ondm[i].sum_scu + '</td>' +
                    '<td>' + data.ondm[i].sum_p2_1 + '</td>' +
                    '<td>' + data.ondm[i].sum_summ + '</td>' +
                    '<td>' + data.ondm[i].sum_dis_price + '</td>' +
                    '<td>' + data.ondm[i].sum_lack_price + '</td>' +
                    '<td>' + data.ondm[i].sum_etc + '</td>' +
                    '</tr>';
                $('#table_dm_id').append(table_row_dm);
            }
            var table_itog_sv = '<tbody><tr>' +
                '<td class="util-table">' + "Итого:" + '</td>' +
                '<td></td>' + '<td></td>' + '<td></td>' + '<td></td>' +
                '<td>' + itog_scu + '</td>' +
                '<td>' + itog_p2_1 + '</td>' +
                '<td>' + parseFloat(itog_p2_sum) + '</td>' +
                '<td>' + itog_lack_price + '</td>' +
                '<td>' + itog_dis_price + '</td>' +
                '<td>' + itog_etc + '</td>' +
                '</tr></tbody>';
            $('#table_dm_id').append(table_itog_sv);


            for (var i = 0; i < data.ondm.length; i++) {
                var table_row_shop = '<tr>' +
                    '<td>' + data.ondm[i].shop + '</td>' +
                    '<td>' + data.ondm[i].sum_scu + '</td>' +
                    '</tr>';
                $('#table_shop_id').append(table_row_shop);

            }
            var table_itog_shop = '<tbody><tr>' +
                '<td>' + "Итого:" + '</td>' +
                '<td>' + itog_scu + '</td>' +
                '</tr></tbody>';
            $('#table_shop_id').append(table_itog_shop);
        }
    });
}


