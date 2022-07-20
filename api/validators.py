from django.core.exceptions import ValidationError
def validate_size(file):
    limit = 1 * 1024 * 1024 * 1024
    if file.size > limit:
        raise ValidationError('File too large. Size should not exceed 1 GiB.')

def validate_file_type(value):
    if not (value.name.endswith('.mp4') or value.name.endswith('.mkv')):
        raise ValidationError('Only .mp4 or .mkv files are supported')