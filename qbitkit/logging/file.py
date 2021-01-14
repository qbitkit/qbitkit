from qbitkit.io import frame as __fr

def save(frame=__fr.frame.get_frame(),
         file_type='csv',
         pth=f'output'):
    __fr.frame.save_frame(frame=frame,
                          pth=pth,
                          file_type=file_type)
    return f"{pth}.{file_type}"