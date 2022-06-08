import project
import pytest


def test_quit():
    """"""
    ...


def test_update_preview():
    """"""
    ...


def test_cleanup():
    """"""
    ...


def test_generate():
    """"""
    ...


def test_build():
    """"""
    ...


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
