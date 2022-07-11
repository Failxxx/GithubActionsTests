import pytest
from blender_addon_tester.addon_helper import get_version


@pytest.fixture
def bpy_module(cache):  # noqa: D103
    return cache.get('bpy_module', None)


def test_version_advanced(bpy_module):  # noqa: D103
    # If we touch this point, this file has been properly loaded and run through a custom config mechanism :)
    assert len(get_version(bpy_module)) < 10


def test_versionID_pass(bpy_module):  # noqa: D103
    expect_version = (0, 0, 1)
    return_version = get_version(bpy_module)
    assert expect_version == return_version


def test_versionID_fail(bpy_module):  # noqa: D103
    expect_version = (0, 1, 1)
    return_version = get_version(bpy_module)
    assert not expect_version == return_version
