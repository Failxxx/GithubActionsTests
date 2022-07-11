from bpy.types import Panel, Context
from bpy.app.handlers import persistent


class TEST_PT_Panel(Panel):
    """
    Test panel.
    """

    bl_label = 'Test'
    bl_idname = 'TEST_PT_Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Test'

    def draw(self, _context: Context) -> None:
        """
        Layout of the panel.

        :param _context: Context
        :type _context: Context
        """

        layout = self.layout
        row = layout.row()
        row.label(text='Test', icon='ERROR')


class TEST_PT_ChildPanel(TEST_PT_Panel):
    """
    Child test panel.
    """

    bl_label = 'Child test panel'
    bl_idname = 'TEST_PT_ChildPanel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Test'

    def draw(self, context: Context) -> None:
        """
        Layout of the panel.

        :param _context: Context
        :type _context: Context
        """
        TEST_PT_Panel.draw(self, context)

        layout = self.layout
        row = layout.row()
        row.label(text='Child error', icon='ERROR')


@persistent
def test_function_with_decorator(size: int = 0) -> None:
    """
    Test function with a decorator.

    :param size: sugar, defaults to 0
    :type size: int, optional
    """

    pass
