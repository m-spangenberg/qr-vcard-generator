import os
import project
import pytest


def test_end():
    """Check that the quit function calls sys.exit"""
    with pytest.raises(SystemExit):
        project.end()


def test_update_preview():
    """Check that update preview catches exception attempting to load a non-existent file."""
    with pytest.raises(TypeError):
        project.update_preview()


def test_cleanup():
    """Check that cleanup removes file."""
    f = open('output/preview.png', 'w')
    f.close()
    project.cleanup()
    assert os.path.isfile("output/preview.png") == False


def test_build():
    """Assert calling build generates easter egg image."""
    project.build()
    assert os.path.isfile("output/preview.png") == True
    project.cleanup()


def test_vcard_exists():
    """Check that the vcard dictionary exists."""
    assert project.vCard != None


def test_vcard_format():
    """Check that the vCard dictionary starts with "BEGIN": "VCARD", and ends with "END": "VCARD"."""
    assert project.vCard["BEGIN"] == "VCARD"
    assert project.vCard["END"] == "VCARD"


def test_vcard_version():
    """Check that the vCard contains "VERSION": "4.0" at the beginning of the card."""
    assert project.vCard["VERSION"] == "4.0"
