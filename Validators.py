def validate_project_exists(projects, name):
    if not any(p["name"] == name for p in projects):
        raise ValueError(f"Project '{name}' bestaat niet")