

_model = None


def warm(model_path):
    global _model
    if _model is None:
        model = None
        _model = model
    return True


def predict(raw_data: bytes) -> bytes:
    return b'hot dog'
