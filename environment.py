import os

from conda_git_deployment import utils


root = os.path.dirname(__file__)
environment = {}

# PYTHONPATH
environment["PYTHONPATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-template"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-locations"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-maya",
        "pyblish_maya",
        "pythonpath"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "pythonpath"
    ),
]

# NUKE_PATH
environment["NUKE_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-nuke",
        "pyblish_nuke",
        "nuke_path"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "nuke_path"
    )
]

# FTRACK_TEMPLATES_PATH
environment["FTRACK_TEMPLATES_PATH"] = [
    os.path.join(root, "environment", "FTRACK_TEMPLATES_PATH")
]

# FTRACK_CONNECT_PLUGIN_PATH
environment["FTRACK_CONNECT_PLUGIN_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "djv_plugin"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "pending_changes"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "status_assign"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "pipeline_plugins"
    ),
    os.path.join(root, "environment", "FTRACK_CONNECT_PLUGIN_PATH"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-ftrack",
        "pyblish_ftrack"
    ),
]

# FTRACK_LOCATION_PLUGIN_PATH
environment["FTRACK_LOCATION_PLUGIN_PATH"] = [
    os.path.join(root, "environment", "FTRACK_LOCATION_PLUGIN_PATH"),
]

# FTRACK_LOCATIONS_MODULE
environment["FTRACK_LOCATIONS_MODULE"] = [
    os.environ.get("FTRACK_LOCATIONS_MODULE", "ftrack_template_disk")
]

utils.write_environment(environment)