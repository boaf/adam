(function ($, window, document, undefined) {

    $('ul.expandable header.skill-group').on('click', function (e) {
        var innerList = $(e.target).parent().find('ul');

        innerList.slideToggle();
    });

    $('a.openid-provider').on('click', function(e) {
        e.preventDefault();
        var url = $(this).attr('href')
        $('input[name=openid]').val(url);
    });

})(jQuery, window, document);
