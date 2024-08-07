# Simple FL Studio MIDI Scripts

A small collection of simple MIDI controller scripts to improve user experience
when using MIDI controllers with FL Studio.

## List of scripts

### Notes and CCs to All Selected Generators

Forwards CC and note events to all selected generator plugins on the channel
rack.

### CCs to Active Plugin

Forwards CC events to the active plugin.

### Pedals to Active Generator

Forwards pedal events to the active generator plugin.

## Installation

1. Press the green "Code" button near the top of this page, then choose to
"Download ZIP".

2. Extract the `.zip` file to your Image-Line data directory, under
   `Image-Line/FL Studio/Settings/Hardware`. (By default this directory will be
   located within your documents).

3. Restart FL Studio.

4. Open the MIDI settings panel, and assign a port number to your desired
   MIDI controller. Ensure this port number is set for both the input and
   output.

5. Assign your desired script to your desired controller. The scripts in this
   repo all have names that start with "Simple:"

## Development

This project uses the Poetry build system for dependency management.

Install the project's dependencies to a Python environment by running

```sh
poetry install --no-root
```

After installing the project dependencies, you can use the following commands.

* Type checking: `poetry run mypy`
* Linting: `poetry run ruff`
