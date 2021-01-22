def remove_value(self=list([]), value=None):
    cleaned_list = list([])
    for item in list:
        if item is not None:
            cleaned_list = self.append(item)
    return cleaned_list
