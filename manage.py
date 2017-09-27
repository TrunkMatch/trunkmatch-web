#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trunkmatch.settings")

    from django.core.management import execute_from_command_line

    if 'SERVERTYPE' not in os.environ:
        import json
        import os

        json_data = open('zappa_settings.json')
        env_vars = json.load(json_data)['dev']['environment_variables']
        for key, val in env_vars.items():
            os.environ[key] = val

    execute_from_command_line(sys.argv)
