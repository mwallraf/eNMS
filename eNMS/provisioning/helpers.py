from flask import current_app as app
from jinja2 import meta


def get_template_vars(templatename, ignorevars=[], sort=True, maxnestlevels=100):
    """Return a list of all variables found in the template


    Arguments:

        ignorevars  -- a list of variables that are removed from the output
        sort        -- True (default) or False if returned list should be sorted
        maxnestlevels -- a positve integer which defines how deep you can nest templates with includes
    """

    tplvars = []
    templates = []
    templatesseen = []
    nestlevels = 0

    env = app.jinja_env

    templates.append(templatename)
    templatesseen.append(templatename)

    while len(templates) > 0:
        tpl = templates.pop()
        nested = False

        tplsrc = env.loader.get_source(env, tpl)[0]
        ast = env.parse(tplsrc)

        for template in meta.find_referenced_templates(ast):
            if template in templatesseen:
                raise Exception("Template loop detected: \"{}\" references \"{}\" which was seen earlier".format(tpl, template))
            else:
                templates.append(template)
                templatesseen.append(template)
                nested = True

        for e in meta.find_undeclared_variables(ast):
            if not e in ignorevars:
                tplvars.append(e)

        if nested and nestlevels >= maxnestlevels:
            raise Exception("Maximum template nesting depth of {} reached in template {}".format(maxnestlevels, template))
        else:
            nestlevels += 1

    if sort:
        return sorted(tplvars)
    else:
        return tplvars

# def get_unset_template_vars(ignorevars=[]):
#     """Return a list of variables that have no assigned value
# 
#     Arguments:
#         ignorevars  -- a list of variables that are removed from the output
#     """
#     tplvars = get_template_vars()
# 
#     return [e for e in tplvars if not e in self.variables]
