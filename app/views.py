from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from .models import FaqCustomerService

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


class FaqCustomerServiceModelView(ModelView):
    datamodel = SQLAInterface(FaqCustomerService)

    label_columns = {'faq': 'FAQ'}
    list_columns = ['question', 'answer', 'update_time']

    show_fieldsets = [
        (
            'FAQ Info',
            {'fields': ['question', 'answer', 'update_time'], 'expanded': False}
        ),
    ]

    add_fieldsets = [
        (
            '问答组合',
            {'fields': ['question', 'answer'], 'expended': False}
        )
    ]


db.create_all()
appbuilder.add_view(
    FaqCustomerServiceModelView,
    "客户服务",
    icon="fa-envelope",
    category="知识库"
)
