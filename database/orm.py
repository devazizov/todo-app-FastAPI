import logging
from sqlalchemy.exc import IntegrityError
from .models import Todo
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

object_type_hint = Todo
object_type_hints = list[Todo] | list


class ORMBase:
    def __init__(self, model):
        self.model = model

    def get(self, db: Session, id: int) -> object_type_hint:
        return db.query(self.model).filter(self.model.id == id).first()

    def create(self, db: Session, **object_data: dict) -> object_type_hint:
        try:
            object_data = self.model(**object_data)
            db.add(object_data)
            db.commit()
            db.refresh(object_data)
            return object_data
        except IntegrityError:
            logging.info("Already exists")

        except Exception as e:
            logging.error(f"An error occurred: {e}")

    def update(self, db: Session, id: int, **updated_data: dict) -> object_type_hint:
        try:
            object = db.query(self.model).get(id)

            if not object:
                raise Exception(f"{self.model.__name__} with id {id} not found")

            for key, value in updated_data.items():
                if hasattr(object, key):
                    setattr(object, key, value)

            db.commit()
            return object
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise

    def delete(self, db: Session, id: int) -> object_type_hint:
        try:
            object = db.query(self.model).get(id)

            if object is not None:
                db.delete(object)
                db.commit()
                return True

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return False

    def get_all(self, db: Session) -> object_type_hints:
        return db.query(self.model).all()

    def filter(self, db: Session, **filters) -> object_type_hints:
        try:
            query = db.query(self.model)

            conditions = []
            for key, value in filters.items():
                if hasattr(self.model, key):
                    conditions.append(getattr(self.model, key) == value)

            if "logic" in filters and filters["logic"].lower() == "or":
                query = query.filter(or_(*conditions))
            else:
                query = query.filter(and_(*conditions))

            return query.all()

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise

    def count(self, db: Session) -> int:
        return db.query(self.model).count()

    def get_or_create(self, db: Session, **data) -> object_type_hint:
        get = self.get(db, data["id"])

        if get is None:
            return self.create(db, **data)
        else:
            return get


TodoDB = ORMBase(model=Todo)
