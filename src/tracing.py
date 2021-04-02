from flask import Flask
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.ext.stackdriver.trace_exporter import StackdriverExporter
from opencensus.trace import execution_context
from opencensus.trace.propagation import google_cloud_format
from opencensus.trace.samplers import AlwaysOnSampler

propagator = google_cloud_format.GoogleCloudFormatPropagator()
# trace_context_header = propagator.to_header(
#     execution_context.get_opencensus_tracer().span_context
# )

def create_middle_ware(exporter, app):
    return FlaskMiddleware(
        app,
        exporter=exporter,
        propagator=propagator,
        sampler=AlwaysOnSampler()
    )