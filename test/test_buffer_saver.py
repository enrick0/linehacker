import csv
from src.buffer_saver import BufferSaver


def test_add_element():
    """Test that elements are correctly added to the buffer."""
    buffer_saver = BufferSaver()
    buffer_saver.add_element(42.5)
    buffer_saver.add_element(100.0)

    assert len(buffer_saver.buffer) == 2
    assert buffer_saver.buffer[0][1] == 42.5
    assert buffer_saver.buffer[1][1] == 100.0


def test_save_to_csv(tmp_path):
    """Test that the buffer is correctly saved to a CSV file."""
    buffer_saver = BufferSaver()
    buffer_saver.add_element(42.5)
    buffer_saver.add_element(100.0)

    # Create a temporary file path
    file_path = tmp_path / "test_output.csv"

    # Save buffer to CSV
    buffer_saver.save_to_csv(file_path)

    # Verify the contents of the CSV file
    with open(file_path, mode="r") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    # Check header
    assert rows[0] == ["Time (ms)", "Value"]

    # Check data rows
    assert len(rows) == 3  # Header + 2 data rows
    assert float(rows[1][1]) == 42.5
    assert float(rows[2][1]) == 100.0


def test_empty_buffer_save_to_csv(tmp_path):
    """Test saving an empty buffer to a CSV file."""
    buffer_saver = BufferSaver()

    # Create a temporary file path
    file_path = tmp_path / "empty_output.csv"

    # Save buffer to CSV
    buffer_saver.save_to_csv(file_path)

    # Verify the contents of the CSV file
    with open(file_path, mode="r") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    # Check header
    assert rows[0] == ["Time (ms)", "Value"]

    # Check that no data rows exist
    assert len(rows) == 1  # Only header


def test_time_in_buffer():
    """Test that the time in the buffer is correctly recorded."""
    buffer_saver = BufferSaver()
    buffer_saver.add_element(42.5)

    # Check that the time is recorded as an integer
    assert isinstance(buffer_saver.buffer[0][0], int)
    assert buffer_saver.buffer[0][1] == 42.5
