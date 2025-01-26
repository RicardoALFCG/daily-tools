#!/bin/bash

# Define the directory where meeting notes will be saved
NOTES_DIR=~/Documents/Notes/Meetings
FILENAME="meeting-$(date +%F_%H-%M-%S).md"
FILEPATH="$NOTES_DIR/$FILENAME"

FILENAME_O="tranformed-meeting-$(date +%F_%H-%M-%S).md"
FILEPATH_O="$NOTES_DIR/$FILENAME_O"


# Ensure the directory exists
mkdir -p "$NOTES_DIR"

# Create and open the new meeting note in nano
nano "$FILEPATH"

# Call Fabric pattern after closing nano
echo "Running Fabric pattern for processing..."
cat "$FILENAME" | fabric -o "$FILENAME_O" -p create_meeting_note_actions 

# Confirmation message
echo "Meeting note created and processed: $FILEPATH"
echo "Transformed Meeting note created and processed: $FILEPATH_O"

