# Routes excluded from Sentry trace sampling (health checks, metrics, root).
# Note: health and metrics routers are mounted WITHOUT a /v1 prefix
# (see the setup_routers function in src/app/routers.py), so ASGI paths are
# /readiness, /liveness, /metrics.
SENTRY_EXCLUDED_ROUTES: Final[tuple[str, ...]] = (
    "/readiness",
    "/liveness",
    "/metrics",
    "/",
)

