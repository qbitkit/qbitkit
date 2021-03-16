from qbitkit.io import frame as __fr__


def save(frame=__fr__.Frame.get_frame(),
         file_type='csv',
         pth='output'):
    """Save a given Pandas DataFrame to disk at a given path using a given file format.

    Args:
        frame(pandas.DataFrame): A Pandas DataFrame you wish to save to disk. (default pandas.DataFrame())
        file_type(str): The file format to use when saving the Pandas DataFrame to disk. (default 'csv')
        pth(str): The path you wish to write the data to. (default 'output')
    Returns:
        str: The path the file was saved to."""
    # Use the save_frame function from qbitkit to save the frame to the specified path with the specified filetype.
    __fr__.Frame.save_frame(frame=frame,
                            pth=pth,
                            file_type=file_type)
    # Return the path the new file is located at.
    return f"{pth}.{file_type}"

def save_str(self=str(''),
             filename=str('output.txt'),
             permissions=str('w')):
    """Save a given string to disk using a given file name.

    Args:
        self(str): String to save to disk. (default str(''))
        filename(str): File name to use when saving to disk. (default str('output.txt'))
        permissions(str): Permissions to use when opening file. (default str('w'))
    Returns:
        dict: Input parameters specified."""
    # Convert variables
    if self is not None:
        string = str(self)

    if filename is not None:
        filename = str(filename)

    if permissions is not None:
        permissions = str(permissions)

    # Open file on disk.
    file_on_disk = open(filename,
                        permissions)

    # Write to file on disk.
    file_on_disk.write(string)

    # Close file on disk.
    file_on_disk.close()

    # Create dict of specified parameters.
    params = dict({'string': [string],
                   'filename': [filename],
                   'permissions': [permissions]})

    # Return dict of specified parameters.
    return params