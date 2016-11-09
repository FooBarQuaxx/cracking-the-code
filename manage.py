#!/usr/bin/env python

import jinja2
import sys


tmpl = """#!/usr/bin/env python
import pytest

def solution({% for param in params %}{{param}}{% if not loop.last %}, {%endif%}{% endfor %}):
    pass


@pytest.mark.parametrize("{% for param in params %}{{param}}, {% endfor %}expected", [
    ({% for param in params %}, {% endfor %}),
])
def test_solution({% for param in params %}{{param}}, {% endfor %}expected):
    assert expected == solution({% for param in params %}{{param}}{% if not loop.last%}, {%endif%}{% endfor %})
"""


def main(args):
    if len(args) == 0:
        return
    template = jinja2.Template(tmpl)
    print(template.render(params=args))


if __name__ == '__main__':
    main(sys.argv[1:])
