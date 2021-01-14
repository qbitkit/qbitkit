from qbitkit.io import frame as __fr


def save(frame=__fr.frame.get_frame(),
         file_type='csv',
         pth=f'output'):
    """Save a given Pandas DataFrame to disk at a given path using a given file format.

    Args:
        frame(pandas.DataFrame): A Pandas DataFrame you wish to save to disk. (default pandas.DataFrame())
        file_type(str): The file format to use when saving the Pandas DataFrame to disk. (default 'csv')
        pth(str): The path you wish to write the data to. (default 'output')
    Returns:
        str: The path the file was saved to."""
    __fr.frame.save_frame(frame=frame,
                          pth=pth,
                          file_type=file_type)
    return f"{pth}.{file_type}"
