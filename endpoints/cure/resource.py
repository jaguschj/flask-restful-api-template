from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from flask_restful import abort
from werkzeug.exceptions import BadRequest
from .model import Curedb
from app import db

       
        
cure_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'a': fields.Float,
    'b': fields.Float,
    'user_id': fields.Integer,
    'bu_id': fields.Integer,
    'comp_id': fields.Integer
}

cure_list_fields = {
    'count': fields.Integer,
    'cures': fields.List(fields.Nested(cure_fields)),
}

cure_post_parser = reqparse.RequestParser()
cure_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')
cure_post_parser.add_argument('description', type=str, required=False, location=['json'],
                              help='description parameter is optional')
cure_post_parser.add_argument('a', type=float, required=True, location=['json'],
                              help='a parameter is required')
cure_post_parser.add_argument('b', type=float, required=True, location=['json'],
                              help='b parameter is required')
cure_post_parser.add_argument('user_id', type=int, required=True, location=['json'],
                              help='user_id parameter is required')
cure_post_parser.add_argument('bu_id', type=int, required=True, location=['json'],
                              help='bu_id parameter is required')
cure_post_parser.add_argument('comp_id', type=int, required=True, location=['json'],
                              help='comp_id parameter is required')


class CuredbResource(Resource):
    def get(self, cure_id=None):
        if cure_id:
            cure = Curedb.query.filter_by(id=cure_id).first()
            #cure = Curedb.get(cure_id)
            return marshal(cure, cure_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            cure = Curedb.query.filter_by(**args).order_by(Curedb.id)
            if limit:
                cure = cure.limit(limit)

            if offset:
                cure = cure.offset(offset)

            cure = cure.all()

            return marshal({
                'count': len(cure),
                'cures': [marshal(t, cure_fields) for t in cure]
            }, cure_list_fields)

    @marshal_with(cure_fields)
    def post(self):
        args = cure_post_parser.parse_args()
        #print(args)
        #import pdb;pdb.set_trace()
        if Curedb.query.filter_by(name=args['name']).first():
            raise BadRequest(description='Name %s already exists'%(args['name']))
            #raise CuredbAlreadyExistsError
            #return bad_request('please use a different name')
            #abort(Response('name already exists'))
        cure = Curedb(**args)
        db.session.add(cure)
        db.session.commit()

        return cure

    @marshal_with(cure_fields)
    def put(self, cure_id=None):
        cure = Curedb.query.get(cure_id)

        if 'name' in request.json:
            cure.name = request.json['name']
        if 'user_id' in request.json:
            cure.user_id = request.json['user_id']
        if 'description' in request.json:
            cure.description = request.json['description']
        if 'a' in request.json:
            cure.a = request.json['a']
        if 'b' in request.json:
            cure.b = request.json['b']

        db.session.commit()
        return cure

    @marshal_with(cure_fields)
    def delete(self, cure_id=None):
        cure = Curedb.query.get(cure_id)

        db.session.delete(cure)
        db.session.commit()

        return cure