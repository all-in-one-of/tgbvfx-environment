import ftrack_api
import lucidity


class Structure(ftrack_api.structure.base.Structure):

    def get_resource_identifier(self, entity, context=None):

        templates = lucidity.discover_templates()

        valid_templates = templates[0].get_valid_templates(entity, templates)
        if valid_templates:
            path = valid_templates[0].format(entity)
            return path

        msg = (
            'Could not find any templates for {0} with template name "{1}".'
        )
        raise ValueError(
            msg.format(entity, templates[0].get_template_name(entity))
        )


class ResourceIdentifierTransformer(object):

    def __init__(self, session):
        self.session = session
        super(ResourceIdentifierTransformer, self).__init__()

    def encode(self, resource_identifier, context=None):
        return resource_identifier

    def decode(self, resource_identifier, context=None):
        # Server transition from "10.11.0.184" to "10.10.200.11"
        return resource_identifier.replace("10.11.0.184", "10.10.200.11")


def configure_locations(event):
    '''Configure locations for session.'''
    session = event['data']['session']

    location = session.query(
        "Location where name is \"lucidity\""
    ).one()
    location.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix="")
    location.structure = Structure()
    location.priority = 50
    location.resource_identifier_transformer = ResourceIdentifierTransformer(
        session
    )
    ftrack_api.mixin(
        location,
        ftrack_api.entity.location.UnmanagedLocationMixin,
        name="Unmanaged"
    )


def register(session):

    # Validate that session is an instance of ftrack_api.Session. If not,assume
    # that register is being called from an old or incompatible API and return
    # without doing anything.
    if not isinstance(session, ftrack_api.Session):
        return

    session.event_hub.subscribe(
        'topic=ftrack.api.session.configure-location',
        configure_locations
    )
