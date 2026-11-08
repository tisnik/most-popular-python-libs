DOCUMENT_CONTENT_TYPES: Final[frozenset[str]] = frozenset(
    {
        "text/plain",
        "application/json",
        "application/yaml",
        "application/xml",
    }
)

IMAGE_CONTENT_TYPES: Final[frozenset[str]] = frozenset(
    {
        "image/jpeg",
        "image/png",
        "image/webp",
    }
)

ATTACHMENT_CONTENT_TYPES = DOCUMENT_CONTENT_TYPES | IMAGE_CONTENT_TYPES

print(ATTACHMENT_CONTENT_TYPES)
