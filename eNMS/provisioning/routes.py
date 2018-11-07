from flask import current_app as app, jsonify, render_template, request
from flask_login import current_user
from eNMS.provisioning.helpers import get_template_vars
from eNMS.provisioning import bp
from eNMS.base.helpers import get


@get(bp, '/test', 'Provisioning Section')
def test():

    template_vars = get_template_vars('snippets/test.j2')

    template_data = { x: "blablabla" for x in template_vars }

    rendering_result = render_template('snippets/test.j2', **template_data)

    return render_template(
        'test.html',
        rendering_result=rendering_result
    )

