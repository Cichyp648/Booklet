from django import template

register = template.Library();

@register.simple_tag
def get_links():
    return [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house',
    }, {
        'name': 'News',
        'href': '/news/',
        'icon': 'fa-newspaper',
    }, {
        'name': 'Books',
        'href': '/books',
        'icon': 'fa-book',
    }, {
        'name': 'Movies',
        'href': '/movies',
        'icon': 'fa-video-camera',
    },{
        'name': 'Forum',
        'href': '/forum',
        'icon': 'fa-comments', #look for your icon here https://fontawesome.com/search?ic=free
    }, {
        'name': 'About Us',
        'href': '/about',
        'icon': 'fa-address-card',
    }, {
        'name': 'About our project',# nazwa wyświetlana na stronie
        'href': '/aboutproject',
        'icon': 'fa-info-circle', 
    }, {
        'name': 'Contact Us',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    },  {
        'name': 'Admin panel',
        'href': '/admin',
        'icon': 'fa-user',
    }
    ]
    