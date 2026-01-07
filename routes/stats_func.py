from flask import Blueprint, render_template, request, redirect, jsonify
from extensions import db

def create_stats_blueprint(
    *,
    name,
    url_prefix,
    service,
    model,
    template,
    filter_arg,
    get_all_filters,
    get_by_filter,
    summary_func,
    id_field,
    status_field,
    status_done,
    status_not_done
):
    bp = Blueprint(name, __name__, url_prefix=url_prefix)

    @bp.get("/")
    def list_data():
        current = request.args.get(filter_arg)
        all_filters = get_all_filters()
        summary = summary_func()

        if current:
            all_data = get_by_filter(current)
        else:
            all_data = service.get_all()

        return render_template(
            template,
            all_data=all_data,
            all_certain=[x[0] for x in all_filters],
            current=current,
            summary=summary
        )

    @bp.route("/complete_all", methods=["POST"])
    def complete_all():
        service.complete_all()
        return redirect(request.referrer)


    @bp.route("/disable_all", methods=["POST"])
    def disable_all():
        service.disable_all()
        return redirect(request.referrer)
    

    @bp.route("/update", methods=["POST"])
    def update_status():
        data = request.get_json()
        if not data or id_field not in data:
            return jsonify({"error": "Нет данных"}), 400

        obj = model.query.get(data[id_field])
        if not obj:
            return jsonify({"error": "Не найдено"}), 404

        current = getattr(obj, status_field)
        new_status = status_not_done if current == status_done else status_done
        setattr(obj, status_field, new_status)

        db.session.commit()
        return jsonify({"status": new_status})

    return bp
