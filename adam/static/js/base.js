(function ($, window, document, undefined) {

    $('ul.expandable header.skill-group').on('click', function (e) {
        var innerList = $(e.target).parent().find('ul');

        innerList.slideToggle();
    });

})(jQuery, window, document);
