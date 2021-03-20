"""
run as python script:
    python ./scripts/test_script.py
"""
if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.join(os.path.abspath('..'), ''))
    sys.path.append(os.path.join(os.path.abspath('..'), ''))
    sys.path.append(os.path.join(os.path.abspath('..'), ''))

    print('-'*10, 'sys.path', '-'*10)
    for path in sys.path:
        print('(%s)' % path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.local'

    import django
    django.setup()


from finoitpms import pylogging


if __name__ == '__main__':
    print('START %s' %('-' * 40))
    pylogging.logger.info('START %s' %('-' * 40))

    data = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
    pylogging.logger_info("info: %s" %(data))

    print('END %s' %('=' * 40))
    pylogging.logger.info('END %s' %('=' * 40))
