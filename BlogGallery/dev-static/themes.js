var themes = [
//    'cerulean',
    'cosmo',
//    'cyborg',
//    'darkly',
//    'flatly',
//    'journal',
    'litera',
    'lumen',
    'lux',
    'materia',
    'minty',
    'pulse',
    'sandstone',
    'simplex',
//    'sketchy',
    'slate',
    'solar',
    'spacelab',
    'superhero',
    'united',
    'yeti'
];


function updateNavbarClass(className) {
    $('nav')
        .removeClass(function (index, css) {
            return (css.match(/(^|\s)fixed-\S+/g) || []).join(' ');
        })
        .addClass(className);

    $('[data-class]').removeClass('active').parent('li').removeClass('active');
    $('[data-class="' + className + '"]').addClass('active').parent('li').addClass('active');

    fixBodyMargin(className);
}

function fixBodyMargin(className) {
    if (/fixed-(left|right)/.test(className)) {
        $('body').removeAttr('style');
        if (className === 'fixed-right') {
            $('body').css('marginLeft', 0);
        } else {
            $('body').css('marginRight', 0);
        }
    } else {
        $('body').css({
            "margin-right": 0,
            "margin-left": 0,
            "padding-top": '90px'
        });
    }
}

function selectTheme(theme) {
    console.log(theme);
    let r = new XMLHttpRequest();
    r.open('GET', 'http://127.0.0.1:8000/get_theme/' + theme);
    r.send();
    $('#theme_link').attr('href', 'https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.3.1/' + theme + '/bootstrap.min.css');
}
