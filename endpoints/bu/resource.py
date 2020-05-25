from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from werkzeug.exceptions import BadRequest
from .model import BU
from app import db

bu_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String
}

bu_list_fields = {
    'count': fields.Integer,
    'bus': fields.List(fields.Nested(bu_fields)),
}

bu_post_parser = reqparse.RequestParser()
bu_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='unique name parameter is required')
bu_post_parser.add_argument('description', type=str, required=True, location=['json'],
                              help='description parameter is required')


class BUResource(Resource):
    def get(self, bu_id=None):
        if bu_id:
            bu = BU.query.filter_by(id=bu_id).first()
            return marshal(bu, bu_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            bu = BU.query.filter_by(**args).order_by(BU.id)
            if limit:
                bu = bu.limit(limit)

            if offset:
                bu = bu.offset(offset)

            bu = bu.all()

            return marshal({
                'count': len(bu),
                'bus': [marshal(t, bu_fields) for t in bu]
            }, bu_list_fields)

    @marshal_with(bu_fields)
    def post(self):
        args = bu_post_parser.parse_args()
        if BU.query.filter_by(name=args['name']).first():
            raise BadRequest(description='Name %s already exists'%(args['name']))
        bu = BU(**args)
        db.session.add(bu)
        db.session.commit()

        return bu

    @marshal_with(bu_fields)
    def put(self, bu_id=None):
        bu = BU.query.get(bu_id)

        if 'name' in request.json:
            bu.name = request.json['name']

        if 'description' in request.json:
            bu.description = request.json['description']

        db.session.commit()
        return bu

    @marshal_with(bu_fields)
    def delete(self, bu_id=None):
        bu = BU.query.get(bu_id)

        db.session.delete(bu)
        db.session.commit()

        return bu