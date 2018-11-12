from flask import current_app as app, jsonify, render_template, render_template_string, request
from flask_login import current_user
from eNMS.provisioning.helpers import get_template_vars, get_all_snippets
from eNMS.provisioning import bp
from eNMS.base.helpers import get


@get(bp, '/test', 'Provisioning Section')
def test():

    snippets = get_all_snippets(bp)
    print(snippets)

    tpl_source = snippets['snippets/test.j2']['template']
    tpl_vars = { x: 'blablabla' for x in snippets['snippets/test.j2']['vars'] }

    rendering_result = render_template_string(tpl_source, **tpl_vars)

    return render_template(
        'test.html',
        rendering_result=rendering_result
    )

# -----

@get(bp, '/', 'Provisioning Section')
def provisioning():

    snippets = get_all_snippets(bp)
    #print(snippets)

    tpl_source = snippets['snippets/test.j2']['template']
    tpl_vars = { x: 'blablabla' for x in snippets['snippets/test.j2']['vars'] }

    rendering_result = render_template_string(tpl_source, **tpl_vars)

    return render_template(
        'provisioning.html',
        snippets=snippets,
        rendering_result=rendering_result
    )
