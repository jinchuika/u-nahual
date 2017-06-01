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
    $.get($('#nahual_form').attr('action'), {
        anno: $('#id_year').val(),
        mes: $('#id_month').val(),
        dia: $('#id_day').val(),
    }, function (data) {
        if (data.url) {
            window.location = data.url;
        }
    })
}

$(document).ready(function () {
    $('#nahual_form').on('submit', function (e) {
        e.preventDefault();
        consultar();
    });
});