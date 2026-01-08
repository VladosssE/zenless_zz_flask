from extensions import db

class BaseStatsService:
    model = None
    id_field = None
    status_field = None
    done_value = None
    undone_value = None
    group_field = None
    order_field = None

    @classmethod
    def get_all(cls):
        return cls.model.query.order_by(getattr(cls.model, cls.order_field).asc()).all()


    @classmethod
    def get_by_group(cls, value):
        return (
            cls.model.query
            .filter_by(**{cls.group_field: value})
            .order_by(getattr(cls.model, cls.order_field).asc())
            .all()
        )

    @classmethod
    def get_all_groups(cls):
        return (
            db.session.query(getattr(cls.model, cls.group_field))
            .distinct()
            .order_by(getattr(cls.model, cls.order_field).asc())
            .all()
        )

    @classmethod
    def summary(cls):
        groups = [g[0] for g in cls.model.query.with_entities(getattr(cls.model, cls.group_field)).distinct()]
        summary = {}
        for group in groups:
            total = cls.model.query.filter_by(**{cls.group_field: group}).count()
            completed = cls.model.query.filter_by(**{cls.group_field: group, cls.status_field: cls.done_value}).count()
            summary[group] = {"completed": completed, "total": total}
        return summary

    @classmethod
    def total_completed(cls):
        completed = cls.model.query.filter_by(**{cls.status_field: cls.done_value}).count()
        total = cls.model.query.count()
        return {"completed": completed, "total": total}

    @classmethod
    def complete_all(cls):
        cls.model.query.update({cls.status_field: cls.done_value})
        db.session.commit()

    @classmethod
    def disable_all(cls):
        cls.model.query.update({cls.status_field: cls.undone_value})
        db.session.commit()

    @classmethod
    def toggle_status(cls, obj_id):
        obj = cls.model.query.get_or_404(obj_id)
        new_status = cls.undone_value if getattr(obj, cls.status_field) == cls.done_value else cls.done_value
        setattr(obj, cls.status_field, new_status)
        db.session.commit()
        return new_status

    @classmethod
    def update(cls, obj_id, status):
        obj = cls.model.query.get_or_404(obj_id)
        setattr(obj, cls.status_field, str(status))
        db.session.commit()
