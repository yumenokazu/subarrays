$(document).ready(
    function()
    {
        $('#subarrays_form').submit(function(e) {
            e.preventDefault();
            ajaxSetup();
        });
    })

function ajaxSetup()
{
    var numbers = document.getElementsByName('numbers_input')[0];
    var target = document.getElementsByName('target_input')[0];
    if (numbers.value.length === 0) {
        return false;
    }
    if (target.value.length === 0)
    {
        target.value = target.placeholder;
    }
    $.post
    (
        '/',
        {
            numbers: numbers.value,
            target: target.value
        }
    ).fail(function(response, textStatus, errorThrown) {
        $('#hidden').text(errorThrown);
    }).done(function(response){
        $('#hidden').text('');
        $('.Result').html(response.data)
    })
}
