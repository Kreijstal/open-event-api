from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship

from app.api.bootstrap import api
from app.api.helpers.db import safe_query
from app.api.schema.event_locations import EventLocationSchema
from app.models import db
from app.models.event import Event
from app.models.event_location import EventLocation


class EventLocationList(ResourceList):

    """
    List event locations
    """
    decorators = (api.has_permission('is_admin', methods="POST"),)
    schema = EventLocationSchema
    data_layer = {'session': db.session,
                  'model': EventLocation}


# class EventLocationDetail(ResourceDetail):
#     """
#     Event location detail by id
#     """
#     def before_get_object(self, view_kwargs):
#         """
#         before get method to get the resource id for fetching details
#         :param view_kwargs:
#         :return:
#         """
#         if view_kwargs.get('event_identifier'):
#             event = safe_query(self, Event, 'identifier', view_kwargs['event_identifier'], 'event_identifier')
#             view_kwargs['event_id'] = event.id

#         if view_kwargs.get('event_id'):
#             event = safe_query(self, Event, 'id', view_kwargs['event_id'], 'event_id')
#             if event.event_type_id:
#                 view_kwargs['id'] = event.event_location_id
#             else:
#                 view_kwargs['id'] = None

#     schema = EventLocationSchema
#     data_layer = {'session': db.session,
#                   'model': EventLocation,
#                   'methods': {
#                       'before_get_object': before_get_object
#                   }}


# class EventLocationRelationship(ResourceRelationship):
#     """
#     Event location Relationship
#     """
#     decorators = (api.has_permission('is_admin', methods="PATCH,DELETE"),)
#     schema = EventLocationSchema
#     data_layer = {'session': db.session,
#                   'model': EventLocation}
