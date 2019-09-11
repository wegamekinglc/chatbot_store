from flask_appbuilder import Model
from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy import func

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class FaqCustomerService(Model):
    id = Column(Integer, primary_key=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    update_time = Column(DateTime, server_default=func.now())

