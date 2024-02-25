from flask import abort, make_response
from config import db
from content.models import Provider, Provider_schema, Providers_schema

def show_all():
    providers = Provider.query.all()
    return Providers_schema.dump(providers)

def lookup_by_id(provider_id):
    provider = Provider.query.filter(Provider.provider_id == provider_id).one_or_none()
    if provider is not None:
        return Provider_schema.dump(provider)
    else:
        abort(404, f"Provider id {provider_id} not found")

def get_provider_name(provider_id):
    provider = Provider.query.filter(Provider.provider_id == provider_id).one_or_none()
    if provider is not None:
        return { 'provider_name': provider.provider_name }
    else:
        abort(404, f"Provider id {provider_id} not found")