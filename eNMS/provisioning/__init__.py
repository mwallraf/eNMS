from flask import Blueprint

bp = Blueprint(
    'provisioning_blueprint',
    __name__,
    url_prefix='/provisioning',
    template_folder='templates',
    static_folder='static'
)

#from eNMS.base.helpers import add_classes
#from eNMS.objects.models import Device, Link, Pool

#add_classes()

import eNMS.provisioning.routes  # noqa: F401
