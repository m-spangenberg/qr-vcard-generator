import os
import sys
import qrcode
import itertools
from PIL import Image as mm
import dearpygui.dearpygui as dpg
from dearpygui_ext.themes import create_theme_imgui_light

# vCard format
vCard = {
    "BEGIN": "VCARD",
    "VERSION": "4.0",
    "KIND": "INDIVIDUAL",
    "EMAIL;TYPE=WORK": "Email",
    "TITLE": "Title",
    "ROLE": "Role",
    "FN": "Full Name",
    "TEL;TYPE=CELL": "Telephone",
    "TEL;TYPE=WORK": "Mobile",
    "URL": "URL",
    "ORG": "Organization",
    "END": "VCARD",
}


def main():
    dpg.create_context()

    # # Set the theme and styling
    light_theme = create_theme_imgui_light()
    dpg.bind_theme(light_theme)

    # Build the menu bar
    with dpg.viewport_menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Generate", tag="generate_menu", callback=generate)
            dpg.add_menu_item(label="Reset", tag="reset_menu", callback=reset)
            dpg.add_menu_item(label="Save", tag="save_menu", callback=generate)
            dpg.add_menu_item(label="Quit", tag="quit_menu", callback=quit)

    # Build the primary window
    with dpg.window(tag="QR-vCard - V0.1.0"):

        # Spacing guide: menu bar
        dpg.add_spacer(width=240, height=25)

        # Generate input fields as defined by vCard dictionary
        display_fields = dict(itertools.islice(vCard.items(), 3, 11))
        for key, value in display_fields.items():
            dpg.add_input_text(width=240, hint=value, tag=value, indent=10)

        # Spacing guide: prompt
        dpg.add_spacer(width=5, height=5)

        # Prompt user to perform generation
        dpg.add_text("Generate a QR vCard", indent=10)

        # Present the action button
        dpg.add_button(
            tag="generate_button",
            label="Generate",
            width=240,
            height=20,
            indent=10,
            callback=generate,
        )

        # Import a placeholder image
        width, height, channels, data = dpg.load_image("images/placeholder.png")

        with dpg.texture_registry(show=False):
            dpg.add_dynamic_texture(330, 330, data, tag="texture_tag")

        # Present a window and populate it with the resulting image
        dpg.add_image(
            texture_tag="texture_tag",
            width=240,
            height=240,
            pos=(18, 290),
        )

    dpg.create_viewport(
        title="QR-vCard - V0.1.0",
        width=280,
        height=550,
        x_pos=660,
        y_pos=180,
        resizable=False,
        small_icon=r"images/icon.png",
        large_icon=r"images/icon.png",
    )

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("QR-vCard - V0.1.0", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

    cleanup()


def quit():
    """Removes temporary files and exits the program cleanly."""
    cleanup()
    sys.exit(1)


def update_preview():
    """Refresh placeholder image with generated qr-code.
    Note all images must have the same dimensions or update_preview
    will fail with segmentation fault."""
    width, height, channels, data = dpg.load_image("output/preview.png")
    dpg.set_value("texture_tag", data)


def cleanup():
    """Remove preview image from output folder."""
    try:
        os.remove("output/preview.png")
    except OSError as e:
        pass


def reset():
    """Clear all contact fields."""
    try:
        display_fields = dict(itertools.islice(vCard.items(), 3, 11))
        for key, value in display_fields.items():
            dpg.set_value(value, "")
    except IndexError:
        pass


def generate(sender):
    """Fetch field data and build vCard."""
    user_vcard = ""
    user_input = []

    for key, value in vCard.items():
        if dpg.get_value(value):
            user_input.append(f"{key}:{dpg.get_value(value)}")
        elif dpg.get_value(value) == None:
            user_input.append(f"{key}:{value}")

    for field in user_input:
        user_vcard += f"{field}\n"

    if len(user_vcard) > 50:
        if "generate_button" in sender or "generate_menu" in sender:
            build(vcard=user_vcard.strip())
            update_preview()
        elif "save_menu" in sender:
            if os.path.isfile("output/preview.png"):
                build(dest="output/vcard.png", vcard=user_vcard.strip())
            else:
                pass
    else:
        build()
        update_preview()


def build(dest="output/preview.png", vcard="https://youtu.be/dQw4w9WgXcQ"):
    """Generates a QR code from collected field data."""

    # Check if output/ exists, else create it
    if not os.path.exists("output/"):
        os.makedirs("output/")

    # Clean up previously generated preview image
    cleanup()

    # Set up the qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the data and create the qrcode image
    qr.add_data(vcard)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(dest)

    # Resize the image - there should be a way to do this directly from qrcode??
    img = mm.open(dest)
    img2 = img.resize((330, 330))
    img2.save(dest)


if __name__ == "__main__":
    main()
