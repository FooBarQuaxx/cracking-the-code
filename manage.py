#!/usr/bin/env python

from jinja2 import Environment
import sys
import argparse

tmpl = """#!/usr/bin/env python
{% for import in imports %}{{render_import(import)}}{% endfor %}

def solution({% for param in params %}{{param}}{% if not loop.last %}, {%endif%}{% endfor %}):
    pass


@pytest.mark.parametrize("{% for param in params %}{{param}}, {% endfor %}expected", [
    # ({% for param in params %}, {% endfor %}),
])
def test_solution({% for param in params %}{{param}}, {% endfor %}expected):
    assert expected == solution({% for param in params %}{{param}}{% if not loop.last%}, {%endif%}{% endfor %})
"""


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('params', nargs='*')
    parser.add_argument('--imports')
    return parser.parse_args()


def render_import(value):
    _import = value
    if '.' in _import:
        module, thing = '.'.join(_import.split('.')[:-1]), _import.split('.')[-1]
        return "from {module} import {thing}\n".format(module=module, thing=thing)
    else:
        return "import {thing}\n".format(thing=_import.strip())


def main(argv):
    opts = parse_args(argv)
    imports = ['pytest']
    imports += opts.imports.split(',') if opts.imports else []
    params = opts.params

    env = Environment()
    template = env.from_string(tmpl)
    env.globals.update(render_import=render_import)
    print(template.render(params=params, imports=imports))


if __name__ == '__main__':
    main(sys.argv[1:])
