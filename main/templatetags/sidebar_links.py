from django import template

register = template.Library();

@register.simple_tag
def get_links():
    return [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house',
    }, {
        'name': 'Books',
        'href': '/books',
        'icon': 'fa-book',
    }, {
        'name': 'Movies',
        'href': '/movies',
        'icon': 'fa-clapperboard',
    }, {
        'name': 'Contact',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    }, {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card',
    },{
        'name': 'News',
        'href': '/news/',
        'icon': 'fa-newspaper',
    },{
        'name': 'Add news',
        'href': '/news/create',
        'icon': 'fa-plus',
    },{
        'name': 'Forum',
        'href': '/forum',
        'icon': 'fa-comment', #look for your icon here https://fontawesome.com/search?ic=free
    }, {
        'name': 'About project',# nazwa wyświetlana na stronie
        'href': '/aboutproject',
        'icon': 'fa-diagram-project', 
    }]
    