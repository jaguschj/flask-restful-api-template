from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from werkzeug.exceptions import BadRequest
from .model import Compound
from app import db

comp_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
}

comp_list_fields = {
    'count': fields.Integer,
    'comps': fields.List(fields.Nested(comp_fields)),
}

comp_post_parser = reqparse.RequestParser()
comp_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')
comp_post_parser.add_argument('description', type=str, required=True, location=['json'],
                              help='description parameter is required')


class CompoundResource(Resource):
    def get(self, comp_id=None):
        if comp_id:
            comp = Compound.query.filter_by(id=comp_id).first()
            return marshal(comp, comp_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            comp = Compound.query.filter_by(**args).order_by(Compound.id)
            if limit:
                comp = comp.limit(limit)

            if offset:
                comp = comp.offset(offset)

            comp = comp.all()

            return marshal({
                'count': len(comp),
                'comps': [marshal(t, comp_fields) for t in comp]
            }, comp_list_fields)

    @marshal_with(comp_fields)
    def post(self):
        args = comp_post_parser.parse_args()
        if Compound.query.filter_by(name=args['name']).first():
            raise BadRequest(description='Name %s already exists'%(args['name']))
        comp = Compound(**args)
        db.session.add(comp)
        db.session.commit()

        return comp

    @marshal_with(comp_fields)
    def put(self, comp_id=None):
        comp = Compound.query.get(comp_id)

        if 'name' in request.json:
            comp.name = request.json['name']

        if 'description' in request.json:
            comp.description = request.json['description']

        db.session.commit()
        return comp

    @marshal_with(comp_fields)
    def delete(self, comp_id=None):
        comp = Compound.query.get(comp_id)

        db.session.delete(comp)
        db.session.commit()

        return comp