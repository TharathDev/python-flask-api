from db import session


class BaseModel:
    def __init__(self):
        self._session = session()
        self._query = self._get_query()

    def _commit(self):
        self._session.commit()

    def _get_query(self):
        return self._session.query(self.__class__)

    def jsonify(self, model, schema, **kwargs):
        _schema = schema()
        return _schema.dump(model, **kwargs)

    def get_all(self, expression={}):
        search = self._query.filter_by(
            **{k: v for k, v in expression.items()
               if k not in ["username", "phone", "email"]
               }
        )
        for k in ["username", "phone", "email"]:
            exp = expression.get(k)
            if not exp:
                continue
            search = search.filter(getattr(self.__class__, k).like(f"%{exp}%"))
        return search.all()

    def get_by_id(self, id):
        return self._query.filter(self.__class__.id == id).one()

    def add(self):
        self._session.add(self)
        self._commit()

    def delete(self):
        self._session.delete(self)
        self._commit()
