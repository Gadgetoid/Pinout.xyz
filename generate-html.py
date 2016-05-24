#!/usr/bin/env python
import markdown
import unicodedata
import re
import os
import sys
import pinout
import markjaml
import urlmapper

reload(sys)
sys.setdefaultencoding('utf8')



lang = "en"
default_strings = {
    'made_by': 'Made by {manufacturer}',
    'type_hat': 'HAT form-factor',
    'type_classic': 'Classic form-factor',
    'pin_header': '{} pin header',
    'uses_i2c': 'Uses I2C',
    'wiring_pi_pin': 'Wiring Pi pin {}',
    'uses_n_gpio_pins': 'Uses {} GPIO pins',
    'bcm_pin_rev1_pi': 'BCM pin {} on Rev 1 ( very early ) Pi',
    'physical_pin_n': 'Physical pin {}',
    'more_information': 'More Information',
    'github_repository': 'GitHub Repository',
    'buy_now': 'Buy Now',
    'group_multi': 'Multi',
    'group_led': 'LED',
    'group_iot': 'IOT',
    'group_instrument': 'Instrument',
    'group_lcd': 'LCD',
    'group_other': 'Other',
    'group_motor': 'Motor',
    'group_audio': 'Audio',
    'group_gesture': 'Gesture',
    'group_pinout': 'Pinout',
    'group_info': 'Info',
    'group_featured': 'Featured'
}



def cssify(value):
    value = slugify(value);
    if value[0] == '3' or value[0] == '5':
        value = 'pow' + value

    return value


def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '_', value)


def load_overlay(overlay):
    try:
        data = markjaml.load('src/{}/overlay/{}.md'.format(lang, overlay))

        loaded = data['data']
        loaded['long_description'] = data['html']
    except IOError:
        return None

    '''
    If this is not an info page, then build a collection of details and append them to long_description
    '''
    if 'type' not in loaded or loaded['type'] != 'info':
        details = []

        if 'type' not in loaded:
            loaded['type'] = 'addon'

        if 'manufacturer' in loaded:
            details.append(strings['made_by'].format(manufacturer=loaded['manufacturer']))

        if 'pincount' in loaded:
            '''
            Choose correct board type to be displayed based upon pincount and form factor.
            This could be a HAT, a pHAT or other...
            '''
            pincount = int(loaded['pincount'])
            if 'formfactor' in loaded:
                formfactor = str(loaded['formfactor'])
                if pincount == 40 and formfactor == 'HAT':
                    details.append(strings['type_hat'])
                elif pincount == 40 and formfactor == 'pHAT':
                    details.append(strings['type_phat'])
                elif pincount == 40 and formfactor == '40-way':
                    details.append(strings['pin_header'].format(pincount))
                else:
                    details.append(strings['pin_header'].format(pincount))
            elif pincount == 40:
                details.append(strings['type_hat'])
            elif pincount == 26:
                details.append(strings['type_classic'])
            else:
                details.append(strings['pin_header'].format(pincount))

        '''
        If the overlay includes a collection of pins then
        loop through them and count how many non-power pins are used
        '''
        if 'pin' in loaded:
            uses = 0
            for pin in loaded['pin']:
                pin = str(pin)
                if pin.startswith('bcm'):
                    pin = pinout.bcm_to_physical(pin[3:])

                if pin in pinout.pins:
                    actual_pin = pinout.pins[pin]

                    if actual_pin['type'] in ['+3v3', '+5v', 'GND'] and overlay != 'ground':
                        raise Exception(
                            "{} includes a reference to a {} pin, which isn't allowed".format(overlay, actual_pin['type']))
                    else:
                        uses += 1

            if uses > 0:
                details.append(strings['uses_n_gpio_pins'].format(uses))

            '''
            If the collection of pins includes pins 3 and 5 in i2c mode, then
            assume the board uses i2c communication
            '''
            if '3' in loaded['pin'] and '5' in loaded['pin']:
                pin_3 = loaded['pin']['3']
                pin_5 = loaded['pin']['5']
                if 'mode' in pin_3 and 'mode' in pin_5:
                    if pin_3['mode'] == 'i2c' and pin_5['mode'] == 'i2c':
                        details.append(strings['uses_i2c'])

        # A URL to more information about the add-on board, could be a GitHub readme or an about page
        if 'url' in loaded:
            details.append('[{text}]({url})'.format(text=strings['more_information'], url=loaded['url']))

        # Should only ever be a URL to the github repository with code supporting the product
        if 'github' in loaded:
            details.append('[{text}]({url})'.format(text=strings['github_repository'], url=loaded['github']))

        # A URL to a preferred place to buy the add-on board
        if 'buy' in loaded:
            details.append('[{text}]({url})'.format(text=strings['buy_now'], url=loaded['buy']))

        loaded['long_description'] = '{}\n{}'.format(loaded['long_description'],
                                                    markdown.markdown('\n'.join(map(lambda d: '* ' + d, details))))

    # Automatically generate a page slug from the name if none is specified
    if 'page_url' not in loaded:
        loaded['page_url'] = slugify(loaded['name'])

    loaded['rendered_html'] = render_overlay_page(loaded)
    loaded['src'] = overlay
    pages[loaded['page_url']] = loaded
    navs[loaded['page_url']] = render_nav(loaded['page_url'], overlay=loaded)

    return loaded


def load_md(filename):
    filename = 'src/{}/{}'.format(lang, filename)
    try:
        html = markdown.markdown(open(filename).read(), extensions=['fenced_code'])

        return html
    except IOError:
        print('!! Unable to load markdown from {}'.format(filename))
        return ''


def render_pin_text(pin_num, pin_url, pin_name, pin_functions, pin_subtext):
    return '<article class="{pin_url}"><h1>{pin_name}</h1>{pin_functions}{pin_subtext}{pin_text}</article>'.format(
        pin_url=pin_url,
        pin_name=pin_name,
        pin_functions=pin_functions,
        pin_subtext=pin_subtext,
        pin_text=load_md('pin/pin-{}.md'.format(pin_num)))


def render_overlay_page(overlay):
    if overlay is None:
        return ''
    return '<article class="page_{}">{}</article>'.format(slugify(overlay['name']), overlay['long_description'])


def render_alternate(handle, name):
    handle = slugify(handle.lower())
    return '<span class="alternate legend_{}">{}</span>'.format(handle, name)


def render_pin_page(pin_num):
    pin = pinout.pins[str(pin_num)]
    pin_url = pin['name']

    if pin_url == 'Ground':
        return None, None, None

    pin_text_name = pin['name']

    pin_subtext = []

    pin_subtext.append(strings['physical_pin_n'].format(pin_num))

    if 'scheme' in pin:
        if 'bcm' in pin['scheme']:
            bcm = pin['scheme']['bcm']
            pin_url = 'gpio{}'.format(bcm)

            pin_text_name = 'BCM {}'.format(bcm)

            pin_subtext.append('BCM pin {}'.format(bcm))
        if 'wiringpi' in pin['scheme']:
            wiringpi = pin['scheme']['wiringpi']
            pin_subtext.append('Wiring Pi pin {}'.format(wiringpi))
        if 'bcmAlt' in pin['scheme']:
            bcmAlt = pin['scheme']['bcmAlt']
            pin_subtext.append(strings['bcm_pin_rev1_pi'].format(bcmAlt))

    if 'description' in pin:
        pin_text_name = '{} ({})'.format(pin_text_name, pin['description'])

    fn_headings = []
    fn_functions = []
    pin_functions = ''
    if 'functions' in pin:
        for x in range(6):
            fn_headings.append('Alt' + str(x))

            function = ''
            if 'alt' + str(x) in pin['functions']:
                function = pin['functions']['alt' + str(x)]

            fn_functions.append(function)

        pin_functions = '''<table class="pin-functions">
		<thead>
			<tr>
				<th>{headings}</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>{functions}</td>
			</tr>
		</tbody>
		</table>'''.format(headings='</th><th>'.join(fn_headings), functions='</td><td>'.join(fn_functions))

    pin_url = slugify('pin{}_{}'.format(pin_num, pin_url))

    pin_text = render_pin_text(
        pin_num,
        pin_url,
        pin_text_name,
        pin_functions,
        '<ul><li>{}</li></ul>'.format('</li><li>'.join(pin_subtext))
    )
    # if pin_text != None:
    return pin_url, pin_text, pin_text_name  # pages[pin_url] = pin_text


def render_pin(pin_num, selected_url, overlay=None):
    pin = pinout.pins[str(pin_num)]

    pin_type = list([x.strip() for x in pin['type'].lower().split('/')])
    pin_url = pin['name']
    pin_name = pin['name']
    pin_used = False
    pin_link_title = []
    bcm_pin = None
    if 'scheme' in pin:
        if 'bcm' in pin['scheme']:
            bcm_pin = 'bcm' + str(pin['scheme']['bcm'])

    if overlay is not None and (
                        pin_num in overlay['pin'] or str(pin_num) in overlay['pin'] or bcm_pin in overlay['pin']):

        if pin_num in overlay['pin']:
            overlay_pin = overlay['pin'][pin_num]
        elif str(pin_num) in overlay['pin']:
            overlay_pin = overlay['pin'][str(pin_num)]
        else:
            overlay_pin = overlay['pin'][bcm_pin]

        if overlay_pin is None:
            overlay_pin = {}

        pin_used = True

        if 'name' in overlay_pin:
            pin_name = overlay_pin['name']

        if 'description' in overlay_pin:
            pin_link_title.append(overlay_pin['description'])

    if 'scheme' in pin:
        if 'bcm' in pin['scheme']:
            bcm = pin['scheme']['bcm']
            pin_subname = ''

            pin_url = 'gpio{}'.format(bcm)
            if pin_name != '':
                pin_subname = '<small>({})</small>'.format(pin_name)
            pin_name = 'BCM {} {}'.format(bcm, pin_subname)
        if 'wiringpi' in pin['scheme']:
            wiringpi = pin['scheme']['wiringpi']
            pin_link_title.append(strings['wiring_pi_pin'].format(wiringpi))

    pin_url = base_url + slugify('pin{}_{}'.format(pin_num, pin_url))

    if pin['type'] in pinout.get_setting('urls'):
        pin_url = base_url + pinout.get_setting('urls')[pin['type']]

    selected = ''

    if base_url + selected_url == pin_url:
        selected = ' active'
    if pin_used:
        selected += ' overlay-pin'

    pin_url = pin_url + url_suffix

    return '<li class="pin{pin_num} {pin_type}{pin_selected}"><a href="{pin_url}" title="{pin_title}"><span class="default"><span class="phys">{pin_num}</span> {pin_name}</span><span class="pin"></span></a></li>\n'.format(
        pin_num=pin_num,
        pin_type=' '.join(map(cssify, pin_type)),
        pin_selected=selected,
        pin_url=pin_url,
        pin_title=', '.join(pin_link_title),
        pin_name=pin_name,
        langcode=lang
    )


def render_nav(url, overlay=None):
    html_odd = ''
    html_even = ''
    for odd in range(1, len(pinout.pins), 2):
        html_odd += render_pin(odd, url, overlay)
        html_even += render_pin(odd + 1, url, overlay)

    return '''<ul class="bottom">
{}</ul>
<ul class="top">
{}</ul>'''.format(html_odd, html_even)


def get_hreflang_urls(src):
    hreflang = []
    for lang in sorted(alternate_urls):
        if src in alternate_urls[lang]:
            url = alternate_urls[lang][src]
            hreflang.append('<link rel="alternate" href="{url}" hreflang="{lang}"/>'.format(
                lang=lang,
                url=url
            ))
    return hreflang


def get_lang_urls(src):
    urls = []
    for url_lang in sorted(alternate_urls):
        if src in alternate_urls[url_lang]:
            img_css = ''
            if url_lang == lang:
                img_css = ' class="grayscale"'
            url = alternate_urls[url_lang][src]
            urls.append(
                '<li><a href="{url}" rel="alternate" hreflang="{lang}"><img{css} src="{resource_url}{lang}.png" /></a>'.format(
                    lang=url_lang,
                    url=url,
                    resource_url=resource_url,
                    css=img_css
                ))
    return urls


'''
Main Program Flow
'''

if len(sys.argv) > 1:
    lang = sys.argv[1]

alternate_urls = urlmapper.generate_urls(lang)

pinout.load(lang)

overlays = pinout.settings['overlays']

strings = pinout.get_setting('strings', {})

if type(strings) == list:
    _strings = {}
    for item in strings:
        _strings[item.keys()[0]] = item.values()[0]
    strings = _strings

for key, val in default_strings.items():
    if key not in strings:
        strings[key] = val

base_url = pinout.get_setting('base_url', '/pinout/')  # '/pinout-tr/pinout/'
resource_url = pinout.get_setting('resource_url', '/resources/')  # '/pinout-tr/resources/'
url_suffix = pinout.get_setting('url_suffix', '')  # '.html'

template = open('src/{}/template/layout.html'.format(lang)).read()

pages = {}
navs = {}

overlays_html = []

nav_html = {}

if not os.path.isdir('output'):
    try:
        os.mkdir('output')
    except OSError:
        exit('Failed to create output dir')
if not os.path.isdir('output/{}'.format(lang)):
    try:
        os.mkdir('output/{}'.format(lang))
    except OSError:
        exit('Failed to create output/{} dir'.format(lang))
if not os.path.isdir('output/{}/pinout'.format(lang)):
    try:
        os.mkdir('output/{}/pinout'.format(lang))
    except OSError:
        exit('Failed to create output/{}/pinout dir'.format(lang))

overlays = map(load_overlay, overlays)
overlay_subnav = ['featured']
featured_boards = []

'''
Build up the navigation between overlays. This needs to be done before rendering pages
as it's used in every single page.

overlays_html is generated with all types for legacy reasons
'''
for overlay in overlays:
    #image = None

    #if 'image' in overlay:
    #    image = overlay['image']
    
    link = (overlay['page_url'], overlay['name'])

    overlays_html += [link]

    if overlay['src'] in pinout.settings['featured'] and 'image' in overlay and len(featured_boards) < 3:
        featured_boards.append(overlay)

    if 'class' in overlay and 'type' in overlay:
        o_class = overlay['class']
        o_type = overlay['type']

        if o_class not in nav_html:
            nav_html[o_class] = {}

        if o_type not in nav_html[o_class]:
            nav_html[o_class][o_type] = []

        if o_class == 'board' and o_type not in overlay_subnav:
            overlay_subnav.append(o_type)

        nav_html[o_class][o_type] += [overlay]



featured_boards_html = ''
for overlay in featured_boards:
    featured_boards_html += '<div class="featured"><a href="{base_url}{page_url}"><img src="{resource_url}boards/{image}" /><strong>{name}</strong><span>{description}</span></a></div>'.format(
            image=overlay['image'],
            name=overlay['name'],
            page_url=overlay['page_url'],
            base_url=base_url,
            resource_url=resource_url,
            description=overlay['description']
        )

featured_boards_html = '<div class="group group_featured">' + featured_boards_html + '</div>'

'''
Generate legacy navigation menu for all overlays in a single drop-down
'''
overlays_html.sort()
overlays_html = ''.join(map(lambda x: '<li><a href="{}{}">{}</a></li>'.format(base_url, x[0], x[1]), overlays_html))

'''
Generate the new categorised navigation menu
'''
overlay_subnav = ''.join(map(lambda overlay_type: '<li class="group_{cls}" data-group="{cls}">{text}</li>'.format(cls=overlay_type,text=strings['group_' + overlay_type]),overlay_subnav))

for overlay_type in nav_html.keys():
    for overlay_group, items in nav_html[overlay_type].iteritems():
        items.sort()
        featured = [x for x in items if 'image' in x]
        regular = [x for x in items if 'image' not in x]

        group_items = ''

        group_items_pictures = (''.join(map(lambda x: '<li class="featured"><a href="{base_url}{page_url}"><img src="{resource_url}boards/{image}" /><strong>{name}</strong><span>{description}</span></a></li>'.format(
            image=x['image'],
            name=x['name'],
            page_url=x['page_url'],
            base_url=base_url,
            resource_url=resource_url,
            description=x['description']), featured)))

        group_items_normal = (''.join(map(lambda x: '<li><a href="{}{}">{}</a></li>'.format(base_url, x['page_url'], x['name']), regular)))

        group_items = group_items_pictures + group_items_normal

        if len(featured) > 0 and len(regular) > 0:
                group_items = group_items_pictures + '<hr />' + group_items_normal

        nav_html[overlay_type][overlay_group] = '<div class="group group_' + overlay_group + '"><ul>' + group_items + '</ul></div>'
    nav_html[overlay_type] = ''.join(nav_html[overlay_type].values())
    
    if overlay_type == 'board':
        nav_html[overlay_type] = '<div class="group-nav"><ul>' + overlay_subnav + '</ul></div>' + featured_boards_html + nav_html[overlay_type]


print(nav_html)

'''
Manually add the index page as 'pinout', this is due to how the
website is currently structured with /pinout as the index
and all other pages in /pinout/

serve.py will mirror this structure for testing.
'''
pages['index'] = {}
pages['index']['rendered_html'] = render_overlay_page({'name': 'Index', 'long_description': load_md('index.md')})
navs['index'] = render_nav('pinout')

'''
Add the 404 page if 404.md is present.
'''
page404 = load_md('404.md')
if page404 is not None:
    pages['404'] = {}
    pages['404']['rendered_html'] = render_overlay_page({'name': '404', 'long_description': page404})
    navs['404'] = render_nav('pinout')


print('\nRendering pin pages...')

for pin in range(1, len(pinout.pins) + 1):
    (pin_url, pin_html, pin_title) = render_pin_page(pin)
    if pin_url is None:
        continue

    hreflang = get_hreflang_urls('pin{}'.format(pin))
    langlinks = get_lang_urls('pin{}'.format(pin))

    pin_nav = render_nav(pin_url)
    pin_html = pinout.render_html(template,
                                  lang_links="\n\t\t".join(langlinks),
                                  hreflang="\n\t\t".join(hreflang),
                                  nav=pin_nav,
                                  content=pin_html,
                                  resource_url=resource_url,
                                  overlays=overlays_html,
                                  description=pinout.settings['default_desc'],
                                  title=pin_title + pinout.settings['title_suffix'],
                                  langcode=lang,
                                  nav_html=nav_html
                                  )

    print('>> pinout/{}.html'.format(pin_url))

    with open(os.path.join('output', lang, 'pinout', '{}.html'.format(pin_url)), 'w') as f:
        f.write(pin_html)


print('\nRendering overlay and index pages...')

for url in pages:
    content = pages[url]['rendered_html']
    nav = navs[url]
    hreflang = []
    langlinks = []

    if url == 'index':
        hreflang = get_hreflang_urls('index')
        langlinks = get_lang_urls('index')

    if 'src' in pages[url]:
        src = pages[url]['src']
        hreflang = get_hreflang_urls(src)
        langlinks = get_lang_urls(src)

    if not 'description' in pages[url]:
        pages[url]['description'] = pinout.settings['default_desc']

    if 'name' in pages[url]:
        pages[url]['name'] = pages[url]['name'] + pinout.settings['title_suffix']
    else:
        pages[url]['name'] = pinout.settings['default_title']

    html = pinout.render_html(template,
                              lang_links="\n\t\t".join(langlinks),
                              hreflang="\n\t\t".join(hreflang),
                              nav=nav,
                              content=content,
                              overlays=overlays_html,
                              resource_url=resource_url,
                              description=pages[url]['description'],
                              title=pages[url]['name'],
                              langcode=lang,
                              nav_html=nav_html
                              )

    if url != 'index' and url != '404':
        url = os.path.join('pinout', url)

    print('>> {}.html'.format(url))

    with open(os.path.join('output', lang, '{}.html'.format(url)), 'w') as f:
        f.write(html)

print('\nAll done!')
