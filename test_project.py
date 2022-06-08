import vcard


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
    assert vcard.vCard != None


def test_vcard_format():
    """Check that the vCard dictionary starts with "BEGIN": "VCARD", and ends with "END": "VCARD"."""
    assert vcard.vCard["BEGIN"] == "VCARD"
    assert vcard.vCard["END"] == "VCARD"


def test_vcard_version():
    """Check that the vCard contains "VERSION": "4.0" at the beginning of the card."""
    assert vcard.vCard["VERSION"] == "4.0"
