# <pep8 compliant>
from bpy.utils import unregister_class, register_class
from .panels.test import TEST_PT_Panel, TEST_PT_ChildPanel


bl_info = {
    'name': 'Add-on',
    'description': 'Add-on',
    'author': 'Félix Olart',
    'version': (0, 1, 0),
    'blender': (2, 80, 0),
    'location': 'View3D',
    'warning': '',
    'category': 'Import-Export',
    'doc_url': 'https://github.com/Failxxx/GithubActionsTests',
    'tracker_url': 'https://github.com/Failxxx/GithubActionsTests/issues'
}

classes = (TEST_PT_Panel, TEST_PT_ChildPanel,)


def register():
    """My docstring."""
    print('ADDON - REGISTER')
    for cls in classes:
        register_class(cls)


def unregister():
    """My docstring."""
    print('ADDON - UNREGISTER')
    for cls in reversed(classes):
        unregister_class(cls)
