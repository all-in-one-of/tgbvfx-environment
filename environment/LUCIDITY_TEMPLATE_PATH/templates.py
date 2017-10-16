import os
import platform

import lucidity


class Template(lucidity.Template):

    def get_parents(self, entity, parents):
        """Recursive iterate to find all parents.

        For AssetVersion where no parent is present, the asset is assumed as
        parent.
        For SequenceComponent and FileComponent where no parent is present, the
        asset version is assumed as parent.
        """

        try:
            parent = entity["parent"]
            if parent:
                parents.append(parent)
                return self.get_parents(parent, parents)
        except KeyError:
            if entity.entity_type == "AssetVersion":
                parents.append(entity["asset"])
                return self.get_parents(entity["asset"], parents)

            if entity.entity_type == "FileComponent":

                parent = entity["version"]
                # Assuming its in a container, if there are no version.
                if parent:
                    parents.append(entity["version"])
                else:
                    parent = entity["container"]
                    parents.append(entity["container"])
                return self.get_parents(parent, parents)

            if entity.entity_type == "SequenceComponent":
                parents.append(entity["version"])
                return self.get_parents(entity["version"], parents)

        return parents

    def get_entity_type_path(self, entities):
        """Get the entity type path from a list of entities

        The returned path is a list of entity types separated by a path
        separator:
            "[entity_type]/[entity_type]/[entity_type]"
            "Project/Asset/AssetVersion"

        For further uniqueness the file_type data member (extension) is used
        for components. This results in paths like this:
            "Project/Asset/AssetVersion/FileComponent/[file_type]"
            "Project/Asset/AssetVersion/FileComponent/.txt"
            "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.exr
            /FileComponent/.exr"
        """

        entity_types = []
        for entity in entities:
            entity_types.append(entity.entity_type)

            try:
                entity_types.append(entity["file_type"])
            except KeyError:
                pass

        return "/".join(entity_types)

    def get_template_name(self, entity):
        """Convenience method for getting the template name

        The template name is generated from the entity's parents, and their
        entity type.
        """

        entities = list(reversed(self.get_parents(entity, [])))
        entities.append(entity)
        return self.get_entity_type_path(entities)

    def get_valid_templates(self, entity, templates):

        results = []
        template_name = self.get_template_name(entity)
        try:
            template_name = entity["metadata"]["lucidity_template_name"]
        except KeyError:
            pass

        for template in templates:
            if template.name == template_name:
                results.append(template)

        return results

    def format(self, data):

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "AssetVersion":
            version_string = str(data["version"]).zfill(3)
            data["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "FileComponent":
            if data["version"]:
                version_string = str(data["version"]["version"]).zfill(3)
                data["version"]["version"] = version_string
            else:
                version_string = str(
                    data["container"]["version"]["version"]
                ).zfill(3)
                data["container"]["version"]["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "SequenceComponent":
            version_string = str(data["version"]["version"]).zfill(3)
            data["version"]["version"] = version_string

            # "padding" data member needs to be convert from integer to string.
            padding_string = str(data["padding"]).zfill(2)
            data["padding"] = padding_string

        if data.entity_type == "Task" and "version" in data.keys():
            version_string = str(data["version"]).zfill(3)
            data["version"] = version_string

        return os.path.abspath(
            super(Template, self).format(data)
        ).replace("\\", "/")


def register():
    '''Register templates.

    Templates are named according to the entity in the hierarchy,
    they aim to solve paths for.
    For example a template named "Project" is only for paths for the project.
    Nested entity types are specified with a path separator, for example
    "Project/Shot" deals with paths for shots under the project.
    To specify dealing with certain file types, the file types extension is
    added. For example a template named "Project/.nk" deals with Nuke script
    paths under the project.
    It is assumed that asset versions are children of the asset, resulting in a
    path "Project/Asset/AssetVersion".
    '''

    system_name = platform.system().lower()
    if system_name != "windows":
        system_name = "unix"

    templates = []

    # Project level templates
    mount = "{disk." + system_name + "}/{root}/tgbvfx"
    templates.extend([
        Template("Project", mount),
        Template("Project", mount + "/editorial"),
        Template("Project", mount + "/editorial/audio"),
        Template("Project", mount + "/editorial/edl"),
        Template("Project", mount + "/editorial/footage"),
        Template("Project", mount + "/editorial/nukestudio"),
        Template("Project", mount + "/editorial/nukestudio/workspace"),
        Template("Project", mount + "/editorial/omf"),
        Template("Project", mount + "/editorial/qt_offline"),
        Template("Project", mount + "/editorial/xml"),
        Template("Project", mount + "/editorial/aaf"),
        Template("Project", mount + "/io"),
        Template("Project", mount + "/io/client"),
        Template("Project", mount + "/io/client/from_client"),
        Template("Project", mount + "/io/client/to_client"),
        Template("Project", mount + "/io/graphics"),
        Template("Project", mount + "/io/outsource"),
        Template("Project", mount + "/io/outsource/company"),
        Template("Project", mount + "/io/outsource/company/from_broncos"),
        Template("Project", mount + "/io/outsource/company/to_broncos"),
        Template("Project", mount + "/io/references"),
        Template("Project", mount + "/io/setdata"),
        Template("Project", mount + "/io/setdata/grids"),
        Template("Project", mount + "/io/setdata/HDRs"),
        Template("Project", mount + "/io/setdata/measurements"),
        Template("Project", mount + "/io/setdata/references"),
        Template("Project", mount + "/io/sourcefootage"),
        Template("Project", mount + "/io/transcodedfootage"),
        Template("Project", mount + "/preproduction"),
        Template("Project", mount + "/preproduction/moodboards"),
        Template("Project", mount + "/preproduction/scripts"),
        Template("Project", mount + "/preproduction/storyboards"),
        Template("Project", mount + "/preproduction/treatments"),
        Template("Project", mount + "/vfx"),
        Template("Project", mount + "/vfx/_dev"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/_references"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/3dsmax"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/_in"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/_out"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/geo"),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/render"
        ),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/temp"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/mari"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/caches"),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/caches/arnold"
        ),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/outputScenes"
        ),
        Template(
            "Project",
            mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/outputScenes/cacheScenes"
        ),
        Template(
            "Project",
            mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/outputScenes/dynamicScenes"
        ),
        Template(
            "Project",
            mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/outputScenes/renderScenes"
        ),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/renders"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/scenes"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/source"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/temp"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/textures"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/renders"),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/renders/comp"
        ),
        Template(
            "Project",
            mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/renders/slapcomp"
        ),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/renderScripts"
        ),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/scripts"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/temp"),
        Template("Project", mount + "/vfx/_publish"),
    ])

    # Projet level auxiliary files
    template = Template(
        "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/workspace.mel"
    )
    template.source = os.path.join(
        os.path.dirname(__file__), "workspace.mel"
    )
    templates.append(template)

    # Project/Task level templates
    templates.extend([
        Template(
            "Project/Task",
            "{project.disk." + system_name + "}/{project.root}/tgbvfx/vfx/"
            "{name}"
        ),
        Template(
            "Project/Task",
            "{project.disk." + system_name + "}/{project.root}/tgbvfx/vfx/"
            "{name}/nuke"
        ),
        Template(
            "Project/Task",
            "{project.disk." + system_name + "}/{project.root}/tgbvfx/vfx/"
            "{name}/nuke/scripts"
        ),
    ])

    # Project/Sequence level templates
    templates.extend([
        Template(
            "Project/Sequence",
            "{project.disk." + system_name + "}/{project.root}/tgbvfx/vfx/"
            "{name}"
        ),
    ])

    # Work directories
    directories = [
        "{0}",
        "{0}/_plates",
        "{0}/_references",
        "{0}/3dsmax",
        "{0}/mari",
        "{0}/houdini",
        "{0}/houdini/_in",
        "{0}/houdini/_out",
        "{0}/houdini/geo",
        "{0}/houdini/render",
        "{0}/houdini/temp",
        "{0}/maya",
        "{0}/maya/caches",
        "{0}/maya/caches/arnold",
        "{0}/maya/outputScenes",
        "{0}/maya/outputScenes/cacheScenes",
        "{0}/maya/outputScenes/dynamicScenes",
        "{0}/maya/outputScenes/renderScenes",
        "{0}/maya/renders",
        "{0}/maya/scenes",
        "{0}/maya/source",
        "{0}/maya/temp",
        "{0}/maya/textures",
        "{0}/nuke",
        "{0}/nuke/renders",
        "{0}/nuke/renders/comp",
        "{0}/nuke/renders/slapcomp",
        "{0}/nuke/renderScripts",
        "{0}/nuke/scripts",
        "{0}/nuke/scripts/workspace",
        "{0}/nuke/temp",
    ]

    # Project/Sequence/Shot directories
    mount = (
        "{project.disk." + system_name + "}/"
        "{project.root}/"
        "tgbvfx/"
        "vfx/"
        "{parent.name}/"
        "{name}"
    )
    for directory in directories:
        templates.append(
            Template("Project/Sequence/Shot", directory.format(mount))
        )

    # Project/AssetBuild and Project/Folder/AssetBuild
    mount = (
        "{project.disk." + system_name + "}/"
        "{project.root}/"
        "tgbvfx/"
        "vfx/"
        "_dev/"
        "{name}"
    )
    for directory in directories:
        templates.append(
            Template("Project/AssetBuild", directory.format(mount))
        )
        templates.append(
            Template("Project/Folder/AssetBuild", directory.format(mount))
        )

    # Project/Sequence/Shot level auxiliary files
    mount = (
        "{project.disk." + system_name + "}/"
        "{project.root}/"
        "tgbvfx/"
        "vfx/"
        "{parent.name}/"
        "{name}"
    )
    template = Template(
        "Project/Sequence/Shot", mount + "/maya/workspace.mel"
    )
    template.source = os.path.join(
        os.path.dirname(__file__), "workspace.mel"
    )
    templates.append(template)

    # Project/AssetBuild and Project/Folder/AssetBuild level auxiliary files
    mount = (
        "{project.disk." + system_name + "}/"
        "{project.root}/"
        "tgbvfx/"
        "vfx/"
        "_dev/"
        "{name}"
    )

    template = Template(
        "Project/AssetBuild", mount + "/maya/workspace.mel"
    )
    template.source = os.path.join(
        os.path.dirname(__file__), "workspace.mel"
    )
    templates.append(template)

    template = Template(
        "Project/Folder/AssetBuild", mount + "/maya/workspace.mel"
    )
    template.source = os.path.join(
        os.path.dirname(__file__), "workspace.mel"
    )
    templates.append(template)

    # Image file templates
    extensions = [".exr", ".dpx", ".jpg", ".jpeg", ".hdr"]

    # SequenceComponent Sequence/Shot
    pattern = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "tgbvfx/"
        "vfx/"
        "_publish/"
        "{version.asset.type.short}/"
        "{version.asset.parent.parent.name}_{version.asset.parent.name}/"
        "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
        "{version.metadata.instance_name}_v{version.version}/"
        "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
        "{version.metadata.instance_name}_v{version.version}.%{padding}d"
        "{file_type}"
    )
    name = (
        "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/{0}"
    )
    for ext in extensions:
        templates.append(Template(name.format(ext), pattern))

    # SequenceComponent AssetBuild and Folder/AssetBuild
    pattern = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "tgbvfx/"
        "vfx/"
        "_publish/"
        "{version.asset.type.short}/"
        "{version.asset.parent.name}/"
        "{version.task.name}/"
        "{version.metadata.instance_name}_v{version.version}/"
        "{version.metadata.instance_name}_v{version.version}.%{padding}d"
        "{file_type}"
    )
    names = [
        "Project/AssetBuild/Asset/AssetVersion/SequenceComponent/{0}",
        "Project/Folder/AssetBuild/Asset/AssetVersion/SequenceComponent/{0}",
    ]
    for ext in extensions:
        for name in names:
            templates.append(Template(name.format(ext), pattern))

    # FileComponent Sequence/Shot
    pattern = (
        "{container.version.task.project.disk." + system_name + "}/"
        "{container.version.task.project.root}/"
        "tgbvfx/"
        "vfx/"
        "_publish/"
        "{container.version.asset.type.short}/"
        "{container.version.asset.parent.parent.name}_"
        "{container.version.asset.parent.name}/"
        "{container.version.asset.parent.parent.name}_"
        "{container.version.asset.parent.name}_"
        "{container.version.metadata.instance_name}_"
        "v{container.version.version}/"
        "{container.version.asset.parent.parent.name}_"
        "{container.version.asset.parent.name}_"
        "{container.version.metadata.instance_name}_"
        "v{container.version.version}.{name}{file_type}"
    )
    names = [
        "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/{0}"
        "/FileComponent/{0}",
    ]
    for ext in extensions:
        for name in names:
            templates.append(Template(name.format(ext), pattern))

    # FileComponent AssetBuild Folder/AssetBuild
    pattern = (
        "{container.version.task.project.disk." + system_name + "}/"
        "{container.version.task.project.root}/"
        "tgbvfx/"
        "vfx/"
        "_publish/"
        "{container.version.asset.type.short}/"
        "{container.version.asset.parent.name}/"
        "{container.version.task.name}/"
        "{container.version.metadata.instance_name}_"
        "v{container.version.version}/"
        "{container.version.metadata.instance_name}_"
        "v{container.version.version}.{name}{file_type}"
    )
    names = [
        "Project/AssetBuild/Asset/AssetVersion/SequenceComponent/{0}/"
        "FileComponent/{0}",
        "Project/Folder/AssetBuild/Asset/AssetVersion/SequenceComponent/{0}/"
        "FileComponent/{0}",
    ]
    for ext in extensions:
        for name in names:
            templates.append(Template(name.format(ext), pattern))

    # .abc
    templates.extend([
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.abc",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.abc",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.abc",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.parent.name}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
    ])

    # .mov
    templates.extend([
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.mov",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.task.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.mov",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.task.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.mov",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.parent.name}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
    ])

    # .gizmo
    templates.extend([
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.gizmo",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/"
            ".gizmo",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.gizmo",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.parent.name}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
    ])

    # .nk
    templates.extend([
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.nk",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.task.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.nk",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.task.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.nk",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.parent.name}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
    ])

    # .mb
    templates.extend([
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.mb",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.task.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.mb",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.task.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.mb",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.parent.name}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
    ])

    # .ma
    templates.extend([
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.ma",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.task.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.ma",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.task.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.ma",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/"
            "tgbvfx/"
            "vfx/"
            "_publish/"
            "{version.asset.type.short}/"
            "{version.asset.parent.parent.name}/"
            "{version.asset.parent.name}/"
            "{version.task.name}/"
            "{version.metadata.instance_name}/"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
    ])

    # Work files
    templates.extend([
        Template(
            "Project/Task/.hrox",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "editorial/"
            "nukestudio/"
            "{project.name}_v{version}{file_type}"
        ),
        Template(
            "Project/Task/.nk",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "{name}/"
            "nuke/"
            "scripts/"
            "{project.name}_{name}_v{version}{file_type}"
        ),
        Template(
            "Project/Task/.mb",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "{name}/"
            "maya/"
            "scenes/"
            "{project.name}_{name}_v{version}{file_type}"
        ),
        Template(
            "Project/Task/.hip",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "{name}/"
            "houdini/"
            "{project.name}_{name}_v{version}{file_type}"
        ),

        Template(
            "Project/AssetBuild/Task/.hrox",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "_dev/"
            "{parent.name}/"
            "nukestudio/"
            "{project.name}_{parent.name}_{name}_v{version}{file_type}"
        ),
        Template(
            "Project/AssetBuild/Task/.nk",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "_dev/"
            "{parent.name}/"
            "nuke/"
            "scripts/"
            "{project.name}_{parent.name}_{name}_v{version}{file_type}"
        ),
        Template(
            "Project/AssetBuild/Task/.mb",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "_dev/"
            "{parent.name}/"
            "maya/"
            "scenes/"
            "{project.name}_{parent.name}_{name}_v{version}{file_type}"
        ),
        Template(
            "Project/AssetBuild/Task/.hip",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "_dev/"
            "{parent.name}/"
            "houdini/"
            "{project.name}_{parent.name}_{name}_v{version}{file_type}"
        ),

        Template(
            "Project/Folder/AssetBuild/Task/.hrox",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "_dev/"
            "{parent.name}/"
            "nukestudio/"
            "{project.name}_{parent.name}_{name}_v{version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Task/.nk",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "_dev/"
            "{parent.name}/"
            "nuke/"
            "scripts/"
            "{project.name}_{parent.name}_{name}_v{version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Task/.mb",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "_dev/"
            "{parent.name}/"
            "maya/"
            "scenes/"
            "{project.name}_{parent.name}_{name}_v{version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Task/.hip",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "_dev/"
            "{parent.name}/"
            "houdini/"
            "{project.name}_{parent.name}_{name}_v{version}{file_type}"
        ),

        Template(
            "Project/Sequence/Shot/Task/.hrox",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "{parent.parent.name}/"
            "{parent.name}/"
            "nukestudio/"
            "{project.name}_{parent.parent.name}_{parent.name}_{name}_"
            "v{version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Task/.nk",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "{parent.parent.name}/"
            "{parent.name}/"
            "nuke/"
            "scripts/"
            "{project.name}_{parent.parent.name}_{parent.name}_{name}_"
            "v{version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Task/.mb",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "{parent.parent.name}/"
            "{parent.name}/"
            "maya/"
            "scenes/"
            "{project.name}_{parent.parent.name}_{parent.name}_{name}_"
            "v{version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Task/.hip",
            "{project.disk." + system_name + "}/"
            "{project.root}/"
            "tgbvfx/"
            "vfx/"
            "{parent.parent.name}/"
            "{parent.name}/"
            "houdini/"
            "{project.name}_{parent.parent.name}_{parent.name}_{name}_"
            "v{version}{file_type}"
        ),
    ])

    return templates
