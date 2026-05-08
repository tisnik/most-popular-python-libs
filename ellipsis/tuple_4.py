LIGHTSPEED_STACK_FIELDS: tuple[FieldSpec | ListFieldSpec, ...] = (
    # Operational
    FieldSpec("name", MaskingType.PASSTHROUGH),
    # Core Service Configuration
    FieldSpec("service.workers", MaskingType.PASSTHROUGH),

