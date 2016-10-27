from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.frosted")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "countdb"
description = """count events, store in plain files, aggregate over time"""
summary = description
authors = [Author("Arne Hilmann", "arne.hilmann@gmail.com")]
url = "https://github.com/netkraken/countdb"
version = "0.5"

default_task = ["clean", "analyze", "package"]


@init
def set_properties(project):
    project.build_depends_on("mock")

    project.set_property("flake8_verbose_output", True)
    project.set_property("flake8_break_build", True)

    project.set_property("coverage_break_build", False)
