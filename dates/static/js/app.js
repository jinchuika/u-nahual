function strToDate(dateStr)
{
    var dateTry = new Date(dateStr);

    if (!dateTry.getTime())
    {
        throw new Exception("Bad Date! dateStr: " + dateStr);
    }

    var tz = dateStr.trim().match(/(Z)|([+-](\d{2})\:?(\d{2}))$/);

    if (!tz)
    {
        var newTzOffset = dateTry.getTimezoneOffset() / 60;
        var newSignStr = (newTzOffset >= 0) ? '-' : '+';
        var newTz = newSignStr + ('0' + Math.abs(newTzOffset)).slice(-2) + ':00';

        dateStr = dateStr.trim() + newTz;
        dateTry = new Date(dateStr);

        if (!dateTry.getTime())
        {
            throw new Exception("Bad Date! dateStr: " + dateStr);
        }
    }

    return dateTry;
}

function consultar() {
    var fecha = $('#id_fecha').datepicker('getDate');
    $.get($('#nahual_form').attr('action'), {
        anno: fecha.getFullYear(),
        mes: fecha.getMonth() + 1,
        dia: fecha.getDate(),
    }, function (data) {
        if (data.url) {
            window.location = data.url;
        }
    })
}

$(document).ready(function () {
    $('#id_fecha').datepicker({
        language: 'es',
        autoclose: true,
        format: 'dd/mm/yyyy',
        enableOnReadonly: true
    });

    $('#nahual_form').on('submit', function (e) {
        e.preventDefault();
        console.log($('#id_fecha').val());
        consultar();
    });
});