import functools
import os
import re
import uuid


def upload_to_uuid(path, make_dir=False, remove_qs=True):
    return functools.partial(_upload_to_uuid_impl, path=path, make_dir=make_dir, remove_qs=remove_qs)


def _upload_to_uuid_impl(instance, filename, path, make_dir, remove_qs):
    if remove_qs:
        filename = re.sub(r'\?.*', '', filename)

    uuid_part = uuid.uuid4().urn.split(':')[-1]

    if make_dir:
        filename = filename.replace(' ', '_')
        return os.path.join(path, uuid_part, filename)
    else:
        ext = os.path.splitext(filename)[-1].lower()
        return os.path.join(path, uuid_part + ext)
