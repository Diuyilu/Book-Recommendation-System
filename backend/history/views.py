from sqlalchemy import func

from history.models import History
from history.serializers import history_serializer


def getHistoryInfo(Resource):
    def get(self):
        history = History.query.order_by(func.random()).limit(10)
        return history_serializer(history)