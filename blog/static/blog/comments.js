//$('.js-add-comment').click(function () {
//    $('.active-form').remove();
//    var $template = $('.form-template').clone(),
//        $this = $(this),
//    comment_id = $this.attr('comment_id');
//    $template.find('form').addClass('active-form').find('input[name="parent"]').val(comment_id);
//    $this.after($template.html());
//
//    return false
//});

$('body').on('click', '.js-add-comment',function () {
    $('.active-form').remove();
    var $template = $('.form-template').clone(),
        $this = $(this),
        comment_id = $this.attr('comment_id');
    $template.find('form').addClass('active-form').find('input[name="parent"]').val(comment_id);

    $this.after($template.html());
    $('.active-form').find('textarea[name="text"]').focus();
    return false
}).on('submit', '.active-form', function () {
    $(this).find('.errorlist').remove();
    var $text = $(this).find('textarea[name="text"]');

    if (!$text.val()) {
        $text.before('<ul class="errorlist"><li>Введите сообщение</li></ul>');
        return false
    }

});


