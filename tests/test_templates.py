import os

import lucidity

import test_project_templates as tpt
import test_project_assetbuilds_templates as tpat
import test_project_folder_assetbuilds_templates as tpfat
import test_project_sequence_templates as tpst
import test_project_folder_sequence_templates as tpfst


def get_test_paths():
    return [
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/preproduction",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/aaf",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/audio",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/edl",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/footage",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/nukestudio",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/omf",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/qt_offline",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/xml",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/nukestudio/workspace",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/client",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/graphics",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/outsource",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/references",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/setdata",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/sourcefootage",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/transcodedfootage",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/client/from_client",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/client/to_client",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/outsource/company",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/outsource/company/from_broncos",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/outsource/company/to_broncos",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/setdata/grids",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/setdata/HDRs",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/setdata/measurements",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/io/setdata/references",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/preproduction/moodboards",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/preproduction/scripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/preproduction/storyboards",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/preproduction/treatments",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/3dsmax",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/"
        "photoshop",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/"
        "photoshop/files",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/"
        "photoshop/rendered",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/mari",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/"
        "_references",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "geo",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "render",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "_in",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "_out",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "workspace.mel",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "caches",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "outputScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "scenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "source",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "textures",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "caches/arnold",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "outputScenes/cacheScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "outputScenes/dynamicScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "outputScenes/renderScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "renderScripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "scripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "renders/comp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "renders/slapcomp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/editing",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/editorial/nukestudio/"
        "pipeline_test_v001.hrox",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/editing/nuke",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/editing/nuke/scripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/editing/nuke/scripts/"
        "pipeline_test_editing_v001.nk",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/editing/houdini/"
        "pipeline_test_editing_v001.hip",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/editing/maya/scenes/"
        "pipeline_test_editing_v001.mb",

<<<<<<< HEAD
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/3dsmax",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/mari",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/"
=======
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/editing/Group1/"
        "Group1_v001.gizmo",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/3dsmax",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/mari",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/"
>>>>>>> master
        "_references",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/_plates",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/photoshop",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/photoshop/files",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/photoshop/"
        "rendered",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/geo",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/render",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/_in",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/_out",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "workspace.mel",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "caches",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "outputScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "scenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "source",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "textures",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "caches/arnold",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "outputScenes/cacheScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "outputScenes/dynamicScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "outputScenes/renderScenes",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "renderScripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "scripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "scripts/workspace",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "renders/comp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "renders/slapcomp",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nukestudio/"
        "pipeline_test_lizard_lookdev_v001.hrox",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/"
        "houdini/pipeline_test_lizard_lookdev_v001.hip",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "scenes/pipeline_test_lizard_lookdev_v001.mb",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "scripts/pipeline_test_lizard_lookdev_v001.nk",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/"
        "lizard/lookdev/Group1/Group1_v001.gizmo",
<<<<<<< HEAD
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/lizard/lookdev/"
=======
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/"
        "lizard/lookdev/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/lizard/lookdev/"
>>>>>>> master
        "BackdropNode1/BackdropNode1_v001.nk",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/cache/"
        "lizard/lookdev/WriteGeo1/WriteGeo1_v001.abc",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/cache/"
        "lizard/lookdev/WriteGeo1/WriteGeo1_v001.fbx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/"
        "lizard/lookdev/set1_mayaBinary/set1_mayaBinary_v001.mb",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/"
        "lizard/lookdev/set1_mayaAscii/set1_mayaAscii_v001.ma",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/mov/lizard/"
        "lookdev/Write1/Write1_v001.mov",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/lizard/"
        "lookdev/Write1/Write1_v001.psd",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.exr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.exr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.dpx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.dpx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.jpeg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.jpeg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.jpg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.jpg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.hdr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.hdr",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/3dsmax",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/mari",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/"
        "_references",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/"
        "_plates",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/photoshop",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/photoshop/files",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/photoshop/"
        "rendered",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "geo",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "render",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "_in",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "_out",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "workspace.mel",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "caches",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "outputScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "scenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "source",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "textures",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "caches/arnold",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "outputScenes/cacheScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "outputScenes/dynamicScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "outputScenes/renderScenes",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "renderScripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "scripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "scripts/workspace",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "renders/comp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "renders/slapcomp",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/"
        "houdini/pipeline_test_castle_lookdev_v001.hip",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "scenes/pipeline_test_castle_lookdev_v001.mb",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "scripts/pipeline_test_castle_lookdev_v001.nk",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_dev/castle/nukestudio/"
        "pipeline_test_castle_lookdev_v001.hrox",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/"
        "castle/lookdev/Group1/Group1_v001.gizmo",
<<<<<<< HEAD
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/castle/lookdev/"
=======
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/castle/lookdev/"
        "Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/castle/lookdev/"
>>>>>>> master
        "BackdropNode1/BackdropNode1_v001.nk",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/cache/"
        "castle/lookdev/WriteGeo1/WriteGeo1_v001.abc",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/cache/"
        "castle/lookdev/WriteGeo1/WriteGeo1_v001.fbx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/"
        "castle/lookdev/set1_mayaBinary/set1_mayaBinary_v001.mb",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/"
        "castle/lookdev/set1_mayaAscii/set1_mayaAscii_v001.ma",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/mov/castle/lookdev/"
        "Write1/Write1_v001.mov",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/castle/lookdev/"
        "Write1/Write1_v001.psd",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.exr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.exr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.dpx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.dpx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.jpeg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.jpeg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.jpg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.jpg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.hdr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.hdr",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/3dsmax",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/mari",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/_plates",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/_references",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/photoshop",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/photoshop/files",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/photoshop/"
        "rendered",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/geo",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/render",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/_in",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/_out",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "workspace.mel",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/caches",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/scenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/source",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/textures",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/caches/"
        "arnold",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes/cacheScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes/dynamicScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes/renderScenes",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/"
        "renderScripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/scripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/renders/"
        "comp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/renders/"
        "slapcomp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/scripts/"
        "workspace",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/"
        "pipeline_test_sq001_sh0010_compositing_v001.hip",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/scripts/"
        "pipeline_test_sq001_sh0010_compositing_v001.nk",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/scenes/"
        "pipeline_test_sq001_sh0010_compositing_v001.mb",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nukestudio/"
        "pipeline_test_sq001_sh0010_compositing_v001.hrox",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001/sh0010/"
        "compositing/BackdropNode1/BackdropNode1_v001.nk",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001/sh0010/"
        "compositing/set1_mayaBinary/set1_mayaBinary_v001.mb",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001/sh0010/"
        "compositing/set1_mayaAscii/set1_mayaAscii_v001.ma",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/sq001/"
        "sh0010/compositing/Group1/Group1_v001.gizmo",
<<<<<<< HEAD
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/mov/sq001/sh0010/"
=======
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/sq001/"
        "sh0010/compositing/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/mov/sq001/sh0010/"
>>>>>>> master
        "compositing/write1/write1_v001.mov",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/mov/sq001/sh0010/"
        "compositing/write1/write1_v001.R3D",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001/sh0010/"
        "compositing/write1/write1_v001.psd",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/cache/sq001/sh0010/"
        "compositing/writegeo1/writegeo1_v001.abc",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/cache/sq001/sh0010/"
        "compositing/writegeo1/writegeo1_v001.fbx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/camera/sq001_sh0010/"
        "standard/0001/camera.abc",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/asset/writegeo1/"
        "model/sq001_sh0010/0001/model.abc",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.exr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.exr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.dpx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.dpx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.jpeg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.jpeg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.jpg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.jpg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.hdr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.hdr",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/_plates",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/_references",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/3dsmax",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/mari",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/photoshop",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/photoshop/"
        "files",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/photoshop/"
        "rendered",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/_in",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/_out",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/geo",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/"
        "render",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/temp",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/caches",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "caches/arnold",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "outputScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "outputScenes/cacheScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "outputScenes/dynamicScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "outputScenes/renderScenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/scenes",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/source",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "textures",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/renders",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/"
        "renders/comp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/"
        "renders/slapcomp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/"
        "renderScripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/scripts",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/scripts/"
        "workspace",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/temp",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "workspace.mel",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nukestudio"
        "/pipeline_test_sq001_sh0010_compositing_v001.hrox",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke"
        "/scripts/pipeline_test_sq001_sh0010_compositing_v001.nk",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya"
        "/scenes/pipeline_test_sq001_sh0010_compositing_v001.mb",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini"
        "/pipeline_test_sq001_sh0010_compositing_v001.hip",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/RND/sq001"
        "/sh0010/compositing/Group1/Group1_v001.gizmo",
<<<<<<< HEAD
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/RND/sq001"
=======
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/RND/sq001"
        "/sh0010/compositing/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/RND/sq001"
>>>>>>> master
        "/sh0010/compositing/BackdropNode1/BackdropNode1_v001.nk",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/mov/RND/sq001"
        "/sh0010/compositing/write1/write1_v001.mov",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/RND/sq001"
        "/sh0010/compositing/write1/write1_v001.psd",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/cache/RND/sq001"
        "/sh0010/compositing/writegeo1/writegeo1_v001.abc",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/cache/RND/sq001"
        "/sh0010/compositing/writegeo1/writegeo1_v001.fbx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/RND/sq001"
        "/sh0010/compositing/set1_mayaBinary/set1_mayaBinary_v001.mb",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/scene/RND/sq001"
        "/sh0010/compositing/set1_mayaAscii/set1_mayaAscii_v001.ma",

        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.exr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.exr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.dpx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.dpx",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.jpeg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.jpeg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.jpg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.jpg",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.hdr",
        "//ACT3-TGBVFX-SAN/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.hdr",
    ]


def assert_entity(entity):
    templates = lucidity.discover_templates()
    msg = (
        "No valid templates found for template name: \"{0}\", and entity: "
        "\"{1}\"".format(templates[0].get_template_name(entity), entity)
    )
    assert templates[0].get_valid_templates(entity, templates), msg

    get_resolved_paths(entity)


def get_resolved_paths(entity):
    templates = lucidity.discover_templates()
    valid_templates = templates[0].get_valid_templates(entity, templates)
    resolved_paths = []
    for template in valid_templates:
        try:
            resolved_paths.append(template.format(entity))
        except lucidity.error.FormatError as e:
            msg = e.message + "\nTemplate name: {0}".format(template.name)
            raise type(e)(msg)

    return resolved_paths


def get_workfile_extensions():
    return [".hrox", ".nk", ".mb", ".hip"]


def get_imagefile_extensions():
    return [".exr", ".dpx", ".jpeg", ".jpg", ".hdr"]


def test_environment():
    msg = "Could not find \"LUCIDITY_TEMPLATE_PATH\" in environment."
    assert "LUCIDITY_TEMPLATE_PATH" in os.environ.keys(), msg


def test_templates_existence():
    templates = lucidity.discover_templates()
    assert templates, "No templates discovered."


def get_entities():
    entities = []

    entities.extend(tpt.get_entities())
    entities.extend(tpat.get_entities())
    entities.extend(tpfat.get_entities())
    entities.extend(tpst.get_entities())
    entities.extend(tpfst.get_entities())

    return entities


def test_proposed_paths():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

    paths = get_test_paths()
    for path in template_paths:
        if path in paths:
            paths.remove(path)

    msg = "Paths not covered by templates:"
    for path in paths:
        msg += "\n{0}".format(path)
    msg += "\nTemplate paths:"
    for path in template_paths:
        msg += "\n{0}".format(path)
    assert not paths, msg


def test_unused_templates():
    templates = lucidity.discover_templates()

    used_templates = []
    for entity in get_entities():
        valid_templates = templates[0].get_valid_templates(entity, templates)
        used_templates.extend(valid_templates)

    # Cover templates not used
    unused_templates = list(set(templates) - set(used_templates))
    msg = "Templates not used:"
    for template in unused_templates:
        msg += "\n{0}".format(template)
    assert not unused_templates, msg


def test_excess_templates():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

    # Cover excess templates
    paths = []
    for path in template_paths:
        if path not in get_test_paths():
            paths.append(path)

    msg = "Excess template paths:"
    for path in paths:
        msg += "\n{0}".format(path)
    assert not paths, msg
