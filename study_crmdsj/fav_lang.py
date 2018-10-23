from collections import OrderedDict

favor_lang = OrderedDict()

favor_lang['jen'] = 'python'
favor_lang['sarah']='c'
favor_lang['edward'] = 'ruby'

for name,language in favor_lang.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

